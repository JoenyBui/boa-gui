"""
**kilogram""

unit value = kilogram

"""
from . import Unit, UNIT_TNT_KEY

__author__ = 'Joeny'


FACTOR_TNT_GRAM = 1.0
FACTOR_TNT_KILOGRAM = 0.001
FACTOR_TNT_TON = 0.000001102
FACTOR_TNT_KILOTON = 0.000000001102
FACTOR_TNT_POUND = 0.00220462

TNT_KEY = {
    'ton': FACTOR_TNT_TON,
    'kiloton': FACTOR_TNT_KILOTON,
    'kilogram': FACTOR_TNT_KILOGRAM,
    'kg': FACTOR_TNT_KILOGRAM,
    'lb': FACTOR_TNT_POUND,
    'lbs': FACTOR_TNT_POUND
}


DEFAULT_TNT_LIST = [
    'ton',
    'kiloton',
    'kilogram'
]


DEFAULT_IMPERIAL_LIST = [
    'ton',
    'kiloton',
    'lbs'
]

DEFAULT_METRIC_LIST = [
    'kg',
]


def get_tnt_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = TNT_KEY.get(origin)
    destination_factor = TNT_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class TntUnit(Unit):
    """
    **TNT Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_TNT_KEY
        self.table = TNT_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST
