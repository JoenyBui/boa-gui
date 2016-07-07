"""
**acceleration**

unity value = m/s^2

=================== ======================= =============== =============== ==========================
Base value	        (Gal, or cm/s2)	        (ft/s2)	        (m/s2)	        (Standard gravity, g0)
=================== ======================= =============== =============== ==========================
1 Gal, or cm/s2	    1	                    0.0328084	    0.01	        0.00101972
1 ft/s2	            30.4800	                1	            0.304800	    0.0310810
1 m/s2	            100	                    3.28084	        1	            0.101972
1 g0	            980.665	                32.1740	        9.80665	        1
=================== ======================= =============== =============== ==========================

"""
from . import Unit, UNIT_ACCELERATION
__author__ = 'jbui'

FACTOR_ACCELERATION_GAL = None
FACTOR_ACCELERATION_FT_S2 = None
FACTOR_ACCELERATION_M_S2 = None
FACTOR_ACCELERATION_GRAVITY = None


class AccelerationUnit(Unit):

    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_ACCELERATION
