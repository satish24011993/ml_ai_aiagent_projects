import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Telco-Customer-Churn.csv')

# X = df.drop('Churn')
# y = df['Churn']



le = LabelEncoder()
df['Churn'] = le.fit_transform(df['Churn'])
df['gender'] = le.fit_transform(df['gender'])
df['Partner'] = le.fit_transform(df['Partner'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
print(df.head())

X = df.drop(columns=['Churn','customerID'])
y = df['Churn']

print(X.columns)

X_cols = [col for col in X.columns if X[col].dtype in ['int','float']]
X = X[X_cols]
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(n_jobs=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

print('Logistic regression Confusion Matrix:',confusion_matrix(y_test, y_pred))

print('KNN confusion matrix:', confusion_matrix(y_test, y_pred_knn))


print('Logistic regression Classification report:',classification_report(y_test, y_pred))

print('KNN Classification report:', classification_report(y_test, y_pred_knn))
# sns.countplot(x = 'Churn', data=df)
# plt.title('Churn Distribution')
# plt.show()