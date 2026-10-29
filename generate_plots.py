import matplotlib.pyplot as plt
import numpy as np
import os

fig = plt.figure(figsize=(9, 8), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Grid
r = np.linspace(0, 2.2, 50)
theta = np.linspace(0, 2*np.pi, 80)
R, Theta = np.meshgrid(r, theta)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = X**2 + Y**2

# Surface with colormap and slight transparency
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.55, edgecolor='gray', linewidth=0.2, antialiased=True)

# Add level contours on the surface (like the circles drawn on the blackboard)
levels = [0.8, 1.8, 3.2, 4.6]
for lvl in levels:
    circ_theta = np.linspace(0, 2*np.pi, 100)
    circ_r = np.sqrt(lvl)
    circ_x = circ_r * np.cos(circ_theta)
    circ_y = circ_r * np.sin(circ_theta)
    circ_z = np.full_like(circ_x, lvl)
    ax.plot(circ_x, circ_y, circ_z, color='darkblue', linewidth=2.2, linestyle='-')

# Also plot circular level curves on the xy-plane (z=0)
for lvl in levels[:3]:
    circ_theta = np.linspace(0, 2*np.pi, 100)
    circ_r = np.sqrt(lvl)
    circ_x = circ_r * np.cos(circ_theta)
    circ_y = circ_r * np.sin(circ_theta)
    circ_z = np.zeros_like(circ_x)
    ax.plot(circ_x, circ_y, circ_z, color='gray', linewidth=1.0, linestyle=':')

# Draw coordinate axes lines through origin
ax.plot([-2.5, 2.5], [0, 0], [0, 0], color='black', linewidth=1.2, linestyle='--')
ax.plot([0, 0], [-2.5, 2.5], [0, 0], color='black', linewidth=1.2, linestyle='--')
ax.plot([0, 0], [0, 0], [0, 5.2], color='black', linewidth=1.5)

# Mark the minimum point (0, 0, 0)
ax.scatter([0], [0], [0], color='red', s=150, zorder=10, edgecolor='black', label=r'Minimum $\mathbf{x}^* = \mathbf{0}$')
ax.text(0.2, 0.2, 0.1, r'$\mathbf{x}^* = \mathbf{0}$ (Minimum)', color='darkred', fontsize=12, fontweight='bold')

# Styling
ax.set_xlabel(r'$x_1$', fontsize=13, labelpad=8)
ax.set_ylabel(r'$x_2$', fontsize=13, labelpad=8)
ax.set_zlabel(r'$f(x) = x_1^2 + x_2^2$', fontsize=12, labelpad=8)
ax.set_title(r'Circular Paraboloid: $f(\mathbf{x}) = \mathbf{x}^T Q \mathbf{x}$ with $Q = I$', fontsize=14, fontweight='bold', pad=15)

ax.view_init(elev=26, azim=215)

os.makedirs('images', exist_ok=True)
plt.tight_layout()
plt.savefig('images/paraboloid_q_identity.png', dpi=300)
print('Successfully saved images/paraboloid_q_identity.png')
