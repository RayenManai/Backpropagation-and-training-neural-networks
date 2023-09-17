import numpy as np
import matplotlib.pyplot as plt

# Define the logistic sigmoid function


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values using sigmoid
y = sigmoid(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sigmoid(x)')
plt.title('Plot of the Logistic Sigmoid Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(False)
plt.show()
