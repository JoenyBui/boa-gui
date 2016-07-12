from unittest import TestCase
from peui.units import mass

__author__ = 'jbui'


class TestMass(TestCase):

    def setUp(self):
        pass

    def test_kg(self):
        self.assertEqual(round(mass.get_mass_conversion_factor('kg', 'g'), 5), 1000)

    def test_lbm(self):
        self.assertEqual(round(mass.get_mass_conversion_factor('lbm', 'g'), 3), 453.592)
