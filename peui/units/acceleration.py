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
from . import Unit, UNIT_ACCELERATION_KEY

__author__ = 'jbui'

FACTOR_ACCELERATION_M_S2 = 1.0
FACTOR_ACCELERATION_KM_S2 = 0.001
FACTOR_ACCELERATION_MM_S2 = 1000.0
FACTOR_ACCELERATION_GAL = 100.0
FACTOR_MILE_S2 = 0.0006214
FACTOR_ACCELERATION_FT_S2 = 3.281
FACTOR_INCH_S2 = 39.370
FACTOR_ACCELERATION_GRAVITY = 100.0

ACCELERATION_KEY = {
    'm/s2': FACTOR_ACCELERATION_M_S2,
    'm/s^2': FACTOR_ACCELERATION_M_S2,
    'km/s2': FACTOR_ACCELERATION_KM_S2,
    'km/s^2': FACTOR_ACCELERATION_KM_S2,
    'mm/s2': FACTOR_ACCELERATION_MM_S2,
    'mm/s^2': FACTOR_ACCELERATION_MM_S2,
    'ft/s2': FACTOR_ACCELERATION_FT_S2,
    'ft/s^2': FACTOR_ACCELERATION_FT_S2,
    'cm/s^2': FACTOR_ACCELERATION_GAL,
    'cm/s2': FACTOR_ACCELERATION_GAL,
    # 'gal': FACTOR_ACCELERATION_GAL
}


DEFAULT_ACCELERATION_LIST = [
    'm/s2',
    'ft/s2',
    'cm/s2'
]

DEFAULT_IMPERIAL__LIST = [
    'ft/s2',
]

DEFAULT_METRIC_LIST = [
    'm/s^2',
    'cm/s^2'
]


def get_acceleration_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = ACCELERATION_KEY.get(origin)
    destination_factor = ACCELERATION_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class AccelerationUnit(Unit):
    """
    **Acceleration Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_ACCELERATION_KEY
        self.table = ACCELERATION_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL__LIST

    # def get_conversion_factor(self, origin, destination):
    #     return get_acceleration_conversion_factor(origin, destination)
