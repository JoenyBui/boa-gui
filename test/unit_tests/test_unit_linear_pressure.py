from peui.units.linear_pressure import LinearPressureUnit

from peui.units import linear_pressure

from base import BaseUnitTest

__author__ = 'jbui'


class TestLinearPressure(BaseUnitTest):

    def setUp(self):
        self.unit = LinearPressureUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'plf'

    def test_plf(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'plf')*self.magnitude, 1.618)

    def test_pli(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'pli')*self.magnitude, 0.1348333)

    def test_klf(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'klf')*self.magnitude, 0.001618)
