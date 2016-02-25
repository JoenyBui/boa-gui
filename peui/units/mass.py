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

# UNITY_VALUE = GRAM
FACTOR_PRESSURE_GRAM = 1.0
FACTOR_PRESSURE_KILOGRAM = 0.001
FACTOR_PRESSURE_POUND_MASS = 0.0022046226218

ID_NAME_MASS_GRAM = ('g', 'gram')
ID_NAME_MASS_KILOGRAM = ('kg', 'kilogram')
ID_NAME_POUND_MASS = ('lbm', 'pound')

MASS_KEY = {
    'g': FACTOR_PRESSURE_GRAM,
    'gram': FACTOR_PRESSURE_GRAM,
    'kg': FACTOR_PRESSURE_KILOGRAM,
    'kilogram': FACTOR_PRESSURE_KILOGRAM,
    'lbm': FACTOR_PRESSURE_POUND_MASS,
    'pound': FACTOR_PRESSURE_POUND_MASS
}


DEFAULT_MASS_LIST = [
    'g',
    'kg',
    'lbm'
]


def get_mass_conversion_factor(origin, destination):
    origin_factor = MASS_KEY.get(origin)
    destination_factor = MASS_KEY.get(destination)

    return destination_factor / origin_factor
