from base import BaseUnitTest

from peui.units.charge import ChargeUnit

__author__ = 'jbui'


class TestTNT(BaseUnitTest):

    def setUp(self):
        self.unit = ChargeUnit()

        self.magnitude = 1.618
        self.magnitude_unit = 'tnt'

    def test_anfo(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'ANFO')*self.magnitude, 2.651427e-5)

    def test_a3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Composition A-3')*self.magnitude, 2.651427e-5)

    def test_b(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Composition B')*self.magnitude, 2.651427e-5)

    def test_cyclotol(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Cyclotol')*self.magnitude, 2.651427e-5)

    def test_hbx1(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'HBX-1')*self.magnitude, 2.651427e-5)

    def test_hbx3(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'HBX-3')*self.magnitude, 2.651427e-5)

    def test_h6(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'H-6')*self.magnitude, 2.651427e-5)

    def test_minol(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Minoi II')*self.magnitude, 2.651427e-5)

    def test_octol(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'octol')*self.magnitude, 2.651427e-5)

    def test_pbx_9404(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'PBX-9404')*self.magnitude, 2.651427e-5)

    def test_pbx_9010(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'PBX-9010')*self.magnitude, 2.651427e-5)

    def test_petn(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'PETN')*self.magnitude, 2.651427e-5)

    def test_pentolite(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Pentolite')*self.magnitude, 2.651427e-5)

    def test_picratol(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Picratol')*self.magnitude, 2.651427e-5)

    def test_tetryl(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Tetryl')*self.magnitude, 2.651427e-5)

    def test_tetrytol(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'Tetrytol')*self.magnitude, 2.651427e-5)

    def test_tnetb(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'TNETB')*self.magnitude, 2.651427e-5)

    def test_tritonal(self):
        self.assertTolerance(self.unit.get_conversion_factor(self.magnitude_unit, 'TRITONAL')*self.magnitude, 2.651427e-5)

