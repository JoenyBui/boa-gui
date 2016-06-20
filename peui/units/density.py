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

# UNITY_VALUE == g/cm^3
FACTOR_DENSITY_G_CM3 = 1
FACTOR_DENSITY_KG_M3 = 0.001
FACTOR_DENSITY_LB_FT3 = 0.0160185
FACTOR_DENSITY_LB_IN3 = 27.699

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

