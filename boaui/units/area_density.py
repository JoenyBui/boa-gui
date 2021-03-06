"""
**area density**

Unity Value = kg/m^2

English Unit Value = psi-ms^2/in


psi-ms^2/in --> lbm*ft*ms2/(s^2 * in^3) --> lbm*12*in*(0.001^2)*s^2/(s^2 * in^3) --> 12e-6*lbm/in^2 --> 12e-6*0.4536*kg/(0.0254^2 * m^2) --> 8.4368e-3*kg/m^2
                                                    |            |____|      |
                                                    |________________________|

"""
from . import Unit, UNIT_AREA_DENSITY_KEY

__author__ = 'Joeny'

FACTOR_AREA_DENSITY_KILOGRAM_M2 = 1.0
FACTOR_AREA_DENSITY_LBM_IN2 = 0.001422334
FACTOR_AREA_DENSITY_PSI_MS2_IN = 3.683957707
FACTOR_AREA_DENSITY_PSI_S2_IN = 3.683957707/(1000**2)
FACTOR_AREA_DENSITY_LB_S2_OVER_IN3 = 0.000003684
FACTOR_AREA_DENSITY_LB_MS2_OVER_IN3 = 0.000003684*(1000**2)
FACTOR_AREA_DENSITY_PSF = 0.20481614401362

AREA_DENSITY_KEY = {
    'kg/m2': FACTOR_AREA_DENSITY_KILOGRAM_M2,
    'kg/m^2': FACTOR_AREA_DENSITY_KILOGRAM_M2,
    'psi-ms^2/in': FACTOR_AREA_DENSITY_PSI_MS2_IN,
    'psi-s^2/in': FACTOR_AREA_DENSITY_PSI_S2_IN,
    'lb-s^2/in^3': FACTOR_AREA_DENSITY_LB_S2_OVER_IN3,
    'lb*s^2/in^3': FACTOR_AREA_DENSITY_LB_S2_OVER_IN3,
    'lb*ms^2/in^3': FACTOR_AREA_DENSITY_LB_MS2_OVER_IN3,
    'lbm/in^2': FACTOR_AREA_DENSITY_LBM_IN2,
    'lb/in^2': FACTOR_AREA_DENSITY_LBM_IN2,
    'psf': FACTOR_AREA_DENSITY_PSF
}

DEFAULT_AREA_LIST = [
    'kg/m2',
    'psi-ms^2/in',
    'psi-s^2/in',
    'lb-s^2/in^3',
    'lb-ms^2/in^3'
]

DEFAULT_IMPERIAL__LIST = [
    'psi-ms^2/in'
]

DEFAULT_METRIC_LIST = [
    'kg/m^2',
]


def get_area_density_conversion_factor(origin, destination):
    """
    Get area density conversion factor

    :param origin:
    :param destination:
    :return:
    """
    origin_factor = AREA_DENSITY_KEY.get(origin)
    destination_factor = AREA_DENSITY_KEY.get(destination)

    return float(destination_factor) / float(origin_factor)


class AreaDensityUnit(Unit):
    """
    **Area Density Unit**

    """
    def __init__(self, *args, **kwargs):
        """
        Constructor

        :param args:
        :param kwargs:
        :return:
        """
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_AREA_DENSITY_KEY
        self.table = AREA_DENSITY_KEY

        self.metric_list = DEFAULT_METRIC_LIST
        self.imperial_list = DEFAULT_IMPERIAL__LIST
