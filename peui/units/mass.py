
__author__ = 'jbui'

# UNITY_VALUE = GRAM
FACTOR_PRESSURE_GRAM = 1.0
FACTOR_PRESSURE_KILOGRAM = 0.001
FACTOR_PRESSURE_POUND_MASS = 0.0022046226218

ID_NAME_MASS_GRAM = ('g', 'gram')
ID_NAME_MASS_KILOGRAM = ('kg', 'kilogram')
ID_NAME_POUND_MASS = ('lbm', 'pound')

MASS_KEY = {
    'g': FACTOR_PRESSURE_GRAM,
    'gram': FACTOR_PRESSURE_GRAM,
    'kg': FACTOR_PRESSURE_KILOGRAM,
    'kilogram': FACTOR_PRESSURE_KILOGRAM,
    'lbm': FACTOR_PRESSURE_POUND_MASS,
    'pound': FACTOR_PRESSURE_POUND_MASS
}


DEFAULT_MASS_LIST = [
    'g',
    'kg',
    'lbm'
]

DEFAULT_IMPERIAL_LIST = [
    'lbm'
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

    return destination_factor / origin_factor
