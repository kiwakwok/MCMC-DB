import matplotlib.pyplot as plt
import numpy as np

# Create a 5x5 grid for the chessboard
rows, cols = 5, 5

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Set the limits and grid
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.set_xticks(np.arange(0, cols + 1, 1))
ax.set_yticks(np.arange(0, rows + 1, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(which='both')

# Draw the arrows in a 5x5 pattern
for i in range(rows):
    for j in range(cols):
        # Center position of the arrow
        x = j + 0.5
        y = i + 0.5

        # Choose arrow color and direction
        if (i + j) % 3 == 0:  # Up arrow for even positions
            ax.annotate('', xy=(x, y + 0.2), xytext=(x, y - 0.2),
                        arrowprops=dict(facecolor='blue', edgecolor='blue', arrowstyle='->', lw=2))
        else:  # Down arrow for odd positions
            ax.annotate('', xy=(x, y - 0.2), xytext=(x, y + 0.2),
                        arrowprops=dict(facecolor='red', edgecolor='red', arrowstyle='->', lw=2))

# Set aspect of the plot to be equal
ax.set_aspect('equal')
plt.title('Ising Model')
plt.show()
