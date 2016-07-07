"""
**Linear Pressure Density**

"""
from . import Unit, UNIT_LINEAR_PRESSURE

__author__ = 'jbui'

FACTOR_LINEAR_PRESSURE_KG_M = 1.0
FACTOR_LINEAR_PRESSURE_KN_LF = 1.0
FACTOR_LINEAR_PRESSURE_PLF = 1.0
FACTOR_LINEAR_PRESSURE_KLF = 1.0
FACTOR_LINEAR_PRESSURE_PLI = 1.0

LINEAR_PRESSURE_KEY = {
    'kg/m': FACTOR_LINEAR_PRESSURE_KG_M,
    'plf': FACTOR_LINEAR_PRESSURE_PLF,
    'lb/ft': FACTOR_LINEAR_PRESSURE_PLF,
    'lb/in': FACTOR_LINEAR_PRESSURE_PLI,
    'klf': FACTOR_LINEAR_PRESSURE_KLF
}

DEFAULT_LINEAR_PRESSURE_LIST = {
    'plf': FACTOR_LINEAR_PRESSURE_PLF,
    'klf': FACTOR_LINEAR_PRESSURE_KLF,
}

DEFAULT_IMPERIAL_LIST = [
    'plf',
    'lb/in'
    'klf'
]

DEFAULT_METRIC_LIST = [
    'kg/m'
]


def get_linear_density_conversion_factor(origin, destination):
    """
    Get the length conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = LINEAR_PRESSURE_KEY.get(origin)
    destination_factor = LINEAR_PRESSURE_KEY.get(destination)

    return origin_factor / destination_factor


class LinearPressureUnit(Unit):
    """
    **Linear Pressure Density Unit**

    """
    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_LINEAR_PRESSURE
        self.table = LINEAR_PRESSURE_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST

    def get_conversion_factor(self, origin, destination):
        return get_linear_density_conversion_factor(origin, destination)
