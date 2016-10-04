from . import Unit, UNIT_VOLUME_KEY

__author__ = 'jbui'

# UNITY_VALUE == 'm^3'
FACTOR_VOLUME_CUBIC_METER = 1.0
FACTOR_VOLUME_CUBIC_MM = 1E9
FACTOR_VOLUME_CUBIC_FT = 35.3147
FACTOR_VOLUME_CUBIC_IN = 61023.801579099
FACTOR_VOLUME_LITER = 1000
FACTOR_VOLUME_GALLON = 264.172
FACTOR_VOLUME_MILLILITER = 1E6

ID_NAME_VOLUME_M3 = ("m^3", "m3", "M3")
ID_NAME_VOLUME_MM3 = ("mm^3", "mm3", "MM3")
ID_NAME_VOLUME_FT3 = ("ft^3", "ft3", "FT3")
ID_NAME_VOLUME_IN3 = ("in^3", "in3", "IN3")

VOLUME_KEY = {
    'm^3': FACTOR_VOLUME_CUBIC_METER,
    'm3': FACTOR_VOLUME_CUBIC_METER,
    'mm^3': FACTOR_VOLUME_CUBIC_MM,
    'mm3': FACTOR_VOLUME_CUBIC_MM,
    'mm^4/mm': FACTOR_VOLUME_CUBIC_MM,
    'ft^3': FACTOR_VOLUME_CUBIC_FT,
    'ft3': FACTOR_VOLUME_CUBIC_FT,
    'in^3': FACTOR_VOLUME_CUBIC_IN,
    'in3': FACTOR_VOLUME_CUBIC_IN,
    'in^4/in': FACTOR_VOLUME_CUBIC_IN,
    'liter': FACTOR_VOLUME_LITER,
    'gallon': FACTOR_VOLUME_GALLON
}

DEFAULT_VOLUME_LIST = [
    'm3',
    'mm3',
    'ft3',
    'in3'
]

DEFAULT_IMPERIAL_LIST = [
    'ft^3',
    'in^3'
]

DEFAULT_METRIC_LIST = [
    'm^3',
    'mm^3'
]


def get_volume_conversion_factor(origin, destination):
    """
    Get the volume conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = VOLUME_KEY.get(origin)
    destination_factor = VOLUME_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class VolumeUnit(Unit):
    """
    **Volume Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_VOLUME_KEY
        self.table = VOLUME_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST
