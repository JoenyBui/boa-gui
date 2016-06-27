
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
    Get torque conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = TORQUE_KEY.get(origin)
    destination_factor = TORQUE_KEY.get(destination)

    return destination_factor / origin_factor
