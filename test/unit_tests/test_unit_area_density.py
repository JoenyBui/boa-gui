from unittest import TestCase

import peui.units as units
from peui.units import area_density
from peui.units.area_density import AreaDensityUnit
from peui.units.mapper import UnitMap

__author__ = 'jbui'


class TestAreaDensity(TestCase):

    def setUp(self):
        self.um = UnitMap(src=None)

        self.um.value = 50
        self.um.value_unit = 'kg/m^2'

        self.um.multivalues = [1, 2, 3]

        self.um.map.update(dict(
            value=(units.UNIT_AREA_DENSITY_KEY, 'value_unit'),
            multivalues=(units.UNIT_AREA_DENSITY_KEY, 'value_unit')
        ))

    def test_kg_m2(self):
        self.assertEqual(self.um.get_value('value', 'kg/m2'), 50)

    def test_psi_ms2_in(self):
        self.assertAlmostEqual(self.um.get_value('value', 'psi-ms^2/in'), 184.1973674, 2)

    def test_lb_s2_in3(self):
        self.assertAlmostEqual(self.um.get_value('value', 'lb-s^2/in^3'), 0.00018497, 3)

    def test_lbm_in2(self):
        self.assertAlmostEqual(self.um.get_value('value', 'lbm/in^2'), 0.07111672, 3)

    def test_multivalues(self):
        mv = self.um.get_value('multivalues', 'lbm/in^2')

        for calc, answer in zip(mv, [0.0014223, 0.002844669, 0.004267]):
            self.assertAlmostEqual(calc, answer, 3)
