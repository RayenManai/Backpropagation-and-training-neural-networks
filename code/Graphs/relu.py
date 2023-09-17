import numpy as np
import matplotlib.pyplot as plt

# Define the function you want to plot


def my_function(x):
    return np.maximum(0, x)


# Generate x values
x = np.linspace(-10, 10, 400)  # Create an array of x values from -10 to 10

# Calculate corresponding y values
y = my_function(x)

# Create the plot
plt.figure(figsize=(8, 6))  # Set the figure size
plt.plot(x, y, label='ReLU(x)')  # Plot the function
plt.title('Plot of the ReLU Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # Display legend
plt.grid(False)
plt.show()  # Show the plot
