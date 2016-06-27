
__author__ = 'jbui'

# UNITY_VALUE == PA
FACTOR_PRESSURE_PASCAL = 1.0
FACTOR_PRESSURE_KILOPASCAL = 0.001
FACTOR_PRESSURE_PSI = 0.000145038
FACTOR_PRESSURE_PSF = 0.00174045
FACTOR_PRESSURE_KSI = 0.000000145038
FACTOR_PRESSURE_ATM = 9.8692e-6

ID_NAME_PRESSURE_PASCAL = ("Pa", "pa", "pascal")
ID_NAME_PRESSURE_KILOPASCAL = ("kPa", "kPA", "kilopascal")
ID_NAME_PRESSURE_PSI = ("psi", "PSI")
ID_NAME_PRESSURE_PSF = ("psf", "PSF")
ID_NAME_PRESSURE_KSI = ("ksi", "KSI")


PRESSURE_KEY = {
    'psi': FACTOR_PRESSURE_PSI,
    'psf': FACTOR_PRESSURE_PSF,
    'ksi': FACTOR_PRESSURE_KSI,
    'Pa': FACTOR_PRESSURE_PASCAL,
    'kPa': FACTOR_PRESSURE_KILOPASCAL
}

DEFAULT_PRESSURE_LIST = [
    'psi',
    'psf',
    'ksi',
    'Pa'
]

DEFAULT_IMPERIAL_LIST = [
    'psi',
    'psf',
    'ksi'
]

DEFAULT_METRIC_LIST = [
    'Pa',
    'kPa'
]


def get_pressure_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = PRESSURE_KEY.get(origin)
    destination_factor = PRESSURE_KEY.get(destination)

    return destination_factor / origin_factor

