import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3 * X**2 + 2*X + np.random.randn(100,1)*5

poly_feat = PolynomialFeatures(degree=2,include_bias=False)

X_poly = poly_feat.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y,test_size=0.2,random_state=42)

# Ridge
ridge = Ridge(alpha=1)
ridge_model = ridge.fit(X_train,y_train)
ridge_prediction = ridge_model.predict(X_test)

# Lasso
lasso = Lasso(alpha=1)
lasso_model = lasso.fit(X_train,y_train)
lasso_prediction = lasso_model.predict(X_test)

Ridge_mse = mean_squared_error(y_test, ridge_prediction)
print('Ridge MSE',Ridge_mse)

Lasso_mse = mean_squared_error(y_test, lasso_prediction)
print('Lasso MSE',Lasso_mse)