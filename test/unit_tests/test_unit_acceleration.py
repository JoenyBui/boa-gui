from unittest import TestCase
from peui.units import acceleration

__author__ = 'jbui'


class TestAcceleration(TestCase):

    def setUp(self):
        pass

    def test_gal(self):
        self.assertEqual(round(acceleration.get_acceleration_conversion_factor('ft/s2', 'm/s2'), 5), 0.3048)

    def test_ft_s2(self):
        self.assertEqual(round(acceleration.get_acceleration_conversion_factor('gal', 'm/s2'), 3), 0.01)
