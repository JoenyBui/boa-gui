from unittest import TestCase
from boaui.units.inertia import InertiaUnit

from base import BaseUnitTest

__author__ = 'Joeny'


class TestInertia(BaseUnitTest):

    def setUp(self):
        self.unit = InertiaUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'm^4'

    def test_m4(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'm^4')*self.magnitude, 1.618)

    def test_mm4(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'mm^4')*self.magnitude, 1618000000000)

    def test_ft4(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ft^4')*self.magnitude, 187.46434)

    def test_in4(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'in^4')*self.magnitude, 3887260.55)
