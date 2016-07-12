"""
**Linear Mass Density**

Mass Derived Unit

"""
from . import Unit, UNIT_LINEAR_DENSITY

__author__ = 'jbui'


FACTOR_LINEAR_DENSITY_KN_LF = 1.0
FACTOR_LINEAR_DENSITY_PLF = 1.0
FACTOR_LINEAR_DENSITY_KLF = 1.0

LINEAR_DENSITY_KEY = {
    'plf': FACTOR_LINEAR_DENSITY_PLF,
    'lb/ft': FACTOR_LINEAR_DENSITY_PLF,
    'klf': FACTOR_LINEAR_DENSITY_KLF
}

DEFAULT_LINEAR_DENSITY_LIST = {
    'plf': FACTOR_LINEAR_DENSITY_PLF,
    'klf': FACTOR_LINEAR_DENSITY_KLF,
}

DEFAULT_IMPERIAL_LIST = [
    'plf',
    'klf'
]

DEFAULT_METRIC_LIST = [
    'm4',
    'mm4'
]


def get_linear_density_conversion_factor(origin, destination):
    """
    Get the length conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = LINEAR_DENSITY_KEY.get(origin)
    destination_factor = LINEAR_DENSITY_KEY.get(destination)

    return origin_factor / destination_factor


class LinearDensityUnit(Unit):
    """
    **Linear Density Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_LINEAR_DENSITY
        self.table = LINEAR_DENSITY_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST

    def get_conversion_factor(self, origin, destination):
        return get_linear_density_conversion_factor(origin, destination)
