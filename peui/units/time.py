"""
**time**

unity value = s


"""

from . import Unit, UNIT_TIME_KEY

FACTOR_TIME_SECOND = 1.0
FACTOR_TIME_MILLISECOND = None

ID_NAME_TIME_SECOND = ('s')
ID_NAME_TIME_MILLISECOND = ('ms')

__author__ = 'jbui'

TIME_KEY = {
    's': FACTOR_TIME_SECOND,
    'ms': FACTOR_TIME_MILLISECOND,
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


class TimeUnit(Unit):
    """
    **Time Unit**

    """
    def __init__(self):
        Unit.__init__(self)

        self.key = UNIT_TIME_KEY
