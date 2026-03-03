import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

# 16 frequencies (Option B)
frequencies = np.linspace(100, 1600, 16).reshape(4, 4)

fig, ax = plt.subplots(figsize=(6, 6))

hex_radius = 1
dx = 3/2 * hex_radius
dy = np.sqrt(3) * hex_radius

for row in range(4):
    for col in range(4):
        x = col * dx
        y = row * dy + (col % 2) * (dy / 2)

        hexagon = RegularPolygon(
            (x, y),
            numVertices=6,
            radius=hex_radius,
            orientation=np.radians(30),
            edgecolor='black',
            facecolor='lightblue'
        )

        ax.add_patch(hexagon)
        ax.text(x, y, f"{int(frequencies[row][col])}",
                ha='center', va='center', fontsize=9)

ax.set_aspect('equal')
ax.axis('off')
plt.show()