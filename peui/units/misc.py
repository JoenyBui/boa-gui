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


DEFAULT_MISC_LIST = [
    'lb/in',
    'lb-in/in',
    'in4/in',
    'in3/in',
    'lb/ft'
]

DEFAULT_IMPERIAL_LIST = [
    'lb/in',
    'lb-in/in',
    'in4/in',
    'in3/in',
    'lb/ft'
]

DEFAULT_METRIC_LIST = [
    'lb/in',
    'lb-in/in',
    'in4/in',
    'in3/in',
    'lb/ft'
]


def get_misc_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    pass
    # origin_factor = TORQUE_KEY.get(origin)
    # destination_factor = TORQUE_KEY.get(destination)
    #
    # return destination_factor / origin_factor
