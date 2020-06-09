# mnist_digit_classifier
Let's classify some handwritten digits!

# Overview

In this repo, a simple model is fit to the MINST data set, and a Flask app allows the user to write a digit 0-9 by hand, which is subsequently classified by the model.

# Starting Material

Here's what I used to get started.

 - [Model](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb)
 - [Server](https://github.com/akashdeepjassal/mnist-flask)

# Requirements

- [Docker](https://www.docker.com/products/docker-desktop)
  - This was written using version 19.03.5, build 633a0ea.
- [make](https://www.gnu.org/software/make/manual/make.html)
  - This was written using version 3.81.

# Short Usage

0. Build and run the containers in one go.
```
make run
```

1. Go to [http://localhost:5000/](http://localhost:5000/).

2. Write a digit 0-9, and press 'Predict'.

3. Behold the prediction.

# Step by Step Usage

0. Build the model container.
```
make build_model
```

1. Fit the model, and put the serialized results in the appropriate directory.
```
make fit_model
```

2. Build the server.
```
make build_server
```

3. Run the server.
```
make run_server
```

4. Go to [http://localhost:5000/](http://localhost:5000/).

5. Write a digit 0-9, and press 'Predict'.

6. Behold the prediction.
