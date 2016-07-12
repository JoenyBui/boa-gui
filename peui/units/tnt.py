from . import Unit, UNIT_TNT_KEY

__author__ = 'jbui'

FACTOR_TNT_TON = 1
FACTOR_TNT_KILOTON = 0.001
FACTOR_PRESSURE_POUND = .0005

TNT_KEY = {
    'ton': FACTOR_TNT_TON,
    'kiloton': FACTOR_TNT_KILOTON,
    'lb': FACTOR_PRESSURE_POUND,
    'pound': FACTOR_PRESSURE_POUND
}


DEFAULT_TNT_LIST = [
    'ton',
    'kiloton',
    'lb'
]


def get_tnt_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = TNT_KEY.get(origin)
    destination_factor = TNT_KEY.get(destination)

    return destination_factor / origin_factor


class TntUnit(Unit):

    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_TNT_KEY
        self.table = TNT_KEY

        self.imperial_list = DEFAULT_TNT_LIST

    def get_conversion_factor(self, origin, destination):
        return get_tnt_conversion_factor(origin, destination)
