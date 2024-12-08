import numpy as np
import matplotlib.pyplot as plt

def initialize_lattice(size):
    """Initialize a random spin lattice."""
    return np.random.choice([-1, 1], size=(size, size))

def calculate_energy(lattice):
    """Calculate the total energy of the lattice."""
    energy = 0
    size = lattice.shape[0]
    for i in range(size):
        for j in range(size):
            spin = lattice[i, j]
            # Neighbors (periodic boundary conditions)
            neighbors = (
                lattice[(i + 1) % size, j] +
                lattice[i, (j + 1) % size] +
                lattice[(i - 1) % size, j] +
                lattice[i, (j - 1) % size]
            )
            energy -= spin * neighbors
    return energy / 2  # Each pair is counted twice

def calculate_magnetization(lattice):
    """Calculate the total magnetization of the lattice."""
    return np.sum(lattice)

def mcmc_simulation(size, temperature, steps):
    """Perform MCMC simulation and return energy and magnetization over time."""
    lattice = initialize_lattice(size)
    energies = []
    magnetizations = []
    
    for _ in tqdm(range(steps)):
        # Randomly choose a spin to flip
        i, j = np.random.randint(0, size, size=2)
        current_spin = lattice[i, j]
        # Calculate energy change if this spin is flipped
        neighbors = lattice[(i + 1) % size, j] + lattice[i, (j + 1) % size] + \
                    lattice[(i - 1) % size, j] + lattice[i, (j - 1) % size]
        delta_energy = 2 * current_spin * neighbors
        
        # Flip the spin based on Metropolis criteria
        if delta_energy <= 0 or np.random.rand() < np.exp(-delta_energy / temperature):
            lattice[i, j] *= -1
        
        # Store energy and magnetization
        energies.append(calculate_energy(lattice))
        magnetizations.append(calculate_magnetization(lattice))
    
    return energies, magnetizations

# Parameters
size = 20
steps = 1000000
temperatures = [1, 2, 5]

# Prepare subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 8))

for idx, temp in enumerate(temperatures):
    energies, magnetizations = mcmc_simulation(size, temp, steps)
    
    # Energy subplot
    axs[0, idx].plot(energies, label=f'Temp = {temp}J')
    axs[0, idx].set_title(f'Energy at {temp}J')
    axs[0, idx].set_xlabel('Steps')
    axs[0, idx].set_ylabel('Energy')
    axs[0, idx].legend()
    
    # Magnetization subplot
    axs[1, idx].plot(magnetizations, label=f'Temp = {temp}J', color='orange')
    axs[1, idx].set_title(f'Magnetization at {temp}J')
    axs[1, idx].set_xlabel('Steps')
    axs[1, idx].set_ylabel('Magnetization')
    axs[1, idx].legend()

plt.tight_layout()
plt.show()
