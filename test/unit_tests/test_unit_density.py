from unittest import TestCase
from boaui.units.density import DensityUnit

from base import BaseUnitTest

__author__ = 'Joeny'


class TestDensity(BaseUnitTest):

    def setUp(self):
        self.unit = DensityUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'kg/m^3'

    def test_kg_m3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kg/m^3')*self.magnitude, 1.618)

    def test_g_cm3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'g/cm^3')*self.magnitude, 0.001618)

    def test_lb_ft3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'lb/ft^3')*self.magnitude, 0.10100844)

    def test_lb_in3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'lb/in^3')*self.magnitude, 0.000058454)
