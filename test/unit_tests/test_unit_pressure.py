from base import BaseUnitTest

from unittest import TestCase
from boaui.units.pressure import PressureUnit

__author__ = 'Joeny'


class TestPressure(BaseUnitTest):

    def setUp(self):
        self.unit = PressureUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'psi'

    def test_kPa(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kPa')*self.magnitude, 11.155)

    def test_MPa(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'MPa')*self.magnitude, 0.01115571)

    def test_psi(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'psi')*self.magnitude, 1.618)

    def test_ksi(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ksi')*self.magnitude, 0.001618)

    def test_psf(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'psf')*self.magnitude, 232.992)
