from unittest import TestCase
from peui.units import area_density

__author__ = 'jbui'


class TestForce(TestCase):

    def setUp(self):
        pass

    def test_psi_ms2_in(self):
        self.assertEqual(round(area_density.get_area_density_conversion_factor('psi-ms^2/in', 'kg/m2'), 10), 8.4368e-3)
