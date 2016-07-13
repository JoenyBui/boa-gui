from unittest import TestCase
from peui.units import tnt

__author__ = 'jbui'


class TestTNT(TestCase):

    def setUp(self):
        pass

    def test_ton(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('ton', 'kilogram'), 3), 907.186)

    def test_kiloton(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('kiloton', 'ton'), 5), 1e3)
