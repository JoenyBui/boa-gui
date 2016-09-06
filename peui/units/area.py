"""
**area**

unity value = m^2

"""
from . import Unit, UNIT_AREA_KEY

__author__ = 'jbui'

# UNITY_VALUE == 'm^2'
FACTOR_AREA_SQUARE_KILOMETER = 1E6
FACTOR_AREA_SQUARE_METER = 1.0
FACTOR_AREA_SQUARE_CENTIMETER = 0.0001
FACTOR_AREA_SQUARE_MILLIMETER = 1E-6
FACTOR_AREA_SQUARE_INCH = 0.00064516
FACTOR_AREA_SQUARE_FEET = 0.092903
FACTOR_AREA_SQUARE_YARD = 0.836127
FACTOR_AREA_SQUARE_MILE = 2.59E6
FACTOR_AREA_ACRE = 4046.86

ID_NAME_AREA_FEET = ("ft2", "feet2", "Foot2")
ID_NAME_AREA_INCH = ("in2", "in.^2", "inches2")
ID_NAME_AREA_YARD = ("yd2", "yard2")

ID_NAME_AREA_MILLIMETER = ("mm2", "mm^2")
ID_NAME_AREA_CENTIMETER = ("cm2", "cm^2")
ID_NAME_AREA_METER = ("m2", "meter2")
ID_NAME_AREA_KILOMETER = ("km2", "kilometer2")

AREA_KEY = {
    'ft2': FACTOR_AREA_SQUARE_FEET,
    'feet2': FACTOR_AREA_SQUARE_FEET,
    'ft.2': FACTOR_AREA_SQUARE_FEET,
    'ft^2': FACTOR_AREA_SQUARE_FEET,
    'in2': FACTOR_AREA_SQUARE_INCH,
    'inch2': FACTOR_AREA_SQUARE_INCH,
    'in.2': FACTOR_AREA_SQUARE_INCH,
    'in^2': FACTOR_AREA_SQUARE_INCH,
    'in^3/in': FACTOR_AREA_SQUARE_INCH,
    'yd2': FACTOR_AREA_SQUARE_YARD,
    'yard2': FACTOR_AREA_SQUARE_YARD,
    'mm2': FACTOR_AREA_SQUARE_MILLIMETER,
    'millimeter2': FACTOR_AREA_SQUARE_MILLIMETER,
    'mm^2': FACTOR_AREA_SQUARE_MILLIMETER,
    'mm^3/mm': FACTOR_AREA_SQUARE_MILLIMETER,
    'cm2': FACTOR_AREA_SQUARE_CENTIMETER,
    'centimeter2': FACTOR_AREA_SQUARE_CENTIMETER,
    'cm^2': FACTOR_AREA_SQUARE_CENTIMETER,
    'm2': FACTOR_AREA_SQUARE_METER,
    'm^2': FACTOR_AREA_SQUARE_METER,
    'meter2': FACTOR_AREA_SQUARE_METER,
    'm^2': FACTOR_AREA_SQUARE_KILOMETER,
    'km2': FACTOR_AREA_SQUARE_KILOMETER,
    'kilometer2': FACTOR_AREA_SQUARE_KILOMETER,
    'km^2': FACTOR_AREA_SQUARE_KILOMETER
}

DEFAULT_AREA_LIST = [
    'in2',
    'ft2',
    'yd2',
    'm2'
]

DEFAULT_IMPERIAL__LIST = [
    'in^2',
    'ft^2'
]

DEFAULT_METRIC_LIST = [
    'cm^2',
    'm^2'
]


def get_area_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = AREA_KEY.get(origin)
    destination_factor = AREA_KEY.get(destination)

    return origin_factor / destination_factor


class AreaUnit(Unit):
    """
    **Area Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_AREA_KEY
        self.table = AREA_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL__LIST

    def get_conversion_factor(self, origin, destination):
        return get_area_conversion_factor(origin, destination)
