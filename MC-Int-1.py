import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Function to determine if a point is inside the irregular closed shape
def is_inside_shape(x, y):
    # Example: Define a star-like shape using vertices
    vertices = np.array([[0.5, 0.9], [0.6, 0.6], [1.0, 0.6],
                         [0.7, 0.4], [0.8, 0.1], [0.5, 0.3],
                         [0.2, 0.1], [0.3, 0.4], [0.0, 0.6],
                         [0.4, 0.6]])
    
    # Create a polygon from the vertices
    polygon = Polygon(vertices, closed=True, fill=None, edgecolor='black')

    # Use a point-in-polygon test
    from matplotlib.path import Path
    path = Path(vertices)
    return path.contains_points(np.vstack((x, y)).T)

# Number of random points
N = 1000

# Generate random points in the unit square [0, 1] x [0, 1]
x = np.random.rand(N)
y = np.random.rand(N)

# Determine points inside the irregular shape
inside_shape = is_inside_shape(x, y)

# Create the plot
plt.figure(figsize=(8, 8))
plt.scatter(x[inside_shape], y[inside_shape], color='blue', label='Inside Shape', alpha=0.5)
plt.scatter(x[~inside_shape], y[~inside_shape], color='red', label='Outside Shape', alpha=0.5)

# Plot the irregular closed shape
vertices = np.array([[0.5, 0.9], [0.6, 0.6], [1.0, 0.6],
                     [0.7, 0.4], [0.8, 0.1], [0.5, 0.3],
                     [0.2, 0.1], [0.3, 0.4], [0.0, 0.6],
                     [0.4, 0.6]])
plt.plot(*zip(*np.append(vertices, [vertices[0]], axis=0)), color='black', linewidth=2)

# Set limits and aspect
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')

# Add title and legend
# plt.title('Monte Carlo Integration: Closed Irregular Shape in a Unit Square')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
plt.legend(loc='lower right')
plt.grid()
plt.show()
