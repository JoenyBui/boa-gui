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
from . import Unit, UNIT_VELOCITY_KEY

__author__ = 'jbui'

FACTOR_VELOCITY_M_S = 1.0
FACTOR_VELOCITY_KM_H = 0.277778
FACTOR_VELOCITY_FT_S = 0.3048
FACTOR_VELOCITY_MM_MS = 1.0

VELOCITY_KEY = {
    'm/s': FACTOR_VELOCITY_M_S,
    'mm/ms': FACTOR_VELOCITY_MM_MS,
    'ft/s': FACTOR_VELOCITY_FT_S,
    'km/h': FACTOR_VELOCITY_KM_H
}


DEFAULT_VELOCITY_LIST = [
    'm/s',
    'mm/ms',
    'ft/s',
    'km/h'
]

DEFAULT_IMPERIAL_LIST = [
    'ft/s',
]

DEFAULT_METRIC_LIST = [
    'm/s',
    'mm/ms',
    'km/h'
]


def get_velocity_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = VELOCITY_KEY.get(origin)
    destination_factor = VELOCITY_KEY.get(destination)

    return origin_factor / destination_factor


class VelocityUnit(Unit):
    """
    **Velocity**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_VELOCITY_KEY
        self.table = VELOCITY_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST
