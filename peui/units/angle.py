"""
**Angle**

unit value = radian

"""
import math

from . import Unit, UNIT_ANGLE_KEY

__author__ = 'jbui'


FACTOR_ANGLE_DEGREE = 180.0 / math.pi
FACTOR_ANGLE_RADIAN = 1

ANGLE_KEY = {
    'degrees': FACTOR_ANGLE_DEGREE,
    'radians': FACTOR_ANGLE_RADIAN
}

DEFAULT_IMPERIAL_LIST = [
    'degrees',
    'radians'
]

DEFAULT_METRIC_LIST = [
    'degrees',
    'radians'
]


class AngleUnit(Unit):
    """
    **Angle Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_ANGLE_KEY
        self.table = ANGLE_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST
