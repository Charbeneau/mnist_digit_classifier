from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow import keras
import re
import base64
import sys
import os


app = Flask(__name__)
global model

# This is **NOT** how I wanted to log; it's what I could get to work.
print('Loading model.', file=sys.stderr)
model = keras.models.load_model('mnist_model')


def parse_image(data):
    '''Parse image data input by user.

    Parameters
    ----------
    data: (bytestring)

    Creates
    -------
    output.png
    '''

    image_str = re.search(b'base64,(.*)', data).group(1)
    print('Creating output.png.', file=sys.stderr)
    with open('output.png', 'wb') as output:
        output.write(base64.decodebytes(image_str))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict/', methods=['GET', 'POST'])
def predict():

    print('Parsing image.', file=sys.stderr)
    parse_image(data=request.get_data())

    print('Reading in output.png.', file=sys.stderr)
    x = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)

    print('Inverting, resizing, and reshaping.', file=sys.stderr)
    x = np.invert(x)
    x = cv2.resize(x, (28, 28))
    x = x.reshape(1, 28, 28)

    print('Predicting.', file=sys.stderr)
    out = model.predict(x)
    response = np.array_str(np.argmax(out, axis=1))
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
