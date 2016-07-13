"""
**area density**

Unity Value = kg/m^2

English Unit Value = psi-ms^2/in

"""
from . import Unit, UNIT_AREA_DENSITY_KEY

__author__ = 'jbui'

FACTOR_AREA_DENSITY_KILOGRAM_M2 = 1.0
FACTOR_AREA_DENSITY_PSI_MS2_IN = None

AREA_DENSITY = {
    'kg/m2': FACTOR_AREA_DENSITY_KILOGRAM_M2,
    'psi-ms^2/in': FACTOR_AREA_DENSITY_PSI_MS2_IN
}

DEFAULT_AREA_LIST = [
    'kg/m2',
    'psi-ms^2/in'
]

DEFAULT_IMPERIAL__LIST = [
    'psi-ms^2/in'
]

DEFAULT_METRIC_LIST = [
    'kg/m2',
]


def get_area_density_conversion_factor(origin, destination):
    """

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = AREA_DENSITY.get(origin)
    destination_factor = AREA_DENSITY.get(destination)

    return origin_factor / destination_factor


class AreaDensityUnit(Unit):
    """
    **Area Density Unit**

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_AREA_DENSITY_KEY
        self.table = AREA_DENSITY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL__LIST

    def get_conversion_factor(self, origin, destination):
        """

        :param origin:
        :param destination:
        :return:
        """
        return get_area_density_conversion_factor(origin, destination)

