from unittest import TestCase
from peui.units.time import TimeUnit

from base import BaseUnitTest

__author__ = 'jbui'


class TestTime(BaseUnitTest):

    def setUp(self):
        self.unit = TimeUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'ms'

    def test_ms(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ms')*self.magnitude, 1.618)

    def test_s(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 's')*self.magnitude, 0.001618)
