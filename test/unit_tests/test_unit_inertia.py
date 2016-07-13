from unittest import TestCase
from peui.units import inertia

__author__ = 'jbui'


class TestInertia(TestCase):

    def setUp(self):
        pass

    def test_mm4(self):
        self.assertEqual(round(inertia.get_inertia_conversion_factor('mm4', 'm4'), 13), 1e-12)

    def test_ft4(self):
        self.assertEqual(round(inertia.get_inertia_conversion_factor('ft4', 'in4'), 5), 12**4)

    def test_in4(self):
        self.assertEqual(round(inertia.get_inertia_conversion_factor('in4', 'ft4'), 10), round(1.0/12**4, 10))
