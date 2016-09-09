"""
1 Meter = [value] Destination Unit


"""
from . import Unit, UNIT_LENGTH_KEY


__author__ = 'jbui'

# UNITY_VALUE == 'meter
FACTOR_LENGTH_METER = 1.0
FACTOR_LENGTH_KILOMETER = 0.001
FACTOR_LENGTH_CENTIMETER = 100
FACTOR_LENGTH_MILLIMETER = 1000
FACTOR_LENGTH_INCH = 39.370
FACTOR_LENGTH_FEET = 3.28084
FACTOR_LENGTH_YARD = 1.09361
FACTOR_LENGTH_MILE = 0.000621371192237

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
    'in^2/in': FACTOR_LENGTH_INCH,
    'yd': FACTOR_LENGTH_YARD,
    'yard': FACTOR_LENGTH_YARD,
    'm': FACTOR_LENGTH_METER,
    'meter': FACTOR_LENGTH_METER,
    'km': FACTOR_LENGTH_KILOMETER,
    'kilometer': FACTOR_LENGTH_KILOMETER,
    'cm': FACTOR_LENGTH_CENTIMETER,
    'centimeter': FACTOR_LENGTH_CENTIMETER,
    'mm': FACTOR_LENGTH_MILLIMETER,
    'millimeter': FACTOR_LENGTH_MILLIMETER,
    'mile': FACTOR_LENGTH_MILE
}


DEFAULT_LENGTH_LIST = [
    'in',
    'ft',
    'yd',
    'm',
    'km',
    'cm',
    'mm'
]

DEFAULT_IMPERIAL_LIST = [
    'in',
    'ft'
]

DEFAULT_METRIC_LIST = [
    'm',
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

    return float(destination_factor) / float(origin_factor)


class LengthUnit(Unit):
    """
    **Length Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_LENGTH_KEY
        self.table = LENGTH_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

    # def get_conversion_factor(self, origin, destination):
    #     return get_length_conversion_factor(origin, destination)

