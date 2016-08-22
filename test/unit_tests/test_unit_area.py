from unittest import TestCase
from peui.units import area

__author__ = 'jbui'


class TestArea(TestCase):

    def setUp(self):
        pass

    def test_cm(self):
        self.assertEqual(round(area.get_area_conversion_factor('cm2', 'm2'), 5), 0.0001)

    def test_km(self):
        self.assertEqual(round(area.get_area_conversion_factor('km2', 'm2'), 3), 1e6)

    def test_in(self):
        self.assertEqual(round(area.get_area_conversion_factor('in2', 'ft2'), 5), round(1.0/144, 5))

    def test_ft(self):
        self.assertEqual(round(area.get_area_conversion_factor('ft2', 'in2'), 3), 144)

    def test_yd(self):
        self.assertEqual(round(area.get_area_conversion_factor('yd2', 'in2'), 0), 36**2)
