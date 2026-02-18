from collections import Counter
import math

# Training data (x1, x2) and labels
X_train = [[1,2], [2,3], [3,3], [6,5], [7,7], [8,6]]
y_train = ['A', 'A', 'A', 'B', 'B', 'B']

# Test point
x_test = [5,5]
k = 3

# Euclidean distance
def euclidean(a,b):
    return math.sqrt(sum((ai - bi)**2 for ai, bi in zip(a,b)))

# Compute distances
distances = [(euclidean(x_test, x_train), label) for x_train, label in zip(X_train, y_train)]
distances.sort(key=lambda x: x[0])

# Take k nearest
nearest_labels = [label for _, label in distances[:k]]
prediction = Counter(nearest_labels).most_common(1)[0][0]

print("Predicted class:", prediction)