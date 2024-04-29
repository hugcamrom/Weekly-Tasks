
'''
Write a program called plottask.py that displays:

A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
Make the plot look nice (legend etc).

'''


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
values = np.random.normal(loc=5, scale=2, size=1000)

# Create histogram
plt.hist(values, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution')

# Generate x values for the function h(x) = x^3
x = np.linspace(0, 10, 100)
y = x**3

# Plot the function h(x) = x^3
plt.plot(x, y, color='red', label='$h(x) = x^3$')

# Set plot title and labels
plt.title('Histogram and Function Plot')
plt.xlabel('Value')
plt.ylabel('Density / $h(x)$')

# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()