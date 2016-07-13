from unittest import TestCase
from peui.units import linear_density

__author__ = 'jbui'


class TestLinearDensity(TestCase):

    def setUp(self):
        pass

    def test_plf(self):
        self.assertEqual(round(linear_density.get_linear_density_conversion_factor('plf', 'klf'), 3), 0.454)

    def test_klf(self):
        self.assertEqual(round(linear_density.get_linear_density_conversion_factor('klf', 'plf'), 3), 2.205)
