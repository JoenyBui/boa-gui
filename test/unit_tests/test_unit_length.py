from unittest import TestCase
from peui.units import length

__author__ = 'jbui'


class TestLength(TestCase):

    def setUp(self):
        pass

    def test_km(self):
        self.assertEqual(round(length.get_length_conversion_factor('km', 'm'), 5), 1000)

    def test_cm(self):
        self.assertEqual(round(length.get_length_conversion_factor('cm', 'm'), 5), 0.01)

    def test_mm(self):
        self.assertEqual(round(length.get_length_conversion_factor('mm', 'm'), 5), 0.001)

    def test_in(self):
        self.assertEqual(round(length.get_length_conversion_factor('in', 'ft'), 5), round(1.0/12, 5))

    def test_ft(self):
        self.assertEqual(round(length.get_length_conversion_factor('ft', 'in'), 5), 12)

    def test_yd(self):
        self.assertEqual(round(length.get_length_conversion_factor('yd', 'in'), 5), 36)

