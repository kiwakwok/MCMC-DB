import numpy as np
import matplotlib.pyplot as plt
import time

# Start the timer
start_time = time.time()

# Linear Congruential Generator function
def lcg(seed, a=1664525, c=1013904223, m=2**32, n=1000000):
    x = seed
    numbers = []
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x / m)  # Normalize to [0, 1)
    return np.array(numbers)

# Generate pseudorandom numbers for histogram
n_samples_histogram = 10000000  # 1 million samples for histogram
seed1 = 42

# Generate pseudorandom numbers for the histogram
random_numbers_histogram = lcg(seed1, n=n_samples_histogram)

# Generate pseudorandom numbers for 2D scatter plot
random_numbers_x = lcg(seed1, n=1000)
seed2 = 12345
random_numbers_y = lcg(seed2, n=1000)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 12))

# Plot the histogram
ax1.hist(random_numbers_histogram, bins=50, density=True, alpha=0.5, color='lightblue', edgecolor='black')
ax1.set_title('Distribution of Pseudorandom Numbers Generated by LCG')
ax1.set_xlabel('Value (normalized to [0, 1))')
ax1.set_ylabel('Density')
# ax1.grid()

# Plot the 2D scatter plot
ax2.scatter(random_numbers_x, random_numbers_y, alpha=0.5, color='green')
ax2.set_title('2D Scatter Plot of Pseudorandom Numbers from LCG')
ax2.set_xlabel('Random Numbers (Seed 1)')
ax2.set_ylabel('Random Numbers (Seed 2)')
ax2.grid()

# Adjust layout
plt.tight_layout()
plt.show()

# End the timer
end_time = time.time()
runtime = end_time - start_time

# Print the runtime
print(f"Runtime: {runtime:.4f} seconds")
