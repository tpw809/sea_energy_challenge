import numpy as np
import matplotlib.pyplot as plt

# [m/s^2], acceleration due to gravity:
g = 9.8

# [kg/m^3], density of sea water:
rho_sw = 1025.0

# [-], freeboard to draft ratio (freeboard / draft)
k_fd = 0.5

# [kg], mass of the payload (top of the spar buoy)
m_payload = 1.0

# [m], distance above the water the payload cg is located:
freeboard = 1.0

# [m], depth below the water the ballast cg is located:
draft = freeboard / k_fd

# [-], mulitplier on ballast mass to guarantee stability:
stability_margin = 2.0

# [m], distance from ballast cg to center of buoyancy:
d_bal = draft / 2.0

# [m], distance from center of buoyancy to payload cg:
d_pl = freeboard + (draft / 2.0)

# stability margin = m_ballast / (m_payload * (d_pl / d_bal))
# [kg], ballast mass required to satisfy stability margin:
m_ballast = stability_margin * m_payload * (d_pl / d_bal)
print(f"m_ballast = {m_ballast} [kg]")

# [m], total length of the cylinder:
l_tot = freeboard + draft

# [kg], total mass:
m_tot = m_payload + m_ballast

# [m^3], water displacement necessary to float ballast and payload:
v_req = m_tot / rho_sw

# [m], required cylinder diameter to float payload and ballast:
# v = l * A = l * pi * r^2 = l * pi * (d/2)^2
diam = 2.0 * np.sqrt(v_req / (draft * np.pi))
print(f"cylinder diameter requrired = {diam} [m]")

# [-], cylinder aspect ratio (L/D)
ar_cyl = l_tot / diam
print(f"cylinder aspect ratio = {ar_cyl}")
