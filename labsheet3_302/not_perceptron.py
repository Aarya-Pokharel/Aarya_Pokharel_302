# Perceptron for NOT Gate

# Input and target
X = [0, 1]
T = [1, 0]

# Initialize weight and bias
w = 0
b = 0.5   # Bias chosen to invert input
lr = 0.1

# Step activation
def step(net):
    return 1 if net >= 0 else 0

# Training (since NOT gate is very simple, one pass is enough)
for i in range(len(X)):
    net = w*X[i] + b
    output = step(net)
    error = T[i] - output
    w += lr * error * X[i]   # Update weight
    b += lr * error           # Update bias
    print(f"Input: {X[i]}, Output: {output}, Target: {T[i]}")

# Testing
print("\nTesting NOT Gate:")
for x in X:
    print(x, "->", step(w*x + b))