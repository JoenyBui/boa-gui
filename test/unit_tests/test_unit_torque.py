from base import BaseUnitTest

from peui.units.torque import TorqueUnit

__author__ = 'jbui'


class TestTorque(BaseUnitTest):

    def setUp(self):
        self.unit = TorqueUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'kip-in'

    def test_n_mm(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'N-m')*self.magnitude, 182.809)

    def test_lb_in(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'lb-in')*self.magnitude, 1618)

    def test_kip_in(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'kip-in')*self.magnitude, 1.618)
