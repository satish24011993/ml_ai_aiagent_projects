import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score, recall_score,f1_score, classification_report


np.random.seed(42)
n_samples = 200
X = np.random.rand(n_samples,2)*10
y = (X[:,0]*1.5+X[:,1]>15).astype(int)

df = pd.DataFrame(X,columns=['Age','Salary'])
df['Purchase'] = y

X_train,X_test,y_train, y_test = train_test_split(df[['Age','Salary']], df['Purchase'], test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Accuracy Score', accuracy_score(y_test,y_pred))
print('Precision Score', precision_score(y_test,y_pred))
print('Recall Score', recall_score(y_test,y_pred))
print('F1 Score', f1_score(y_test,y_pred))
print('\n Classification Report \n', classification_report(y_test,y_pred))

x_min, x_max = (X[:,0].min()-1,X[:,0].max()+1)
y_min, y_max = (X[:,1].min()-1,X[:,1].max()+1)

xx,yy = np.meshgrid(np.arange(x_min,x_max,0.1),np.arange(y_min, y_max,0.1))

# Prediction probabilities of mesh grid
Z = model.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx,yy,Z,cmap='coolwarm',alpha=0.8)
plt.scatter(X_test['Age'],X_test['Salary'],c = y_test,cmap='coolwarm', edgecolors='k')
plt.title('Logistic Regression Boundry analysis')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()