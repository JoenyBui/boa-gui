from . import Unit, UNIT_DENSITY_KEY

__author__ = 'jbui'

# UNITY_VALUE == g/cm^3
FACTOR_DENSITY_G_CM3 = 1
FACTOR_DENSITY_KG_M3 = 0.001
FACTOR_DENSITY_LB_FT3 = 0.0160185
FACTOR_DENSITY_LB_IN3 = 27.6799

ID_NAME_DENSITY_G_CM3 = ("g/cm3", "g/cm^3", "G/CM3", "G/CM^3")
ID_NAME_DENSITY_KG_M3 = ("kg/m3", "kg/m^3", "KG/M3", "KG/M^3")
ID_NAME_DENSITY_LB_FT3 = ("lb/ft^3", "lb/ft3", "LB/FT3", "LB/FT^3")
ID_NAME_DENSITY_LB_IN3 = ("lb/in^3", "lb/in3", "LB/IN3", "LB/IN^3")

DENSITY_KEY = {
    "g/cm3": FACTOR_DENSITY_G_CM3,
    "g/cm^3": FACTOR_DENSITY_G_CM3,
    "G/CM3": FACTOR_DENSITY_G_CM3,
    "G/CM^3": FACTOR_DENSITY_G_CM3,
    "kg/m3": FACTOR_DENSITY_KG_M3,
    "kg/m^3": FACTOR_DENSITY_KG_M3,
    "KG/M3": FACTOR_DENSITY_KG_M3,
    "KG/M^3": FACTOR_DENSITY_KG_M3,
    "lb/ft^3": FACTOR_DENSITY_LB_FT3,
    "lb/ft3": FACTOR_DENSITY_LB_FT3,
    "LB/FT3": FACTOR_DENSITY_LB_FT3,
    "LB/FT^3": FACTOR_DENSITY_LB_FT3,
    "lb/in^3": FACTOR_DENSITY_LB_IN3,
    "lb/in3": FACTOR_DENSITY_LB_IN3,
    "LB/IN3": FACTOR_DENSITY_LB_IN3,
    "LB/IN^3": FACTOR_DENSITY_LB_IN3
}

DEFAULT_DENSITY_LIST = [
    'g/cm3',
    'kg/m3',
    'lb/ft3',
    'lb/in3'
]

DEFAULT_IMPERIAL_LIST = [
    'lb/ft3',
    'lb/in3'
]

DEFAULT_METRIC_LIST = [
    'g/cm3',
    'kg/m3'
]


def get_density_conversion_factor(origin, destination):
    """
    Get the density conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = DENSITY_KEY.get(origin)
    destination_factor = DENSITY_KEY.get(destination)

    return origin_factor / destination_factor


class DensityUnit(Unit):
    """
    Density Unit

    """
    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_DENSITY_KEY
        self.table = DENSITY_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST

    def get_conversion_factor(self, origin, destination):
        return get_density_conversion_factor(origin, destination)
