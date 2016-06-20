"""
 *  PROTECTION ENGINEERING CONSULTANTS CONFIDENTIAL
 *
 *  [2014] - [2015] Protection Engineering Consultants
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Protection Engineering Consultants and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Protection Engineering Consultants
 * and its suppliers and may be covered by U.S. and Foreign Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Protection Engineering Consultants.
"""

__author__ = 'jbui'

# UNITY_VALUE == 'm^2'
FACTOR_AREA_SQUARE_CENTIMETER = 0.0001
FACTOR_AREA_SQUARE_METER = 1.0
FACTOR_AREA_SQUARE_KILOMETER = 1E6
FACTOR_AREA_SQUARE_INCH = 0.00064516
FACTOR_AREA_SQUARE_FEET = 0.092903
FACTOR_AREA_SQUARE_YARD = 0.836127
FACTOR_AREA_SQUARE_MILE = 2.59E6
FACTOR_AREA_ACRE = 4046.86

ID_NAME_AREA_FEET = ("ft2", "feet2", "Foot2")
ID_NAME_AREA_INCH = ("in2", "in.^2", "inches2")
ID_NAME_AREA_YARD = ("yd2", "yard2")

ID_NAME_AREA_CENTIMETER = ("cm2", "cm^2")
ID_NAME_AREA_METER = ("m2", "meter2")
ID_NAME_AREA_KILOMETER = ("km2", "kilometer2")

AREA_KEY = {
    'ft2': FACTOR_AREA_SQUARE_FEET,
    'feet2': FACTOR_AREA_SQUARE_FEET,
    'ft.2': FACTOR_AREA_SQUARE_FEET,
    'in2': FACTOR_AREA_SQUARE_INCH,
    'inch2': FACTOR_AREA_SQUARE_INCH,
    'in.2': FACTOR_AREA_SQUARE_INCH,
    'yd2': FACTOR_AREA_SQUARE_YARD,
    'yard2': FACTOR_AREA_SQUARE_YARD,
    'cm2': FACTOR_AREA_SQUARE_CENTIMETER,
    'centimeter2': FACTOR_AREA_SQUARE_CENTIMETER,
    'cm^2': FACTOR_AREA_SQUARE_CENTIMETER,
    'm2': FACTOR_AREA_SQUARE_METER,
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
    'in2',
    'ft2',
    'yd2'
]

DEFAULT_METRIC_LIST = [
    'cm2',
    'm2',
    'km2'
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
