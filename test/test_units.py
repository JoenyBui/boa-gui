import pytest

from peui.units import length, mass, pressure, charge

__author__ = 'jbui'


class TestLength():

    def test_feet(self):
        assert round(length.get_length_conversion_factor('ft', 'in'), 4) == 12.0
        assert round(length.get_length_conversion_factor('ft.', 'yd'), 4) == 0.3333
        assert round(length.get_length_conversion_factor('meter', 'feet'), 4) == 3.2808

    def test_inches(self):
        assert length.get_length_conversion_factor('inch', 'ft') == 1.0/12.0
        assert length.get_length_conversion_factor('in', 'yard') == 1.0/36.0
        assert length.get_length_conversion_factor('in.', 'm') == 0.0254

    def test_yards(self):
        assert round(length.get_length_conversion_factor('yard', 'ft'), 2) == 3.0





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
