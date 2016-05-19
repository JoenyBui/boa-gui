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

# UNITY_VALUE == 'quad_meter'

# UNITY_VALUE == 'm^3'
FACTOR_INERTIA_QUADRATEC_METER = 1.0
FACTOR_INERTIA_QUADRATEC_MM = 0.001**4
FACTOR_INERTIA_QUADRATEC_FT = 0.3048**4
FACTOR_INERTIA_QUADRATEC_IN = 0.0254**4

ID_NAME_INERTIA_M4 = ("m^4", "m4", "M4")
ID_NAME_INERTIA_MM4 = ("mm^4", "mm4", "MM4")
ID_NAME_INERTIA_FT4 = ("ft^4", "ft4", "FT4")
ID_NAME_INERTIA_IN4 = ("in^4", "in4", "IN4")

INERTIA_KEY = {
    'm^4': FACTOR_INERTIA_QUADRATEC_METER,
    'm4': FACTOR_INERTIA_QUADRATEC_METER,
    'mm^4': FACTOR_INERTIA_QUADRATEC_MM,
    'mm4': FACTOR_INERTIA_QUADRATEC_MM,
    'ft^4': FACTOR_INERTIA_QUADRATEC_FT,
    'ft4': FACTOR_INERTIA_QUADRATEC_FT,
    'in^4': FACTOR_INERTIA_QUADRATEC_IN,
    'in4': FACTOR_INERTIA_QUADRATEC_IN
}

DEFAULT_INERTIA_LIST = [
    'm4',
    'mm4',
    'ft4',
    'in4'
]

DEFAULT_IMPERIAL_LIST = [
    'ft4',
    'in4'
]

DEFAULT_METRIC_LIST = [
    'm4',
    'mm4'
]


def get_inertia_conversion_factor(origin, destination):
    """
    Get the inertia conversion factor.
    :param origin:
    :param destination:
    :return:
    """
    origin_factor = INERTIA_KEY.get(origin)
    destination_factor = INERTIA_KEY.get(destination)

    return destination_factor / origin_factor
