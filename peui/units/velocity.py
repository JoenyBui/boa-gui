"""
**velocity**

unity value = 'm/s'

Conversions between common units of speed

=========== =========== =========== =========== =========== ============
            m/s	        km/h	    mph	        knot	    ft/s
=========== =========== =========== =========== =========== ============
1 m/s =	    1	        3.6	        2.236936	1.943844	3.280840
1 km/h =	0.277778	1	        0.621371	0.539957	0.911344
1 mph =	    0.44704	    1.609344	1	        0.868976	1.466667
1 knot =	0.514444	1.852	    1.150779	1	        1.687810
1 ft/s =	0.3048	    1.09728	    0.681818	0.592484	1
=========== =========== =========== =========== =========== ============

"""
from . import Unit, UNIT_TIME_KEY

__author__ = 'jbui'

FACTOR_VELOCITY_M_S = 1.0
FACTOR_VELOCITY_KM_H = None
FACTOR_VELOCITY_FT_S = None
FACTOR_VELOCITY_MM_MS = None

VELOCITY_KEY = {
}

class VelocityUnit(Unit):

    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_TIME_KEY
