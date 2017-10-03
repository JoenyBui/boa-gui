from unittest import TestCase
from boaui.units.specific_weight import SpecificWeightUnit

from base import BaseUnitTest

__author__ = 'Joeny'


class TestSpecificWeight(BaseUnitTest):

    def setUp(self):
        self.unit = SpecificWeightUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'kPa/mm'

    def test_kPa_mm(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kPa/mm')*self.magnitude, 1.618)

    def test_psi_in(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'psi/in')*self.magnitude, 5.9606)

