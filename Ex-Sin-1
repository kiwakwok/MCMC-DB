import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    return np.sin(x)  # Example function

# Parameters
V = 1  # Volume of integration (for 1D, it's just the length)
N = 1000000  # Number of samples

# Monte Carlo integration
samples = np.random.uniform(0, 1, N)  # Sample uniformly from [0, 1]
f_values = f(samples)

# Calculate integral estimate
I_estimate = V * np.mean(f_values)
f_square_mean = np.mean(f_values**2)
sigma = np.sqrt(f_square_mean - np.mean(f_values)**2)
error_estimate = V * sigma / np.sqrt(N)

# True value of the integral from 0 to 1
I_true = 1 - np.cos(1)  # Exact value of the integral of sin(x) from 0 to 1

# Calculate the percentage difference
percentage_difference = abs((I_true - I_estimate) / I_true) * 100

# Print results
print(f"Estimated Integral: {I_estimate:.6f}")
print(f"Estimated Error: {error_estimate:.6f}")
print(f"True Value of Integral: {I_true:.6f}")
print(f"Percentage Difference: {percentage_difference:.6f}%")

# Calculate the mean value of f(x)
mean_value = np.mean(f_values)

# Visualize the distribution of f(x_n)
plt.figure(figsize=(12, 8))
plt.hist(f_values, bins=50, density=True, alpha=0.4, color='green', label='Distribution of sin(x)')
plt.axvline(mean_value, alpha=0.5, color='red', linestyle='--', label='Mean Value of sin(x)')
plt.title('Distribution of sin(x)')
plt.xlabel('sin(x)')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()
