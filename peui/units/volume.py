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

# UNITY_VALUE == 'm^3'
FACTOR_VOLUME_CUBIC_METER = 1.0
FACTOR_VOLUME_CUBIC_MM = 1E-6
FACTOR_VOLUME_CUBIC_FT = 0.0283168
FACTOR_VOLUME_CUBIC_IN = 1.6387e-5

ID_NAME_VOLUME_M3 = ("m^3", "m3", "M3")
ID_NAME_VOLUME_MM3 = ("mm^3", "mm3", "MM3")
ID_NAME_VOLUME_FT3 = ("ft^3", "ft3", "FT3")
ID_NAME_VOLUME_IN3 = ("in^3", "in3", "IN3")

VOLUME_KEY = {
    'm^3': FACTOR_VOLUME_CUBIC_METER,
    'm3': FACTOR_VOLUME_CUBIC_METER,
    'mm^3': FACTOR_VOLUME_CUBIC_MM,
    'mm3': FACTOR_VOLUME_CUBIC_MM,
    'ft^3': FACTOR_VOLUME_CUBIC_FT,
    'ft3': FACTOR_VOLUME_CUBIC_FT,
    'in^3': FACTOR_VOLUME_CUBIC_IN,
    'in3': FACTOR_VOLUME_CUBIC_IN
}

DEFAULT_VOLUME_LIST = [
    'm3',
    'mm3',
    'ft3',
    'in3'
]

DEFAULT_ENGLISH_VOLUME_LIST = [
    'ft3',
    'in3'
]

DEFAULT_METRIC_VOLUME_LIST = [
    'm3',
    'mm3'
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

    return destination_factor / origin_factor

