import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures


np.random.seed(42)
X = np.random.rand(100,1)*10
y = 3 * X**2 - 2*X + np.random.randn(100, 1) * 5

# Transform feature to Polynomial
poly_features = PolynomialFeatures(degree=2,include_bias=False)
X_poly = poly_features.fit_transform(X)
# print(X_poly)

model = LinearRegression()
model.fit(X_poly,y)

y_pred = model.predict(X_poly)

# Plots for actual and predicted
plt.scatter(X,y,color='blue', label='Actual')
plt.scatter(X, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


mse = mean_squared_error(y, y_pred)
print(mse)
