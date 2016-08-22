from unittest import TestCase
from peui.units import torque

__author__ = 'jbui'


class TestTorque(TestCase):

    def setUp(self):
        pass

    def test_n_mm(self):
        self.assertEqual(round(torque.get_torque_conversion_factor('N-mm', 'N-m'), 5), 0.001)

    def test_lb_in(self):
        self.assertEqual(round(torque.get_torque_conversion_factor('lb-in', 'N-m'), 3), round(9.8066/2.2046*39.37, 3))

    def test_kip_in(self):
        self.assertEqual(round(torque.get_torque_conversion_factor('kip-in', 'lb-in'), 5), 1000)
