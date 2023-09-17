import numpy as np
import matplotlib.pyplot as plt

# Define the Leaky ReLU function


def leaky_relu(x, alpha=0.1):
    return np.where(x > 0, x, alpha * x)


# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values using Leaky ReLU
y = leaky_relu(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Leaky ReLU(x)')
plt.title('Plot of the Leaky ReLU Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(False)
plt.show()
