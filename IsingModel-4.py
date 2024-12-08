import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

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
    return energy / 2  # Each pair counted twice

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
        neighbors = (
            lattice[(i + 1) % size, j] +
            lattice[i, (j + 1) % size] +
            lattice[(i - 1) % size, j] +
            lattice[i, (j - 1) % size]
        )
        delta_energy = 2 * current_spin * neighbors
        
        # Flip the spin based on Metropolis criteria
        if delta_energy <= 0 or np.random.rand() < np.exp(-delta_energy / temperature):
            lattice[i, j] *= -1
        
        # Store energy and magnetization
        energies.append(calculate_energy(lattice))
        magnetizations.append(calculate_magnetization(lattice))
    
    return np.mean(energies), np.mean(magnetizations), np.var(energies), np.var(magnetizations)

# Parameters
size = 20
steps = 1000000  # Number of MCMC steps
temperatures = np.linspace(1, 5, 81)  # Temperature range from 1J to 5J

# Arrays to store results
energies = []
magnetizations = []
specific_heats = []
susceptibilities = []

# Run simulation for each temperature
for T in temperatures:
    mean_energy, mean_magnetization, energy_variance, magnetization_variance = mcmc_simulation(size, T, steps)
    
    energies.append(mean_energy)
    magnetizations.append(mean_magnetization)
    specific_heats.append(energy_variance / (T**2))  # C = variance / T^2
    susceptibilities.append(magnetization_variance / T)  # χ = variance / T

# Plotting results
plt.figure(figsize=(12, 10))

# Energy plot
plt.subplot(2, 2, 1)
plt.scatter(temperatures, energies, marker='o')
plt.title('Energy vs Temperature')
plt.xlabel('Temperature (J)')
plt.ylabel('Average Energy')
plt.grid()

# Magnetization plot
plt.subplot(2, 2, 2)
plt.scatter(temperatures, magnetizations, marker='o', color='orange')
plt.title('Average Magnetization vs Temperature')
plt.xlabel('Temperature (J)')
plt.ylabel('Average Magnetization')
plt.ylim(ymin=0)
plt.grid()

# Specific Heat plot
plt.subplot(2, 2, 3)
plt.scatter(temperatures, specific_heats, marker='o', color='green')
plt.title('Specific Heat vs Temperature')
plt.xlabel('Temperature (J)')
plt.ylabel('Specific Heat')
plt.ylim(ymin=0)
plt.grid()

# Susceptibility plot
plt.subplot(2, 2, 4)
plt.scatter(temperatures, susceptibilities, marker='o', color='red')
plt.title('Susceptibility vs Temperature')
plt.xlabel('Temperature (J)')
plt.ylabel('Susceptibility')
plt.ylim(ymin=0)
plt.grid()

plt.tight_layout()
plt.show()
