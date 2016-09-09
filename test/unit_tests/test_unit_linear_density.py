from unittest import TestCase
from peui.units.linear_density import LinearDensityUnit

from base import BaseUnitTest

__author__ = 'jbui'


class TestLinearDensity(TestCase):

    def setUp(self):
        self.unit = LinearDensityUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'plf'
