from unittest import TestCase
from boaui.units import length
from boaui.units.length import LengthUnit

from base import BaseUnitTest

__author__ = 'Joeny'


class TestLength(BaseUnitTest):

    def setUp(self):
        self.unit = LengthUnit()

        self.golden_ratio = 1.618
        self.golden_ratio_unit = 'yard'

    def test_meter(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'm')*self.golden_ratio, 1.4794992)

    def test_km(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'km')*self.golden_ratio, 0.0014794992)

    def test_cm(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'cm')*self.golden_ratio, 147.94992)

    def test_mm(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'mm')*self.golden_ratio, 1479.4992)

    def test_in(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'in')*self.golden_ratio, 58.248)

    def test_ft(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'ft')*self.golden_ratio, 4.854)

    def test_yd(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.golden_ratio_unit, 'yd')*self.golden_ratio, 1.618)

