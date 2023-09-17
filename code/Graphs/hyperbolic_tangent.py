import numpy as np
import matplotlib.pyplot as plt

# Define the hyperbolic tangent function


def tanh(x):
    return np.tanh(x)


# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values using tanh
y = tanh(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='tanh(x)')
plt.title('Plot of the Hyperbolic Tangent Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(False)
plt.show()
