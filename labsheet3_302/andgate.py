
# Training data (AND gate)
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

targets = [0, 0, 0, 1]

# Initialize weights and bias
w1 = 0
w2 = 0
bias = -1.5
learning_rate = 1

# Step activation function
def step(net):
    return 1 if net >= 0 else 0

# Training the perceptron
epochs = 10
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}")
    for i in range(len(inputs)):
        x1, x2 = inputs[i]
        target = targets[i]

        # Net input calculation
        net = w1 * x1 + w2 * x2 + bias
        output = step(net)

        # Weight update
        error = target - output
        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        bias = bias + learning_rate * error

        print(f"Input: {inputs[i]} Output: {output} Target: {target}")

# Testing
print("\nFinal Weights and Bias")
print("w1 =", w1, "w2 =", w2, "bias =", bias)

print("\nTesting AND Gate")
for x in inputs:
    net = w1 * x[0] + w2 * x[1] + bias
    print(f"Input: {x} Output:", step(net))