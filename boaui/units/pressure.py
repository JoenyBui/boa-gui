from . import Unit, UNIT_PRESSURE_KEY

__author__ = 'Joeny'

# UNITY_VALUE == PA
FACTOR_PRESSURE_PASCAL = 1.0
FACTOR_PRESSURE_KILOPASCAL = 1.0/1000.0
FACTOR_PRESSURE_MEGAPASCAL = 1.0/1E6
FACTOR_PRESSURE_PSI = 1.0/6894.75728
FACTOR_PRESSURE_PSF = 1.0/47.8802589
FACTOR_PRESSURE_KSI = 1.0/6894760.0
FACTOR_PRESSURE_ATM = 1.0/101325.0
FACTOR_PRESSURE_KILOGRAM_M2 = 1.0/9.8067

ID_NAME_PRESSURE_PASCAL = ("Pa", "pa", "pascal")
ID_NAME_PRESSURE_KILOPASCAL = ("kPa", "kPA", "kilopascal")
ID_NAME_PRESSURE_MEGAPASCAL = ("MPa", "MPA")
ID_NAME_PRESSURE_PSI = ("psi", "PSI")
ID_NAME_PRESSURE_PSF = ("psf", "PSF")
ID_NAME_PRESSURE_KSI = ("ksi", "KSI")
ID_NAME_PRESSURE_KILOGRAM_M2 = ("kg/m^2",)

PRESSURE_KEY = {
    'psi': FACTOR_PRESSURE_PSI,
    'psf': FACTOR_PRESSURE_PSF,
    'ksi': FACTOR_PRESSURE_KSI,
    'Pa': FACTOR_PRESSURE_PASCAL,
    'kPa': FACTOR_PRESSURE_KILOPASCAL,
    'MPa': FACTOR_PRESSURE_MEGAPASCAL,
    'kg/m2': FACTOR_PRESSURE_KILOGRAM_M2,
    'kg/m^2': FACTOR_PRESSURE_KILOGRAM_M2
}

DEFAULT_PRESSURE_LIST = [
    'psi',
    'psf',
    'ksi',
    'Pa',
    'MPa',
]

DEFAULT_IMPERIAL_LIST = [
    'psi',
    'psf',
    'ksi'
]

DEFAULT_METRIC_LIST = [
    'Pa',
    'kPa',
    'MPa',
    'kg/m^2'
]


def get_pressure_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = PRESSURE_KEY.get(origin)
    destination_factor = PRESSURE_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class PressureUnit(Unit):
    """
    **Pressure Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_PRESSURE_KEY
        self.table = PRESSURE_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL_LIST

