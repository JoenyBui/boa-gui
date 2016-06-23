__author__ = 'jbui'

FACTOR_TNT_TON = 1
FACTOR_TNT_KILOTON = 0.001

TNT_KEY = {
    'ton': FACTOR_TNT_TON,
    'kiloton': FACTOR_TNT_KILOTON
}


DEFAULT_TNT_LIST = [
    'ton',
    'kiloton'
]


def get_tnt_conversion_factor(origin, destination):
    origin_factor = TNT_KEY.get(origin)
    destination_factor = TNT_KEY.get(destination)

    return destination_factor / origin_factor
