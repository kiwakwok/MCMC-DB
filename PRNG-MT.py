import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Start the timer
start_time = time.time()

# Set the number of samples
n_samples_histogram = 1000000  # 1 million samples for histogram

# Generate pseudorandom numbers using Mersenne Twister
seed1 = 42
seed2 = 12345

# Set the seed for reproducibility
random.seed(seed1)
random_numbers_histogram = [random.random() for _ in range(n_samples_histogram)]

# Generate pseudorandom numbers for 2D scatter plot
random.seed(seed1)
random_numbers_x = [random.random() for _ in range(1000)]
random.seed(seed2)
random_numbers_y = [random.random() for _ in range(1000)]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 12))

# Plot the histogram
ax1.hist(random_numbers_histogram, bins=50, density=True, alpha=0.5, color='lightblue', edgecolor='black')
ax1.set_title('Distribution of Pseudorandom Numbers Generated by Mersenne Twister')
ax1.set_xlabel('Value (normalized to [0, 1))')
ax1.set_ylabel('Density')
# ax1.grid()

# Plot the 2D scatter plot
ax2.scatter(random_numbers_x, random_numbers_y, alpha=0.5, color='green')
ax2.set_title('2D Scatter Plot of Pseudorandom Numbers from Mersenne Twister')
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
