"""
**Specific Weight**


"""

from . import Unit, UNIT_SPECIFIC_WEIGHT

__author__ = 'jbui'

FACTOR_KPA_MM = 1.0
FACTOR_PSI_IN = 1.0

SPECIFIC_WEIGHT_KEY = {
    'kPa/mm': FACTOR_KPA_MM,
    'psi/in': FACTOR_PSI_IN
}

DEFAULT_LINEAR_PRESSURE_LIST = {
    'kPa/mm': FACTOR_KPA_MM,
    'psi/in': FACTOR_PSI_IN,
}

DEFAULT_IMPERIAL_LIST = [
    'psi/in'
]

DEFAULT_METRIC_LIST = [
    'kPa/mm'
]


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

