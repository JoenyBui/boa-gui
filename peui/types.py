from .units.acceleration import ACCELERATION_KEY
from .units.area import AREA_KEY
from .units.area_density import AREA_DENSITY
from .units.charge import CHARGE_KEY
from .units.density import DENSITY_KEY
from .units.force import FORCE_KEY
from .units.inertia import INERTIA_KEY
from .units.length import LENGTH_KEY
from .units.linear_density import LINEAR_DENSITY_KEY
from .units.linear_pressure import LINEAR_PRESSURE_KEY
from .units.mass import MASS_KEY
from .units.pressure import PRESSURE_KEY
from .units.specific_weight import SPECIFIC_WEIGHT_KEY
from .units.time import TIME_KEY
from .units.tnt import TNT_KEY
from .units.torque import TORQUE_KEY
from .units.velocity import VELOCITY_KEY
from .units.volume import VOLUME_KEY


def is_float(string):
    """
    Is string a float representation.

    :param string:
    :return:
    """

    try:
        float(string)
        return True
    except ValueError:
        return False


def is_int(string):
    """
    Is string an integer representation.

    :param string:
    :return:
    """
    try:
        int(string)

        return True
    except ValueError:
        return False


def cast_int(string):
    """

    :param string:
    :return:
    """
    if is_int(string):
        return int(string)
    else:
        # TODO: Write out to log file

        return None


def cast_float(string):
    """

    :param string:
    :return:
    """
    if is_float(string):
        return float(string)
    else:
        # TODO: Write out to log file

        return None


def cast_acceleration_unit(string):
    if string in ACCELERATION_KEY.keys():
        return string
    else:
        return None


def cast_area_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = AREA_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_area_density_unit(string):
    if string in AREA_DENSITY.keys():
        return string
    else:
        return None


def cast_charge_unit(string):
    """

    :param string:
    :return:
    """
    if string in CHARGE_KEY.keys():
        return string
    else:
        return None


def cast_density_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = DENSITY_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_force_unit(string):
    if string in FORCE_KEY.keys():
        return string
    else:
        return None


def cast_inertia_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = INERTIA_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_length_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = LENGTH_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_linear_density(string):
    if string in LINEAR_DENSITY_KEY.keys():
        return string
    else:
        return None


def cast_linear_pressure(string):
    if string in LINEAR_PRESSURE_KEY.keys():
        return string
    else:
        return None


def cast_mass_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = MASS_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_pressure_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = PRESSURE_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_specific_weight_unit(string):
    if string in SPECIFIC_WEIGHT_KEY.keys():
        return string
    else:
        return None


def cast_time_unit(string):
    possible_units = TIME_KEY.keys()

    if string in possible_units:
        return string
    else:
        #TODO: Write out time unit

        return None


def cast_tnt_unit(string):
    if string in TNT_KEY.keys():
        return string
    else:
        return None


def cast_torque_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = TORQUE_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_velocity_unit(string):
    if string in VELOCITY_KEY.keys():
        return string
    else:
        return None


def cast_volume_unit(string):
    """

    :param string:
    :return:
    """
    possible_units = VOLUME_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None
