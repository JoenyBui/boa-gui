"""
**Force**

unity value = newton

"""
from . import Unit, UNIT_FORCE_KEY

__author__ = 'jbui'

FACTOR_FORCE_NEWTON = 1
FACTOR_FORCE_KILONEWTON = 0.001
FACTOR_FORCE_POUND = 0.1
FACTOR_FORCE_TON = 1.0
FACTOR_FORCE_KILOTON = 1.0
FACTOR_FORCE_KIP = 1000

FORCE_KEY = {
    'lb': FACTOR_FORCE_POUND,
    'kip': FACTOR_FORCE_KIP,
    'ton': FACTOR_FORCE_TON,
    'kiloton': FACTOR_FORCE_KILOTON,
    'N': FACTOR_FORCE_NEWTON,
    'kN': FACTOR_FORCE_KILONEWTON
}


DEFAULT_FORCE_LIST = [
    'ton',
    'kiloton'
]

DEFAULT_IMPERIAL_LIST = [
    'lb',
    'ton',
    'kiloton'
]

DEFAULT_METRIC_LIST = [
    'N',
    'kN'
]


def get_force_conversion_factor(origin, destination):
    """
    Return a force conversion factor.

    :param origin: original unit
    :param destination: return destination
    :return:
    """
    origin_factor = FORCE_KEY.get(origin)
    destination_factor = FORCE_KEY.get(destination)

    return destination_factor / origin_factor


class ForceUnit(Unit):
    """
    ** Force Unit **

    """

    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_FORCE_KEY
        self.table = FORCE_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

    def get_conversion_factor(self, origin, destination):
        return get_force_conversion_factor(origin, destination)
