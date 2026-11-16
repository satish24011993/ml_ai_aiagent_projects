import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

data = pd.read_csv(url)

print(data.info())

print('dataset preview:',data.head())


# Applying One-Hot Encoding
df_one_hot = pd.get_dummies(data, columns=['Sex','Embarked'], drop_first=True)

print('\n One - hot encoded dataset:\n', df_one_hot.head())

encoder = LabelEncoder()

data['Pclass_encoded'] = encoder.fit_transform(data['Pclass'])

print('\n Label encoded dataset:')
print(data[['Pclass','Pclass_encoded']].head())

# Apply Frequency Encoding
data['Ticket_frequency'] = data['Ticket'].map(data['Ticket'].value_counts())

print('\n Frequency encoded feature')
print(data[['Ticket','Ticket_frequency']].head())

X = df_one_hot.drop(columns=['Survived', 'Name','Age', 'Ticket', 'Cabin'])
y = data['Survived']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print('Accuracy with One-Hot Encoding', accuracy_score(y_test,y_pred))

