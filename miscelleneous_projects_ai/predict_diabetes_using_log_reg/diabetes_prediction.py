# Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the pima diabetes dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/refs/heads/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI',
                'DiabetesPedigreeFunction', 'Age','Outcome']

df = pd.read_csv(url, names=column_names)

print("Diabetes Dataset:")
print(df.head())

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# model evaluation
accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True, cmap='Blues', fmt="d")
plt.title("Diabetes Prediction Actual Vs Predicted")
plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")
plt.show()

class_report = classification_report(y_test,y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report: {class_report}")
new_data = pd.DataFrame({
    'Pregnancies':[5], 'Glucose':[130], 'BloodPressure':[73], 'SkinThickness':[24],'Insulin':[168],'BMI':[44],
                'DiabetesPedigreeFunction':[0.450], 'Age':[33]
})


predicted = model.predict(new_data)

print(f"Predicted data: {predicted}")