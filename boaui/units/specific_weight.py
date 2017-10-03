"""
**Specific Weight**


"""

from . import Unit, UNIT_SPECIFIC_WEIGHT

__author__ = 'Joeny'

FACTOR_PA_M = 1.0
FACTOR_KPA_MM = 0.000001
FACTOR_PSI_IN = 0.00000368396

SPECIFIC_WEIGHT_KEY = {
    'kPa/mm': FACTOR_KPA_MM,
    'psi/in': FACTOR_PSI_IN
}

DEFAULT_SPECIFIC_WEIGHT_LIST = {
    'Pa/m': FACTOR_PA_M,
    'kPa/mm': FACTOR_KPA_MM,
    'psi/in': FACTOR_PSI_IN,
}

DEFAULT_IMPERIAL_LIST = [
    'psi/in'
]

DEFAULT_METRIC_LIST = [
    'kPa/mm'
]


def get_specific_weight_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = SPECIFIC_WEIGHT_KEY.get(origin)
    destination_factor = SPECIFIC_WEIGHT_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class SpecificWeightUnit(Unit):
    """
    Specific Weight

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_SPECIFIC_WEIGHT
        self.table = SPECIFIC_WEIGHT_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

