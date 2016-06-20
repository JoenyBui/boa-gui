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

# UNITY_VALUE == lb-in
FACTOR_TORQUE_LB_IN = 1.0

ID_NAME_TORQUE_LB_IN = ("lb-in", "LB-IN")


TORQUE_KEY = {
    'lb-in': FACTOR_TORQUE_LB_IN
}

DEFAULT_TORQUE_LIST = [
    'lb-in'
]

DEFAULT_IMPERIAL_LIST = [
    'lb-in'
]

DEFAULT_METRIC_LIST = [
    'lb-in'
]


def get_torque_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = TORQUE_KEY.get(origin)
    destination_factor = TORQUE_KEY.get(destination)

    return destination_factor / origin_factor
