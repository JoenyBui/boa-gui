"""
**Linear Pressure Density**

Force Derived Unit

unity_value = kg/m

"""
from . import Unit, UNIT_LINEAR_PRESSURE

__author__ = 'Joeny'

FACTOR_LINEAR_PRESSURE_N_M = 1.0
FACTOR_LINEAR_PRESSURE_N_CM = 0.01
FACTOR_LINEAR_PRESSURE_N_MM = 0.001
FACTOR_LINEAR_PRESSURE_KN_M = 0.001
FACTOR_LINEAR_PRESSURE_KG_M = 0.1019716212978
FACTOR_LINEAR_PRESSURE_PLF = 0.068521763
FACTOR_LINEAR_PRESSURE_KLF = 0.000068521
FACTOR_LINEAR_PRESSURE_PLI = 0.005710143

LINEAR_PRESSURE_KEY = {
    'N/m': FACTOR_LINEAR_PRESSURE_N_M,
    'N/cm': FACTOR_LINEAR_PRESSURE_N_CM,
    'N/mm': FACTOR_LINEAR_PRESSURE_N_MM,
    'KN/m': FACTOR_LINEAR_PRESSURE_KN_M,
    'lb/ft': FACTOR_LINEAR_PRESSURE_PLF,
    'plf': FACTOR_LINEAR_PRESSURE_PLF,
    'lb/in': FACTOR_LINEAR_PRESSURE_PLI,
    'pli': FACTOR_LINEAR_PRESSURE_PLI,
    'kip/ft': FACTOR_LINEAR_PRESSURE_KLF,
    'klf': FACTOR_LINEAR_PRESSURE_KLF
}

DEFAULT_LINEAR_PRESSURE_LIST = {
    'plf': FACTOR_LINEAR_PRESSURE_PLF,
    'klf': FACTOR_LINEAR_PRESSURE_KLF,
}

DEFAULT_IMPERIAL_LIST = [
    'plf',
    'lb/in',
    'klf'
]

DEFAULT_METRIC_LIST = [
    'kg/m',
    'N/mm'
]


def get_linear_pressure_conversion_factor(origin, destination):
    """
    Get the length conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = LINEAR_PRESSURE_KEY.get(origin)
    destination_factor = LINEAR_PRESSURE_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class LinearPressureUnit(Unit):
    """
    **Linear Pressure Density Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_LINEAR_PRESSURE
        self.table = LINEAR_PRESSURE_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST
