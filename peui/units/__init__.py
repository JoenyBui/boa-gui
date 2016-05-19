from .charge import get_charge_conversion_factor
from .length import get_length_conversion_factor
from .pressure import get_pressure_conversion_factor
from .mass import get_mass_conversion_factor

__author__ = 'jbui'

KEY_IMPERIAL = 'imperial'
KEY_METRIC = 'metric'

UNIT_AREA_KEY = 'area'
UNIT_CHARGE_KEY = 'charge'
UNIT_INERTIA_KEY = 'inertia'
UNIT_LENGTH_KEY = 'length'
UNIT_MASS_KEY = 'mass'
UNIT_PRESSURE_KEY = 'pressure'
UNIT_VOLUME_KEY = 'volume'


BASE_UNITS = dict(
    area='m2',
    charge='TNT',
    inertia='m4',
    length='meter',
    mass='gram',
    pressure='Pa',
    volume='m3'
)


def get_base_value(type, value, unit):
    """
    Get the base value.
    :param type:
    :param value:
    :param unit:
    :return:
    """
    value = float(value)

    if type == UNIT_CHARGE_KEY:
        return value*get_charge_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_LENGTH_KEY:
        return value*get_length_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_MASS_KEY:
        return value*get_mass_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_PRESSURE_KEY:
        return value*get_pressure_conversion_factor(unit, BASE_UNITS[type])
    else:
        return None
