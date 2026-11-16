import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generate synthetic data
X = np.random.rand(100,1,)*100
y = 3 * X + np.random.randn(100,1)*2

# print('X',X)
# print('y',y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Coefficients
print('Slope:', model.coef_[0][0])
print('Intercept:', model.intercept_[0])

plt.scatter(X_test,y_test, color="blue", label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


print('Gradient descent MSE:', mean_squared_error(y_test, y_pred))
print('r_squared:', r2_score(y_test,y_pred))