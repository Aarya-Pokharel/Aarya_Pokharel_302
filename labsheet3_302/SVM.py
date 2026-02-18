from sklearn import svm

# Training data
X_train = [[2,3], [1,1], [2,1], [6,7], [7,8], [8,6]]
y_train = [0, 0, 0, 1, 1, 1]  # Classes

# Create SVM classifier
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

# Test data
X_test = [[3,3], [7,7]]
y_pred = clf.predict(X_test)

print("Predicted classes:", y_pred)