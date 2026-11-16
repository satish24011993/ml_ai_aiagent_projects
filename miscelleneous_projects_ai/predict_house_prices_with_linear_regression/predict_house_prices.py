# Import necessary libraries
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


# Load the California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Create a Dataframe from the dataset
df = housing.frame

print('California housing data:')
print(df.head(5))

# Features (Independent Variable) and Target(dependent variable)
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# model evaluation
mean_squared_error_score = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mean_squared_error_score}")
print(f"R2 Score: {r2}")

print("Model Coefficients:")
print(f"Intercept: {model.intercept_}")
print(f"Coeffcients: {model.coef_}")

coef_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficent'])

print("Coefficients for each feature")
print(coef_df)

# Test the model with new data
new_data = pd.DataFrame({
    'MedInc':[5],
    'HouseAge':[30],
    'AveRooms': [6],
    'AveBedrms': [1],
    'Population': [500],
    'AveOccup':2,
    'Latitude': [40],
    'Longitude':[-118.25]
})

predicted_price = model.predict(new_data)
print(f"Predicted data: {predicted_price}")