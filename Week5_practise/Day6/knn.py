from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

data = load_iris(as_frame=True)
X,y = data.data,data.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)



scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
y_pred_lr = model.predict(X_test)

print('Logistic regression Accuracy:', accuracy_score(y_test, y_pred_lr))

best_knn = 5

knn = KNeighborsClassifier(n_neighbors=best_knn)
knn.fit(X_train,y_train)
y_pred_knn = knn.predict(X_test)

print('KNN accuracy:', accuracy_score(y_test, y_pred_knn))

print('Logistic regression classification report:', classification_report(y_test, y_pred_lr))

print('KNN classification report:', classification_report(y_test, y_pred_knn))

# for k in range(1,11):
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_train,y_train)

#     y_pred = knn.predict(X_test)
#     acc = accuracy_score(y_test, y_pred)
#     print(f'k-neighbor:{k}, Accuracy:{acc:.2f}')