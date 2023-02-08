import numpy as np
import matplotlib.pyplot as plt

# [m/s^2], acceleration due to gravity:
g = 9.8

# [kg/m^3], density of sea water:
rho_sw = 1025.0

# [m], spar buoy cylinder diameter:
diam = 0.5

# [m], draft depth (height):
h_draft = 5.0

# [m^3], submerged volume:
v_sub = h_draft * np.pi * (diam / 2.0)**2

# [kg], total floated mass:
m_tot = v_sub * rho_sw
print(f"total floated mass = {m_tot} [kg]")

# natural frequency,  omega_n
# omega_n = sqrt(k/m)
# k = stiffness
# m = mass

# [N/m], effective floation stiffness:
k_float = g * rho_sw * np.pi * (diam / 2.0)**2
print(f"floatation stiffness = {k_float} [N/m]")

# [], buoyancy natural frequency:
omega_n = np.sqrt(k_float / m_tot)
print(f"omega_n = {omega_n} Hz")

omega_n = np.sqrt(g / h_draft)
print(f"omega_n = {omega_n} Hz")


# Dynamic Model:
# y-direction only
# most significant waves are < 1 Hz
