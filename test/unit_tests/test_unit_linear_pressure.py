from unittest import TestCase
from peui.units import linear_pressure

__author__ = 'jbui'


class TestLinearPressure(TestCase):

    def setUp(self):
        pass

    def test_plf(self):
        self.assertEqual(round(linear_pressure.get_linear_pressure_conversion_factor('plf', 'lb/in'), 5), round(1.0/12, 5))

    def test_pli(self):
        self.assertEqual(round(linear_pressure.get_linear_pressure_conversion_factor('lb/in', 'lb/ft'), 3), 12.0)

    def test_klf(self):
        self.assertEqual(round(linear_pressure.get_linear_pressure_conversion_factor('klf', 'lb/in'), 3), round(1000.0/12, 3))
