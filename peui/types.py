from .units.length import LENGTH_KEY
from .units.area import AREA_KEY
from .units.charge import CHARGE_KEY
from .units.inertia import INERTIA_KEY
from .units.mass import MASS_KEY
from .units.volume import VOLUME_KEY
from .units.pressure import PRESSURE_KEY
from .units.density import DENSITY_KEY
from .units.torque import TORQUE_KEY


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
        float(string)

        return True
    except ValueError:
        return False


def cast_int(string):
    """

    :param string:
    :return:
    """
    if is_float(string):
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


def cast_length_unit(string):
    possible_units = LENGTH_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_area_unit(string):
    possible_units = AREA_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_charge_unit(string):
    possible_units = CHARGE_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_inertia_unit(string):
    possible_units = INERTIA_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_mass_unit(string):
    possible_units = MASS_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_volume_unit(string):
    possible_units = VOLUME_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_pressure_unit(string):
    possible_units = PRESSURE_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_density_unit(string):
    possible_units = DENSITY_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None


def cast_torque_unit(string):
    possible_units = TORQUE_KEY.keys()

    if string in possible_units:
        return string
    else:
        # TODO: Write out to log file

        return None
