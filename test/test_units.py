import pytest

from peui.units import length, mass, pressure, charge

__author__ = 'jbui'


class TestLength():

    def test_feet(self):
        assert length.get_length_conversion_factor('ft', 'in') == 1.0/12.0
        assert length.get_length_conversion_factor('ft.', 'yd') == 3.0
        assert length.get_length_conversion_factor('meter', 'feet') == 0.3048

    def test_inches(self):
        assert round(length.get_length_conversion_factor('inch', 'ft'), 4) == 12.0
        assert round(length.get_length_conversion_factor('in', 'yard'), 4) == 36.0
        assert round(length.get_length_conversion_factor('in.', 'm'), 4) == 39.3701

    def test_yards(self):
        assert round(length.get_length_conversion_factor('yard', 'ft'), 2) == 0.33


class TestMass():

    def test_kg(self):
        assert round(mass.get_mass_conversion_factor('kg', 'g'), 5) == 1000

    def test_lbm(self):
        assert round(mass.get_mass_conversion_factor('lbm', 'g'), 3) == 453.592


class TestPressure():

    def test_psi(self):
        assert round(pressure.get_pressure_conversion_factor('psi', 'Pa'), 2) == 6894.74

    def test_ksi(self):
        assert float('%.3e'%round(pressure.get_pressure_conversion_factor('ksi', 'Pa'), 4)) == 6.895e+6


def TestCharge():

    def test_anfo():
        pass

    def test_tritonal():
        pass

    # def test_atm(self):
    #     assert round(pressure.get_pressure_conversion_factor('atm', 'Pa'), 4) == 101325
