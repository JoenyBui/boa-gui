"""
**Linear Mass Density**

Mass Derived Unit

"""
from . import Unit, UNIT_LINEAR_DENSITY

__author__ = 'jbui'


FACTOR_LINEAR_DENSITY_G_M = 1.0
FACTOR_LINEAR_DENSITY_KG_M = 0.001
FACTOR_LINEAR_DENSITY_PLF = 0.000671969

LINEAR_DENSITY_KEY = {
    'g/m': FACTOR_LINEAR_DENSITY_G_M,
    'kg/m': FACTOR_LINEAR_DENSITY_KG_M,
    'lbm/ft': FACTOR_LINEAR_DENSITY_PLF,
    'plf': FACTOR_LINEAR_DENSITY_PLF,
    'lb/ft': FACTOR_LINEAR_DENSITY_PLF
}

DEFAULT_LINEAR_DENSITY_LIST = {
    'plf': FACTOR_LINEAR_DENSITY_PLF,
}

DEFAULT_IMPERIAL_LIST = [
    'plf'
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
    origin_factor = LINEAR_DENSITY_KEY.get(origin)
    destination_factor = LINEAR_DENSITY_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


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
