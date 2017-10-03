from base import BaseUnitTest

from boaui.units.velocity import VelocityUnit

__author__ = 'Joeny'


class TestVelocity(BaseUnitTest):

    def setUp(self):
        self.unit = VelocityUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'km/h'

    def test_m_s(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'm/s')*self.magnitude, 0.44944444)

    def test_mm_ms(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'mm/ms')*self.magnitude, 0.4494444)

    def test_ft_s(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ft/s')*self.magnitude, 1.4745553)

    def test_km_h(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'km/h')*self.magnitude, 1.618)

    def test_in_s(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'in/s')*self.magnitude, 17.694663)

    def test_mph(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'mph')*self.magnitude, 1.0053785790981)
