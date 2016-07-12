"""

Unit Value == N-m

"""
from . import Unit, UNIT_TORQUE_KEY

__author__ = 'jbui'


FACTOR_TORQUE_N_M = 1.0
FACTOR_TORQUE_N_MM = 0.001
FACTOR_TORQUE_LB_IN = 175.126772
FACTOR_TORQUE_KIP_IN = 175126.772

ID_NAME_TORQUE_LB_IN = ("lb-in", "LB-IN")


TORQUE_KEY = {
    'lb-in': FACTOR_TORQUE_LB_IN,
    'kip-in': FACTOR_TORQUE_KIP_IN,
    'N-mm': FACTOR_TORQUE_N_MM,
    'N-m': FACTOR_TORQUE_N_M
}

DEFAULT_TORQUE_LIST = [
    'lb-in',
    'kip-in',
    'N-mm',
    'N-m'
]

DEFAULT_IMPERIAL_LIST = [
    'lb-in',
    'kip-in'
]

DEFAULT_METRIC_LIST = [
    'N-m',
    'N-mm'
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

    return origin_factor / destination_factor


class TorqueUnit(Unit):
    """
    **Torque Unit**

    """
    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_TORQUE_KEY
        self.table = TORQUE_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

    def get_conversion_factor(self, origin, destination):
        return get_torque_conversion_factor(origin, destination)
