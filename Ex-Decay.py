import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_atoms = 1000  # Initial number of thallium atoms
half_life_minutes = 3.053  # Half-life in minutes
half_life_seconds = half_life_minutes * 60  # Convert to seconds
time_step = 1  # Time step in seconds
total_time = 1200  # Total simulation time in seconds (20 minutes)

# Calculate the number of time steps
num_steps = total_time // time_step

# Initialize array to hold the number of atoms over time
atom_counts = np.zeros(num_steps + 1)
atom_counts[0] = initial_atoms

# Simulate decay
for step in range(num_steps):
    current_atoms = int(atom_counts[step])
    
    # Calculate probability of decay in this time step
    decay_probability = 1 - 2**(-time_step / half_life_seconds)

    # Determine number of decayed atoms
    decayed_atoms = np.sum(np.random.rand(current_atoms) < decay_probability)
    
    # Update the number of atoms
    atom_counts[step + 1] = current_atoms - decayed_atoms

# Time array for plotting
time_array = np.arange(0, total_time + time_step, time_step)

# Theoretical decay values
theoretical_counts = initial_atoms * 2**(-time_array / half_life_seconds)

# Plotting the results
plt.figure(figsize=(12, 8))
plt.plot(time_array, atom_counts, linestyle='-', alpha=0.4, color='blue', label='Thallium-208')
plt.plot(time_array, theoretical_counts, linestyle='--', color='lightblue', label='Theoretical Decay')
plt.plot(time_array, initial_atoms - atom_counts, linestyle='-', alpha=0.4, color='red', label='Stable Lead-208')
plt.title('Decay of Thallium-208 over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Number of Atoms')
plt.grid()
plt.xlim(0, total_time)
plt.ylim(0, initial_atoms)
plt.legend()
plt.show()
