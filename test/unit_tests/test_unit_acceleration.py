from unittest import TestCase

from boaui.units import acceleration
from boaui.units.acceleration import AccelerationUnit

from base import BaseUnitTest

__author__ = 'Joeny'


class TestAcceleration(BaseUnitTest):

    def setUp(self):
        self.unit = AccelerationUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'ft/s^2'

    def test_m2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'm/s^2')*self.magnitude, 1618)

    def test_mm2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'mm/s^2')*self.magnitude, 1618000)

    def test_ft_s2(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ft/s^2')*self.magnitude, 5308)
