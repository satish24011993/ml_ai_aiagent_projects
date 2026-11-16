# Import necessary libraries
import numpy as np

# Sigmoid activation function and its derivatives
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

# Mean Squared Error(MSE) Loss Function
def mean_squared_errr(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))

# Basic Neural Network Class
class BasicNeuralNetwork:
    