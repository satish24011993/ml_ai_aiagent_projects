# import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, f1_score, recall_score
import seaborn as sns
import matplotlib.pyplot as plt

# https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones
data = pd.read_csv('mnist_train.csv')

# Preprocess the dataset
X = data.drop('Activity', axis=1)
y = data['Activity']

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# model fitting
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# model evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')


print(f"Accuracy: {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"f1 score: {f1*100:.2f}%")
print(f"Recall: {recall*100:.2f}%")


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Digit Recogintion Confusion Matrix')
plt.show()



