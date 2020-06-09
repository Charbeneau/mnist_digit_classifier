import logging
import sys
import tensorflow as tf


logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.info('Downloading MNIST data.')
mnist = tf.keras.datasets.mnist

logger.info('Creating train and test data sets.')
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

logger.info('Defining model.')
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),  # noqa: E501
                                    tf.keras.layers.Dense(128, activation='relu'),  # noqa: E501
                                    tf.keras.layers.Dropout(0.2),
                                    tf.keras.layers.Dense(10)])

logger.info('Defining loss function.')
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

logger.info('Compiling model.')
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

logger.info('Fitting model.')
model.fit(x_train, y_train, epochs=5)

logger.info('Test data performance.')
logger.info(model.evaluate(x_test,  y_test, verbose=2))

logger.info('Saving model as mnist_model.')
model.save('mnist_model')
