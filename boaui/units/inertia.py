"""
**Inertia**

"""
from . import Unit, UNIT_INERTIA_KEY

__author__ = 'Joeny'

# UNITY_VALUE == 'quad_meter'

# UNITY_VALUE == 'm^3'
FACTOR_INERTIA_QUADRATIC_METER = 1.0
FACTOR_INERTIA_QUADRATIC_MM = 1.0/(0.001**4)
FACTOR_INERTIA_QUADRATIC_FT = 1.0/0.3048**4
FACTOR_INERTIA_QUADRATIC_IN = 1.0/0.0254**4

ID_NAME_INERTIA_M4 = ("m^4", "m4", "M4")
ID_NAME_INERTIA_MM4 = ("mm^4", "mm4", "MM4")
ID_NAME_INERTIA_FT4 = ("ft^4", "ft4", "FT4")
ID_NAME_INERTIA_IN4 = ("in^4", "in4", "IN4")

INERTIA_KEY = {
    'm^4': FACTOR_INERTIA_QUADRATIC_METER,
    'm4': FACTOR_INERTIA_QUADRATIC_METER,
    'mm^4': FACTOR_INERTIA_QUADRATIC_MM,
    'mm4': FACTOR_INERTIA_QUADRATIC_MM,
    'ft^4': FACTOR_INERTIA_QUADRATIC_FT,
    'ft4': FACTOR_INERTIA_QUADRATIC_FT,
    'in^4': FACTOR_INERTIA_QUADRATIC_IN,
    'in4': FACTOR_INERTIA_QUADRATIC_IN
}

DEFAULT_INERTIA_LIST = [
    'm4',
    'mm4',
    'ft4',
    'in4'
]

DEFAULT_IMPERIAL_LIST = [
    'ft^4',
    'in^4'
]

DEFAULT_METRIC_LIST = [
    'm^4',
    'mm^4'
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

    return float(destination_factor) / float(origin_factor)


class InertiaUnit(Unit):
    """
    **Inertia Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_INERTIA_KEY
        self.table = INERTIA_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST
