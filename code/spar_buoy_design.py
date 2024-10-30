import numpy as np
import matplotlib.pyplot as plt

# Constants:

# [kg/L], density of sea-water
rho_sw = 1.025

# [kg/m^3], density of concrete
rho_concrete = 2000.0

# [kg/m^3], iron density
rho_iron = 7800.0

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


# [N/m^2] = [Pa] water pressure at max depth
max_pressure = (rho_sw / L_to_m3) * grav * h_submerged
print(f"max_pressure = {max_pressure} [Pa]")

# Design Criteria:
# -buoy must float
# -center of mass must be below the center of buoyancy
# -payload freeboard height
# -wave height ratio to total height?



# New Design Process:
print("\n\nNew Method:")

# float cylinder length to diameter ratio: (L/D)
ld_ratio = 10.0

# [kg], ballast mass:
m_ballast = 10.0

# assume waterline is halfway up cylinder
# with no payload mass:
# Find water volume equal to ballast mass:
# m_disp = v_float * (rho_sw / L_to_m3)
v_req = m_ballast / (rho_sw / L_to_m3)
print(f"float volume required (no payload) = {v_req} [m^3]")

# for submerged volume with no payload:
# L = 5*D = (ld_ratio/2.0)*D
# v = L * pi * D^2 / 4
# v = (5/4) * pi * D^3
diam = np.power((4.0 / (ld_ratio/2.0)) * v_req / np.pi, 1.0/3.0)
print(f"diam = {diam} [m]")

# total length of the float cylinder:
l_cyl = ld_ratio * diam
print(f"l_cycl = {l_cyl} [m]")

draft_max = l_cyl * 0.75
draft_min = l_cyl * 0.5
freeboard_max = 0.5 * l_cyl
freeboard_min = 0.25 * l_cyl

v_float_min = np.pi / 4.0 * diam**2 * draft_min
v_float_max = np.pi / 4.0 * diam**2 * draft_max
print(f"v_float_max = {v_float_max} [m^3]")
print(f"v_float_min = {v_float_min} [m^3]")

m_disp_max = (rho_sw / L_to_m3) * v_float_max
m_disp_min = (rho_sw / L_to_m3) * v_float_min
print(f"m_disp_max = {m_disp_max} [kg]")
print(f"m_disp_min = {m_disp_min} [kg]")


# stability margin = m_ballast / (m_payload * (d_pl / d_bal))
stab_marg = m_ballast / (m_ballast / 2.0 * ((freeboard_min + draft_max / 2.0) / (draft_max / 2.0)))
stab_marg = (m_ballast * (draft_max / 2.0)) / (m_ballast / 2.0 * (freeboard_min + draft_max / 2.0))
print(f"stab_marg = {stab_marg}")


# need to try and make freeboard and stability margin an input parameter...
# remove aspect ratio constraint, make cyl diameter and draft design variables

# requirements:
# payload mass
# stability margin
# freeboard

# design parameters:
# diameter
# draft
# ballast mass

print("\n\nNew Method 2:")

# [kg], payload mass (requirement)
m_pl = 2.5

# [-], stability margin (requirement)
stab_marg = 2.0

# [m], freeboard (requirement)
freeboard = 0.5

# [m], diameter of the float cylinder
diam = 0.1

# constraints:
# it has to float at the correct height:
# displacement mass = payload + ballast mass
# stability margin

m_ballast = 3.0 * m_pl

# m = rho * v
v_disp_min = (m_pl + m_ballast) / (rho_sw / L_to_m3)

# v = draft * pi * D^2 / 4 
draft_min = 4.0 * v_disp_min / (np.pi * diam**2)
print(f"draft_min = {draft_min} [m]")

stab_marg = (m_ballast * draft_min / 2.0) / (m_pl * (freeboard + draft_min / 2.0))
print(f"stab_marg = {stab_marg}")

ld_ratio = (freeboard + draft_min) / diam
print(f"ld_ratio = {ld_ratio}")


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