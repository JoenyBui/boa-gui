from unittest import TestCase
from peui.units import force

__author__ = 'jbui'


class TestForce(TestCase):

    def setUp(self):
        pass

    def test_kN(self):
        self.assertEqual(round(force.get_force_conversion_factor('kN', 'N'), 5), 1000)

    def test_lb(self):
        self.assertEqual(round(force.get_force_conversion_factor('lb', 'ton'), 5), 0.0005)

    def test_ton(self):
        self.assertEqual(round(force.get_force_conversion_factor('ton', 'lb'), 2), 2000)

    def test_kiloton(self):
        self.assertEqual(round(force.get_force_conversion_factor('kiloton', 'lb'), 2), 2e6)

    def test_kip(self):
        self.assertEqual(round(force.get_force_conversion_factor('kip', 'lb'), 3), 1000)
