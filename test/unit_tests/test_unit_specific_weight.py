from unittest import TestCase
from peui.units import specific_weight

__author__ = 'jbui'


class TestForce(TestCase):

    def setUp(self):
        pass

    def test_psi_in(self):
        self.assertEqual(round(specific_weight.get_specific_weight_conversion_factor('psi/in', 'kPa/mm'), 5), 0.27145)
