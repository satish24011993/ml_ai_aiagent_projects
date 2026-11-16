import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1/(1+np.exp(-z))

x = np.linspace(-10,10,100)
sigmoid_values = sigmoid(x)


plt.plot(x,sigmoid_values)
plt.title('Sigmoid Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()