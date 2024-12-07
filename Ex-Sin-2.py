import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.sin(x)

# Define the x values
x = np.linspace(0, np.pi, 100)  # 100 points from 0 to pi
y = f(x)

# Create the plot
plt.figure(figsize=(12, 8))
# plt.figure(figsize=(10, 5))
plt.plot(x, y, label='y = sin(x)', color='blue')

# Fill the area under the curve from x = 0 to x = 1
x_fill = np.linspace(0, 1, 100)  # x values to fill
y_fill = f(x_fill)  # y values for the fill
plt.fill_between(x_fill, y_fill, color='lightblue', alpha=0.5, label='Area from 0 to 1')

# Add labels and title
plt.title('Area Under sin(x) from 0 to 1')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.xlim(0, np.pi)
plt.ylim(0, 1.5)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.grid()

# Show the plot
plt.show()
