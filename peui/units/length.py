from . import Unit, UNIT_LENGTH_KEY

__author__ = 'jbui'

# UNITY_VALUE == 'meter
FACTOR_LENGTH_METER = 1.0
FACTOR_LENGTH_KILOMETER = 1000
FACTOR_LENGTH_CENTIMETER = 0.01
FACTOR_LENGTH_MILLIMETER = 0.001
FACTOR_LENGTH_INCH = 0.0254
FACTOR_LENGTH_FEET = 0.3048
FACTOR_LENGTH_YARD = 0.9144
FACTOR_LENGTH_MILE = 1609.34

ID_NAME_LENGTH_FEET = ("ft", "feet", "Foot")
ID_NAME_LENGTH_INCH = ("in", "in.", "inches")
ID_NAME_LENGTH_YARD = ("yd", "yard")
ID_NAME_LENGTH_MILE = ("mile",)

ID_NAME_LENGTH_METER = ("m", "meter")
ID_NAME_LENGTH_KILOMETER = ("km", "kilometer")
ID_NAME_LENGTH_CENTIMETER = ("cm", "centimeter")
ID_NAME_LENGTH_MILLIMETER = ("mm", "millimeter")

LENGTH_KEY = {
    'ft': FACTOR_LENGTH_FEET,
    'feet': FACTOR_LENGTH_FEET,
    'ft.': FACTOR_LENGTH_FEET,
    'in': FACTOR_LENGTH_INCH,
    'inch': FACTOR_LENGTH_INCH,
    'in.': FACTOR_LENGTH_INCH,
    'yd': FACTOR_LENGTH_YARD,
    'yard': FACTOR_LENGTH_YARD,
    'm': FACTOR_LENGTH_METER,
    'meter': FACTOR_LENGTH_METER,
    'km': FACTOR_LENGTH_KILOMETER,
    'kilometer': FACTOR_LENGTH_KILOMETER,
    'cm': FACTOR_LENGTH_CENTIMETER,
    'centimeter': FACTOR_LENGTH_CENTIMETER,
    'mm': FACTOR_LENGTH_MILLIMETER,
    'millimeter': FACTOR_LENGTH_MILLIMETER
}


DEFAULT_LENGTH_LIST = [
    'in',
    'ft',
    'yd',
    'm'
]

DEFAULT_IMPERIAL_LIST = [
    'in',
    'ft',
    'yd',
    'mile'
]

DEFAULT_METRIC_LIST = [
    'm',
    'km',
    'cm',
    'mm'
]


def get_length_conversion_factor(origin, destination):
    """
    Get the length conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = LENGTH_KEY.get(origin)
    destination_factor = LENGTH_KEY.get(destination)

    return origin_factor / destination_factor


class LengthUnit(Unit):

    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_LENGTH_KEY
        self.table = LENGTH_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

    def get_conversion_factor(self, origin, destination):
        return get_length_conversion_factor(origin, destination)

