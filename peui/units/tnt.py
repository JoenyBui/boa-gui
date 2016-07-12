"""
**kilogram""

unit value = kilogram

"""
from . import Unit, UNIT_TNT_KEY

__author__ = 'jbui'

FACTOR_TNT_KILOGRAM = 1
FACTOR_TNT_TON = 907.185819
FACTOR_TNT_KILOTON = 907185.819
FACTOR_PRESSURE_POUND = 0.453592

TNT_KEY = {
    'ton': FACTOR_TNT_TON,
    'kiloton': FACTOR_TNT_KILOTON,
    'kilogram': FACTOR_TNT_KILOGRAM
}


DEFAULT_TNT_LIST = [
    'ton',
    'kiloton',
    'kilogram'
]


DEFAULT_IMPERIAL_LIST = [
    'ton',
    'kiloton'
]

DEFAULT_METRIC_LIST = [
    'kilogram',
]


def get_tnt_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = TNT_KEY.get(origin)
    destination_factor = TNT_KEY.get(destination)

    return origin_factor / destination_factor


class TntUnit(Unit):
    """
    **TNT Unit**

    """
    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_TNT_KEY
        self.table = TNT_KEY

        self.imperial_list = DEFAULT_TNT_LIST

    def get_conversion_factor(self, origin, destination):
        return get_tnt_conversion_factor(origin, destination)
