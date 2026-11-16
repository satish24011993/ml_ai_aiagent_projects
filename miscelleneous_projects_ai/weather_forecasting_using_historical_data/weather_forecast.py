import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = {
    'Day':[1,2,3,4,5,6,7,8,9,10],
    'Temperature':[30,32,34,31,29,28,35,33,30,31],
    'Humidity':[60, 62, 64, 58, 55, 57,65, 63, 59, 61],
    'Wind Speed':[10, 12, 8, 11, 9, 10, 13, 12, 10, 11],
    'Precipitation':[0,0,1,0,1,1,0,0,1,0],
    'Next Day Temperature':[32,34,31,29,28,35,33,30,31,32]
}

df = pd.DataFrame(data)

X = df.drop('Next Day Temperature',axis=1)
y = df['Next Day Temperature']

# splitting training and testing data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Model fitting
model = LinearRegression()
model.fit(X_train, y_train)

# Model prediction
y_pred = model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.figure(figsize=(10,6))
plt.plot(y_test.values, label='Actual Temperatures', marker="o")
plt.plot(y_pred, label='Predicted Temperatures', marker='x')
plt.title('Actual vs Predicted Temperatures')
plt.xlabel('Test Sample Index')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# coeff and intercept
print(f"Intercept, {model.intercept_}")
print(f"Coefficients, {model.coef_}")

# coefficient dataset
data = pd.DataFrame(model.coef_, X.columns, columns=['Coefficients'])

print(data)

new_data = pd.DataFrame({
    'Day':[11],
    'Temperature':[23],
    'Humidity':[54],
    'Wind Speed':[12],
    'Precipitation':[0]
})

prediction = model.predict(new_data)
print('Prediction Score:', prediction[0])