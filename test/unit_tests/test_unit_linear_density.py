from unittest import TestCase
from peui.units.linear_density import LinearDensityUnit

from base import BaseUnitTest

__author__ = 'jbui'


class TestLinearDensity(BaseUnitTest):

    def setUp(self):
        self.unit = LinearDensityUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'plf'

    def test_kg_m(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kg/m')*self.magnitude, 2.4078493)

    def test_g_m(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'g/m')*self.magnitude, 2407.8493)

    def test_plf(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'plf')*self.magnitude, 1.618)

