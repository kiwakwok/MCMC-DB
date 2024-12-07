import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_steps = 500000  # Number of steps in the random walk
step_size = 1      # Step size for each random walk

# Function to perform a random walk
def random_walk(steps):
    steps = np.random.choice([-step_size, step_size], size=steps)
    return np.cumsum(steps)  # Cumulative sum to get positions

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(24, 8))

# Number of walkers for each subplot
num_walkers_list = [1, 10, 1000]

for i, num_walkers in enumerate(num_walkers_list):
    walks = np.array([random_walk(num_steps) for _ in range(num_walkers)])
    
    # Plot individual walks
    for walk in walks:
        axs[i].plot(walk, alpha=0.1, color='blue')

    # Calculate the ensemble average
    ensemble_average = np.mean(walks, axis=0)
    axs[i].plot(ensemble_average, color='red', linewidth=2, label='Ensemble Average')

    # Calculate the time average using only the first walker's trajectory
    first_walk = walks[0]
    time_average = np.zeros(num_steps)
    for j in range(num_steps):
        time_average[j] = np.mean(first_walk[:j + 1])  # Average of all previous values including itself

    axs[i].plot(time_average, color='green', linewidth=2, linestyle='--', label='Time Average (1 Walker)')

    # Set titles and labels
    axs[i].set_title(f'Random Walks: {num_walkers} Walkers')
    axs[i].set_xlabel('Time Steps')
    axs[i].set_ylabel('Position')
    axs[i].axhline(0, color='black', linewidth=0.5, linestyle='--')
    axs[i].grid()
    axs[i].legend(loc='upper left')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
