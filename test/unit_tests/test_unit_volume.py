from unittest import TestCase
from peui.units import volume

__author__ = 'jbui'


class TestVolume(TestCase):

    def setUp(self):
        pass

    def test_mm3(self):
        self.assertEqual(round(volume.get_volume_conversion_factor('mm3', 'm3'), 10), 0.001**3)

    def test_ft3(self):
        self.assertEqual(round(volume.get_volume_conversion_factor('ft3', 'mm3'), 5), round(304.8**3, 5))

    def test_in3(self):
        self.assertEqual(round(volume.get_volume_conversion_factor('in3', 'mm3'), 3), 25.4**3)
