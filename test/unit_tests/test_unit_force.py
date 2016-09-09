from unittest import TestCase
from peui.units.force import ForceUnit

from base import BaseUnitTest

__author__ = 'jbui'


class TestForce(BaseUnitTest):

    def setUp(self):
        self.unit = ForceUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'ton'

    def test_N(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'N')*self.magnitude, 14394.445)

    def test_kN(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kN')*self.magnitude, 14.394445147)

    def test_lb(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'lb')*self.magnitude, 3236)

    def test_ton(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ton')*self.magnitude, 1.618)

    def test_kiloton(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kiloton')*self.magnitude, 0.001618)

    def test_kip(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kip')*self.magnitude, 3.236)
