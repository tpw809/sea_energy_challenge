import numpy as np
import matplotlib.pyplot as plt

# conversion factors:
in_to_mm = 25.4
mm_to_m = 1.0 / 1000.0
mm2_to_m2 = 1.0 / 1000.0 / 1000.0
mm3_to_m3 = 1.0 / 1000.0 / 1000.0 / 1000.0

# [kg/m^3], density of PVC
rho_pvc = 1300.0

# [kg/m^3], density of sea water:
rho_sw = 1025.0

# [kg/m^3], density of concrete:
rho_conrete = 2400.0

# [mm], spar outer diameter
do = 3.5 * in_to_mm

# [mm], spar inner diameter
di = 3.0 * in_to_mm

# [mm], spar outer diameter
ro = do / 2.0

# [mm], spar inner diameter
ri = di / 2.0

# [mm], spar height
h = 35.0 * in_to_mm
print(f"spar height = {h}")

# [mm^2], spar solid cross section area
a_spar = np.pi * (ro**2 - ri**2)

# [mm^3], volume of the solid spar
v_spar = a_spar * h

# [kg], mass of the solid spar
m_spar = v_spar * mm3_to_m3 * rho_pvc
print(f"spar mass = {m_spar} [kg]")

# [kg], mass of 3x3 in concrete puck
m_puck = 0.834

# [mm^2], buoyancy area
a_buoy = np.pi * ro**2

# [m^3], volume of displacement water need to float
v_water = (3.0 * m_puck + m_spar) / rho_sw

# [mm], height of waterline, no ballast
h_wl = (v_water / mm3_to_m3) / a_buoy
print(f"h_wl = {h_wl} [mm]")
