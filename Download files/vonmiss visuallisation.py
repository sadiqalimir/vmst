import numpy as np
import matplotlib.pyplot as plt

def von_mises(sigma_x, sigma_y, tau_xy):
    """Calculate the von Mises stress at a given point"""
    return np.sqrt(sigma_x**2 - sigma_x*sigma_y + sigma_y**2 + 3*tau_xy**2)

def is_failure(sigma_x, sigma_y, tau_xy, yield_strength):
    """Check if the material will fail under the given load"""
    von_mises_stress = von_mises(sigma_x, sigma_y, tau_xy)
    return von_mises_stress >= yield_strength

# Ask the user for input parameters
sigma_x_min = float(input("Enter minimum value of Sigma_x: "))
sigma_x_max = float(input("Enter maximum value of Sigma_x: "))
sigma_y_min = float(input("Enter minimum value of Sigma_y: "))
sigma_y_max = float(input("Enter maximum value of Sigma_y: "))
tau_xy_min = float(input("Enter minimum value of Tau_xy: "))
tau_xy_max = float(input("Enter maximum value of Tau_xy: "))
yield_strength = float(input("Enter the yield strength of the material: "))

# Define the stress components at each point
sigma_x = np.linspace(sigma_x_min, sigma_x_max, 101)
sigma_y = np.linspace(sigma_y_min, sigma_y_max, 101)
tau_xy = np.linspace(tau_xy_min, tau_xy_max, 101)

# Create a grid of coordinates for each point
X, Y, Z = np.meshgrid(sigma_x, sigma_y, tau_xy, indexing='ij')

# Calculate the von Mises stress at each point
VM_stress = von_mises(X, Y, Z)

# Check if the material will fail at each point
failure = is_failure(X, Y, Z, yield_strength)

# Create the first 3D plot of the von Mises stress
fig1 = plt.figure(figsize=(8, 8))
ax1 = fig1.add_subplot(projection='3d')

ax1.set_title('Von Mises Stress')

ax1.set_xlabel('Sigma_x')
ax1.set_ylabel('Sigma_y')
ax1.set_zlabel('Tau_xy')

# Create the first plot
sc1 = ax1.scatter(X, Y, Z, c=VM_stress, cmap='jet')

# Add a colorbar
cbar1 = plt.colorbar(sc1)
cbar1.set_label('Von Mises Stress')

# Create the second 2D plot of the stress-strain curve
fig2, ax2 = plt.subplots(figsize=(8, 6))

ax2.set_title('Stress-Strain Curve')

ax2.set_xlabel('Strain')
ax2.set_ylabel('Stress')

# Calculate and plot the stress-strain curve
strain = np.linspace(0, 1, 101)
stress = yield_strength * strain
ax2.plot(strain, stress, 'r-', linewidth=2)

# Check if the material will fail under the given load
if np.any(failure):
    print("The material will fail under the given load.")
else:
    print("The material will not fail under the given load.")

# Show the plots
plt.show()

