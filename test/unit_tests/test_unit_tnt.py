from base import BaseUnitTest

from boaui.units.tnt import TntUnit

__author__ = 'Joeny'


class TestTNT(BaseUnitTest):

    def setUp(self):
        self.unit = TntUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'kiloton'

    def test_ton(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ton')*self.magnitude, 1618)

    def test_kiloton(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kiloton')*self.magnitude, 1.618)

    def test_kilogram(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kg')*self.magnitude, 1467825)

    def test_lb(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'lb')*self.magnitude, 3236000)
