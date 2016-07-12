
__author__ = 'jbui'

KEY_IMPERIAL = 'imperial'
KEY_METRIC = 'metric'

UNIT_ACCELERATION = 'acceleration'
UNIT_AREA_DENSITY_KEY = 'area_density'
UNIT_AREA_KEY = 'area'
UNIT_CHARGE_KEY = 'charge'
UNIT_DENSITY_KEY = 'density'
UNIT_FORCE_KEY = 'force'
UNIT_INERTIA_KEY = 'inertia'
UNIT_LENGTH_KEY = 'length'
UNIT_LINEAR_DENSITY = 'linear_density'
UNIT_LINEAR_PRESSURE = 'linear_pressure'
UNIT_MASS_KEY = 'mass'
UNIT_PRESSURE_KEY = 'pressure'
UNIT_TIME_KEY = 'time'
UNIT_TNT_KEY = 'tnt'
UNIT_TORQUE_KEY = 'torque'
UNIT_VELOCITY = 'velocity'
UNIT_VOLUME_KEY = 'volume'

BASE_UNITS = dict(
    acceleration='m/s2',
    area='m2',
    area_density='kg/m^2',
    charge='TNT',
    density='lb/ft3',
    force='N',
    inertia='m4',
    length='meter',
    linear_density='plf',
    linear_pressure='plf',
    mass='gram',
    pressure='Pa',
    time='s',
    tnt='ton',
    torque='lb-in',
    velocity='m/s',
    volume='m3',
)


def get_base_value(type, value, unit):
    """
    Get the base value.

    :param type:
    :param value:
    :param unit:
    :return:
    """
    from .area import get_area_conversion_factor
    from .charge import get_charge_conversion_factor
    from .inertia import get_inertia_conversion_factor
    from .length import get_length_conversion_factor
    from .mass import get_mass_conversion_factor
    from .pressure import get_pressure_conversion_factor
    from .volume import get_volume_conversion_factor
    from .tnt import get_tnt_conversion_factor
    from .density import get_density_conversion_factor
    from .torque import get_torque_conversion_factor

    value = float(value)

    if type == UNIT_AREA_KEY:
        return value*get_area_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_CHARGE_KEY:
        return value*get_charge_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_INERTIA_KEY:
        return value*get_inertia_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_LENGTH_KEY:
        return value*get_length_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_MASS_KEY:
        return value*get_mass_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_PRESSURE_KEY:
        return value*get_pressure_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_VOLUME_KEY:
        return value*get_volume_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_TNT_KEY:
        return value * get_tnt_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_DENSITY_KEY:
        return value*get_density_conversion_factor(unit, BASE_UNITS[type])
    elif type == UNIT_TORQUE_KEY:
        return value*get_torque_conversion_factor(unit, BASE_UNITS[type])
    else:
        return None


class Unit(object):
    """
    Unit Object

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        self.key = None
        self.table = None

        self.metric_list = kwargs.get('metric_list', None)
        self.imperial_list = kwargs.get('imperial_list', None)

        self.default_selection = kwargs.get('default_selection', 0)
        self.unit_system = kwargs.get('unit_system', None)

    def get_conversion_factor(self, origin, destination):
        pass

