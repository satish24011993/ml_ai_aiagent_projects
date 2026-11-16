from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder

import seaborn as sns
import matplotlib.pyplot as plt

data = fetch_california_housing(as_frame=True)
df = data.frame

# Inspect data
print(df.info())
print(df.describe())

# Visualize the relationships
# sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
# plt.show()

# # Check for missing values
print('Missing values: \n', df.isnull().sum())

X = df[['MedInc','AveRooms','HouseAge']]
y = df['MedHouseVal']
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print('MSE of model:', mean_squared_error(y_test,y_pred))
# print('Accuracy of model:', accuracy_score(y_test, y_pred))