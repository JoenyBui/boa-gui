from . import Unit, UNIT_MASS_KEY

__author__ = 'jbui'

# UNITY_VALUE = GRAM
FACTOR_MASS_GRAM = 1.0
FACTOR_MASS_OUNCE = 0.035274
FACTOR_MASS_KILOGRAM = 0.001
FACTOR_MASS_MILLOGRAM = 1000
FACTOR_MASS_MICROGRAM = 1E6
FACTOR_MASS_POUND = 0.00220462
FACTOR_MASS_TON = 0.000001102

ID_NAME_MASS_GRAM = ('g', 'gram')
ID_NAME_MASS_KILOGRAM = ('kg', 'kilogram')
ID_NAME_POUND = ('lb', 'pound')

MASS_KEY = {
    'g': FACTOR_MASS_GRAM,
    'gram': FACTOR_MASS_GRAM,
    'kg': FACTOR_MASS_KILOGRAM,
    'kilogram': FACTOR_MASS_KILOGRAM,
    'lb': FACTOR_MASS_POUND,
    'pound': FACTOR_MASS_POUND,
    'ton': FACTOR_MASS_TON
}


DEFAULT_MASS_LIST = [
    'g',
    'kg',
    'lb'
]

DEFAULT_IMPERIAL_LIST = [
    'lb'
]

DEFAULT_METRIC_LIST = [
    'g',
    'kg'
]


def get_mass_conversion_factor(origin, destination):
    """
    Get mass conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = MASS_KEY.get(origin)
    destination_factor = MASS_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class MassUnit(Unit):
    """
    **Mass Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_MASS_KEY
        self.table = MASS_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST
