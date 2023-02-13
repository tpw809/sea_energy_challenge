import numpy as np
import matplotlib.pyplot as plt

# constants:

# [m/s^2], acceleration due to gravity:
g = 9.8

# [kg/m^3], density of sea water:
rho_sw = 1025.0


class SparBuoy:
    def __init__(self, 
                 name='defaultSparBuoy',
                 m_pl=1.0,
                 m_bal=4.0,
                 freeboard=1.0,
                 draft=2.0,
                 diam=0.25) -> None:
        self.name = name

        # [kg], payload mass
        self.m_pl = m_pl 

        # [kg], ballast mass
        self.m_bal = m_bal

        # [m], freeboard
        self.freeboard = freeboard

        # [m], draft
        self.draft = draft

        # [m], diameter:
        self.diam = diam

    @property
    def k_fd(self):
        """
        ratio of freeboard to draft
        """
        return self.freeboard / self.draft

    @property
    def k_bf(self):
        """
        ratio of draft to freeboard
        """
        return self.draft / self.freeboard

    @property
    def v_sub(self):
        """
        [m^3], submerged volume of the spar cylinder
        """
        return self.draft * np.pi * (self.diam / 2.0)**2

    @property
    def m_tot(self):
        """
        total mass (payload + ballast)
        """
        return self.m_bal + self.m_pl
    
    @property
    def m_disp(self):
        """
        [kg], mass of displaced water of submerged volume
        """
        return self.v_sub * rho_sw


if __name__ == "__main__":
    sb1 = SparBuoy()
    print(f"sb1.m_tot = {sb1.m_tot} [kg]")
    print(f"sb1.v_sub = {sb1.v_sub} [m^3]")
    print(f"sb1.m_disp = {sb1.m_disp} [kg]")
