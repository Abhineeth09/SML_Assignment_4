# Secure Computation For ML_Assignment_4
The library Tensorflow encrypted is used to implement a two party privacy preserving logistic regression. As discussed in the office hours on Thursday(04/22/2021), I have changed the sigmoid function to the piecewise function to make the logistic regression work in the way the question describes it.
The link below links to the library -
https://github.com/tf-encrypted/tf-encrypted

TF-encrypted has an implementation of privacy preserving logistic regression. Using the same, I assumed two parties, Alice and Bob that want to implement the logistic regression.
The dataset contains 7000 samples with 32 features, 16 are held by Alice and 16 are with Bob. Both of the datasets are included in the folder. The goal is to detect fraud using this data(Let’s say Alice is a bank and Bob is a government and both have data from common individuals).
In the folder I have enclosed we have -
training_alice.py
Implements the Logistic Regression from Alice’s side.
training_bob.py
Implements the Logistic Regression from Bob’s side.
training_server.py
Implements the server side logic.
common.py
This file implements the logistic regression.
pond.py
This is a standard file in the library which can be found at
https://github.com/tf-encrypted/tf-encrypted/blob/master/tf_encrypted/protocol/pond/pond.py#L1 215
I have modified this file and added the function apply_piecewise(x) which accepts a Tensor and applies the piecewise function to each element of the tensor. This function replaces the sigmoid() function in the original code.
       
Note: This file is directly edited from the library folder, the copy attached here is just to show the code. To run it, this file must be placed in the library path.
aliceTrainFile.csv
Training data from Alice.
bobTrainFileWithLabel.csv
Training data from Bob, along with the class label for fraud.
config.json
Config contains the ip addresses of Alice, Bob and the Server. This has run on the local machine hence the localhost is assigned with different ports for each of these.
Results-
This is the implementation of the piecewise function. The function takes in a PonsPrivateTensor, converts it into a Numpy array, applies the piecewise function to each element, converts it back into a PondPrivateTensor(This type of tensor is required by the library) and returns the same.
