from unittest import TestCase
from peui.units import tnt

__author__ = 'jbui'


class TestTNT(TestCase):

    def setUp(self):
        pass

    def test_anfo(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('ANFO', 'TNT'), 5), 1000)

    def test_a3(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Composition A-3', 'TNT'), 5), 0.01)

    def test_b(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Composition B', 'TNT'), 5), 0.001)

    def test_cyclotol(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Cyclotol (70/30)', 'TNT'), 5), 12)

    def test_hbx1(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('HBX-1', 'TNT'), 5), 36)

    def test_hbx3(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('HBX-3', 'TNT'), 5), 0.01)

    def test_h6(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('H-6', 'TNT'), 5), 0.001)

    def test_minol(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Minoi II', 'TNT'), 5), 5)

    def test_octol(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Octol (70/30)', 'TNT'), 5), 12)

    def test_pbx_9404(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('PBX-9404', 'TNT'), 5), 36)

    def test_pbx_9010(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('PBX-9010', 'TNT'), 5), 0.01)

    def test_petn(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('PETN', 'TNT'), 5), 0.001)

    def test_pentolite(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Pentolite', 'TNT'), 5), 5)

    def test_picratol(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Picratol', 'TNT'), 5), 12)

    def test_tetryl(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Tetryl', 'TNT'), 5), 36)

    def test_tetrytol(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('Tetrytol', 'TNT'), 5), 5)

    def test_tnetb(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('TNETB', 'TNT'), 5), 12)

    def test_tritonal(self):
        self.assertEqual(round(tnt.get_tnt_conversion_factor('TRITONAL', 'TNT'), 5), 36)

