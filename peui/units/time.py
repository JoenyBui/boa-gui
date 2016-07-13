"""
**time**

unity value = s


"""

from . import Unit, UNIT_TIME_KEY

FACTOR_TIME_SECOND = 1.0
FACTOR_TIME_MILLISECOND = 0.001

ID_NAME_TIME_SECOND = ('s', 'sec')
ID_NAME_TIME_MILLISECOND = ('ms', 'millisecond')

__author__ = 'jbui'

TIME_KEY = {
    's': FACTOR_TIME_SECOND,
    'sec': FACTOR_TIME_SECOND,
    'second': FACTOR_TIME_SECOND,
    'ms': FACTOR_TIME_MILLISECOND,
    'millisecond': FACTOR_TIME_MILLISECOND
}

DEFAULT_TIME_LIST = [
    's',
    'ms'
]

DEFAULT_IMPERIAL__LIST = [
    's',
    'ms'
]

DEFAULT_METRIC_LIST = [
    's',
    'ms'
]


def get_time_conversion_factor(origin, destination):
    """
    Get torque conversion factor.

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = TIME_KEY.get(origin)
    destination_factor = TIME_KEY.get(destination)

    return destination_factor / origin_factor


class TimeUnit(Unit):
    """
    **Time Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_TIME_KEY
        self.table = TIME_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL__LIST

    def get_conversion_factor(self, origin, destination):
        return get_time_conversion_factor(origin, destination)
