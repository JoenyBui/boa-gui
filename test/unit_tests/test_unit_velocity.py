from unittest import TestCase
from peui.units import velocity

__author__ = 'jbui'


class TestVelocity(TestCase):

    def setUp(self):
        pass

    def test_mm_ms(self):
        self.assertEqual(round(velocity.get_velocity_conversion_factor('mm/ms', 'm/s'), 5), 1)

    def test_ft_s(self):
        self.assertEqual(round(velocity.get_velocity_conversion_factor('ft/s', 'm/s'), 5), 0.3048)

    def test_km_h(self):
        self.assertEqual(round(velocity.get_velocity_conversion_factor('km/h', 'm/s'), 5), round(1000.0/3600, 5))
