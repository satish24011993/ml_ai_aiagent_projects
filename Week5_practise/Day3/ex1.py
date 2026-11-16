import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


data = fetch_california_housing(as_frame=True)
df = data.frame

X = df[['MedInc']]
y = df[['MedHouseVal']]

poly_feat = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_feat.fit_transform(X)

# X_train, y_train, X_test, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)


# Visualize the output
plt.figure(figsize=(10,5))
plt.scatter(X, y, color='blue',label='Actual Values',alpha=0.5)
plt.plot(X, y_pred,color='red', label='Predicted', alpha=0.5)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()


mse = mean_squared_error(y, y_pred)
print('mean_squared_error',mse)