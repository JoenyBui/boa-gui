from unittest import TestCase
from peui.units import density

__author__ = 'jbui'


class TestDensity(TestCase):

    def setUp(self):
        pass

    def test_kg_m3(self):
        self.assertEqual(round(density.get_density_conversion_factor('kg/m3', 'g/cm3'), 5), 0.001)

    def test_lb_ft3(self):
        self.assertEqual(round(density.get_density_conversion_factor('lb/ft3', 'lb/in3'), 5), round(1.0/12**3, 5))

    def test_lb_in3(self):
        self.assertEqual(round(density.get_density_conversion_factor('lb/in3', 'lb/ft3'), 0), 12**3)
