from unittest import TestCase
from peui.units import area

from peui.units.area import AreaUnit

from base import BaseUnitTest

__author__ = 'jbui'


class TestArea(BaseUnitTest):

    def setUp(self):
        self.unit = AreaUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'ft^2'

    def test_km2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'km^2')*self.magnitude, 1.503171E-7)

    def test_m2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'm^2')*self.magnitude, 0.15031712)

    def test_in2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'in^2')*self.magnitude, 232.992)

    def test_ft2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ft^2')*self.magnitude, 1.618)

    def test_yd2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'yd^2')*self.magnitude, 0.17977778)
