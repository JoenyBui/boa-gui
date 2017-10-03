from unittest import TestCase
from boaui.units import mass

from boaui.units.mass import MassUnit

from base import BaseUnitTest

__author__ = 'Joeny'


class TestMass(BaseUnitTest):

    def setUp(self):
        self.unit = MassUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'kg'

    def test_kg(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kg')*self.magnitude, 1.618)

    def test_lb(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'lb')*self.magnitude, 3.5670794)

    def test_ton(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ton')*self.magnitude, 0.0017835397)
