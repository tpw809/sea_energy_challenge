import numpy as np
import matplotlib.pyplot as plt

# Constants:

# [kg/L], density of sea-water
rho_sw = 1.025

# convert Liters to meters cubed
L_to_m3 = 0.001

# [m/s^2], acceleration due to gravity
grav = 9.8

# Depths and Heights:

# [m], total height of the buoy (top to bottom)
h_total = 5.0

# [m], submerged height of the buoy (water line to bottom)
h_submerged = 3.0

# [m], freeboard height (water line to top)
h_freeboard = h_total - h_submerged 

# Mass Properties:

# [kg], mass of the payload (top of the spar buoy)
m_payload = 100.0

# [-], ballast multipier
ballast_multiplier = 2.0

# [kg], mass of the ballast weight (bottom of the spar)
m_ballast = ballast_multiplier * m_payload

# [kg], total mass
m_total = m_payload + m_ballast
print(f"m_total = {m_total} [kg]")

# Cylinder Geometry:

# [m], cylinder diameter
diam = 0.5

# [m], cylinder radius
radius = diam / 2.0

# [m^3], submerged (floatation) volume
v_float = np.pi * radius**2 * h_submerged


# Balance of Forces:

# [N], force of gravity (weight)
F_grav = m_total * grav
print(f"F_grav = {F_grav} [N]")

# [N], bouyant force (weight of displaced water)
F_buoy = grav * v_float / L_to_m3 * rho_sw
print(f"F_buoy = {F_buoy} [N]")


# water pressure
pressure = rho_sw * grav * h_submerged


# Design Criteria:
# -buoy must float
# -center of mass must be below the center of buoyancy
# -payload freeboard height
# -wave height ratio to total height?



plt.figure()
plt.plot([0.0], [0.0], 'r+')
plt.plot([0.0], [h_freeboard], 'ko')
plt.plot([0.0], [-h_submerged], 'ko')

plt.plot([-radius, radius], [h_freeboard, h_freeboard], 'k')
plt.plot([-radius, radius], [-h_submerged, -h_submerged], 'k')
plt.plot([-radius, -radius], [-h_submerged, h_freeboard], 'k')
plt.plot([radius, radius], [-h_submerged, h_freeboard], 'k')

plt.plot([-radius - 1.0, radius + 1.0], [0.0, 0.0], 'b')

plt.title('Spar Buoy')
plt.ylabel('depth [m]')
plt.grid()
plt.axis('equal')

plt.show()