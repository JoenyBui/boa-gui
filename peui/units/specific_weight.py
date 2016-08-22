"""
**Specific Weight**


"""

from . import Unit, UNIT_SPECIFIC_WEIGHT

__author__ = 'jbui'

FACTOR_KPA_MM = 1.0
FACTOR_PSI_IN = 0.271447

SPECIFIC_WEIGHT_KEY = {
    'kPa/mm': FACTOR_KPA_MM,
    'psi/in': FACTOR_PSI_IN
}

DEFAULT_SPECIFIC_WEIGHT_LIST = {
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

    return origin_factor / destination_factor


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
