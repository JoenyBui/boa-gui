"""
**Force**

unity value = newton

"""
from . import Unit, UNIT_FORCE_KEY

__author__ = 'jbui'

FACTOR_FORCE_NEWTON = 1
FACTOR_FORCE_KILONEWTON = 1000
FACTOR_FORCE_POUND = 4.44822163
FACTOR_FORCE_TON = 8896.4432565
FACTOR_FORCE_KILOTON = 8896443.2565
FACTOR_FORCE_KIP = 4448.2216

FORCE_KEY = {
    'lb': FACTOR_FORCE_POUND,
    'lbs': FACTOR_FORCE_POUND,
    'kip': FACTOR_FORCE_KIP,
    'ton': FACTOR_FORCE_TON,
    'kiloton': FACTOR_FORCE_KILOTON,
    'N': FACTOR_FORCE_NEWTON,
    'kN': FACTOR_FORCE_KILONEWTON
}


DEFAULT_FORCE_LIST = [
    'ton',
    'kip',
    'kiloton'
    'N',
    'kN'
]

DEFAULT_IMPERIAL_LIST = [
    'lbs',
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

    return origin_factor / destination_factor


class ForceUnit(Unit):
    """
    ** Force Unit **

    """

    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_FORCE_KEY
        self.table = FORCE_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

    def get_conversion_factor(self, origin, destination):
        return get_force_conversion_factor(origin, destination)
