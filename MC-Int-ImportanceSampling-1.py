import numpy as np
import matplotlib.pyplot as plt

# Define the range for x, avoiding zero to prevent division by zero
x = np.linspace(0.01, 1, 100)

# Define the functions
f_x = x**(-1/3) + x/10
g_x = (2/3) * x**(-1/3)

# Calculate the ratio
h_x = f_x / g_x

# Create the plot
plt.figure(figsize=(12, 12))
plt.plot(x, f_x, label=r'$f(x) = x^{-1/3} + \frac{x}{10}$', color='blue')
plt.plot(x, g_x, label=r'$g(x) = \frac{2}{3} x^{-1/3}$', color='orange')
plt.plot(x, h_x, label=r'$h(x) = \frac{f(x)}{g(x)}$', color='green')

# Add labels and title
plt.title('Plot of $f(x)$, $g(x)$, and $h(x)$')
plt.xlabel('x')
plt.ylabel('Function value')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.xlim(0, 1)
plt.ylim(0, 5)  # Adjust y-limits for better visibility
plt.show()
