from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

data = load_iris(as_frame=True)

X,y = data.data,data.target

model = RandomForestClassifier(random_state=42)
kfold = KFold(n_splits=5,shuffle=True,random_state=42)
cross_val = cross_val_score(model,X,y,scoring='accuracy',cv=kfold)


print('Cross validation scores',cross_val)
print('Mean Accuracy', cross_val.mean())