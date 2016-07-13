from unittest import TestCase
from peui.units import pressure

__author__ = 'jbui'


class TestPressure(TestCase):

    def setUp(self):
        pass

    def test_kPa(self):
        self.assertEqual(round(pressure.get_pressure_conversion_factor('kPa', 'Pa'), 5), 1000)

    def test_MPa(self):
        self.assertEqual(round(pressure.get_pressure_conversion_factor('MPa', 'Pa'), 5), 1e6)

    def test_psi(self):
        self.assertEqual(round(pressure.get_pressure_conversion_factor('psi', 'Pa'), 2), 6894.76)

    def test_ksi(self):
        self.assertEqual(round(pressure.get_pressure_conversion_factor('ksi', 'psi'), 2), 1e3)

    def test_psf(self):
        self.assertEqual(round(pressure.get_pressure_conversion_factor('psf', 'psi'), 5), round(1.0/12**2, 5))