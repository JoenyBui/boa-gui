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


class AreaDensityUnit(Unit):

    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_AREA_DENSITY_KEY

