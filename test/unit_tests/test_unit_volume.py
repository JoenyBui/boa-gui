from base import BaseUnitTest

from boaui.units.volume import VolumeUnit

__author__ = 'Joeny'


class TestVolume(BaseUnitTest):

    def setUp(self):
        self.unit = VolumeUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'in^3'

    def test_m3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'm^3')*self.magnitude, 2.651427e-5)

    def test_mm3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'mm^3')*self.magnitude, 26514.27)

    def test_ft3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ft^3')*self.magnitude, 0.00093634259)

    def test_in3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'in^3')*self.magnitude, 1.618)
