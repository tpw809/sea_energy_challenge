import numpy as np


in_to_mm = 25.4
mm_to_m = 1.0 / 1000.0
mm3_to_m3 = 1.0 / 1000.0 / 1000.0 / 1000.0
kg_to_lb = 2.20462

# [kg/m^3], density of concrete:
rho_conrete = 2400.0

# [mm], concrete puck diameter:
D = 3.0 * in_to_mm

# [mm], concrete puck radius:
R = D / 2.0

# [mm], conrete puck height:
H = D

# [mm^3], volume:
V = H * np.pi * R**2
print(f"volume = {V} [mm^3]")

# [kg], mass:
m_puck = rho_conrete * V * mm3_to_m3
print(f"mass = {m_puck} [kg]")
print(f"mass = {m_puck * kg_to_lb} [lb]")


# Solid Cylinder Mass Properties:

# [kg-m^2], moment of inertia about z axis (along axis of revolution)
Izz = 0.5 * m_puck * R**2
print(f"Izz = {Izz} [kg-m^2]")

# [kg-m^2], moment of inertia about x and y axis
Ixx = 1.0 / 12.0 * m_puck * (3.0 * R**2 + H**2)
print(f"Ixx = {Ixx} [kg-m^2]")

Iyy = Ixx
print(f"Iyy = {Iyy} [kg-m^2]")
