import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge,Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt


data = fetch_california_housing(as_frame=True)
df = data.frame

X = df[['MedInc']]
y = df[['MedHouseVal']]

poly = PolynomialFeatures(degree=2,include_bias=False)
X_poly = poly.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Ridge
ridge = Ridge(alpha=10)
ridge.fit(X_train, y_train)
ridge_prediction = ridge.predict(X_test)


# Lasso
lasso = Lasso(alpha=10)
lasso.fit(X_train, y_train)
lasso_prediction = lasso.predict(X_test)
plt.figure(figsize=(20,10))
plt.scatter(X_test[:,0], y_test,color='blue', label='Actual values', alpha=0.5)
plt.scatter(X_test[:,0], ridge_prediction, color='red', label='Ridge Predicted value', alpha=0.5)
plt.scatter(X_test[:,0], lasso_prediction, color='green', label='Lasso Predicted value', alpha=0.5)
plt.title('Ridge Vs Lasso graph')
plt.xlabel('Median of Income Transformed')
plt.ylabel('Median of House value')
plt.legend()
plt.show()


r_mse = mean_squared_error(y_test, ridge_prediction)
l_mse = mean_squared_error(y_test, ridge_prediction)

print('Ridge mse', r_mse)
print('Lasso mse', l_mse)
