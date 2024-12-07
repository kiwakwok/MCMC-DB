import numpy as np

# Function definitions
def f(x):
    return x**(-1/3) + x/10

def g(x):
    return (2/3) * x**(-1/3)

# Monte Carlo integration using uniform distribution
def monte_carlo_uniform(n):
    x_samples = np.random.uniform(0, 1, n)
    f_samples = f(x_samples)
    integral_estimate = np.mean(f_samples)
    variance = np.var(f_samples)
    error = np.sqrt(variance / n)
    return integral_estimate, error

# Monte Carlo integration using importance sampling
def monte_carlo_importance(n):
    x_samples = np.random.uniform(0, 1, n)
    weights = g(x_samples**(3/2))
    f_samples = f(x_samples**(3/2))
    
    # Normalizing the weights
    integral_estimate = np.mean(f_samples / weights)  # Integral of g(x) from 0 to 1
    variance = np.var(f_samples / weights)
    error = np.sqrt(variance / n)
    return integral_estimate, error

# Number of samples
N = 100000

# True value of the integral
true_val = 31/20

# Uniform distribution integration
estimate_uniform, error_uniform = monte_carlo_uniform(N)

# Importance sampling integration
estimate_importance, error_importance = monte_carlo_importance(N)

# Output results
print(f"True value of the integral: {true_val:.4f}")
print(f"Uniform Distribution: Estimate = {estimate_uniform:.5f}, Error = {error_uniform:.5f}")
print(f"Importance Sampling: Estimate = {estimate_importance:.5f}, Error = {error_importance:.5f}")
