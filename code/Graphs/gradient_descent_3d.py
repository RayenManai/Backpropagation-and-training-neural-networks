import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D function (you can change this to any function you want)


def function_to_optimize(x, y):
    return x**2 + y**2

# Define the gradient of the function


def gradient(x, y):
    df_dx = 2 * x
    df_dy = 2 * y
    return df_dx, df_dy


# Gradient descent hyperparameters
learning_rate = 0.1
num_iterations = 20

# Starting point
x_start, y_start = 3, 4

# Lists to store the values of x, y, and the function value during optimization
x_values = [x_start]
y_values = [y_start]
function_values = [function_to_optimize(x_start, y_start)]

# Gradient descent optimization loop
for i in range(num_iterations):
    df_dx, df_dy = gradient(x_start, y_start)
    x_start -= learning_rate * df_dx
    y_start -= learning_rate * df_dy
    x_values.append(x_start)
    y_values.append(y_start)
    function_values.append(function_to_optimize(x_start, y_start))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate a grid of points for the function surface
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = function_to_optimize(X, Y)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Plot the optimization steps
ax.plot(x_values, y_values, function_values,
        marker='o', linestyle='-', color='red')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
ax.set_title('Gradient Descent Optimization')

plt.show()
