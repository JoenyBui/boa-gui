from .area import AreaUnit
from .charge import ChargeUnit
from .density import DensityUnit
from .inertia import InertiaUnit
from .length import LengthUnit
from .mass import MassUnit
from .pressure import PressureUnit
from .tnt import TntUnit
from .torque import TorqueUnit
from .volume import VolumeUnit


class UnitMap(object):
    """
    Map the unit value with the text.

    """
    def __init__(self, src='keys'):
        """

        :param src:
        """
        self.map = {}
        self.src = src

        self.units = []

        self.add_default_unit()

    def add_default_unit(self):
        """
        Add default unit values.

        """
        self.units.append(AreaUnit())
        self.units.append(ChargeUnit())
        self.units.append(DensityUnit())
        self.units.append(InertiaUnit())
        self.units.append(LengthUnit())
        self.units.append(MassUnit())
        self.units.append(PressureUnit())
        self.units.append(TntUnit())
        self.units.append(TorqueUnit())
        self.units.append(VolumeUnit())

    def get_value(self, name, unit=None):
        """
        Return the converted unit value.

        :param name: key of the unit to return
        :param unit: unit to convert the value to
        """
        keys = self.__dict__[self.src]

        # Get the magnitude value.
        value = keys[name]

        # Utype and Base Unit
        if self.map.get(name):
            utype, base_unit = self.map.get(name)
        else:
            utype = None

        if utype is None:
            return keys[name]
        else:
            for obj in self.units:
                if obj.key == utype:
                    return value * obj.get_conversion_factor(keys[base_unit], unit)

    def set_value(self, name, value, unit):
        """
        Set the pair value for the type given value and unit.

        :param name:
        :param value:
        :param unit:
        """
        keys = self.__dict__(self.src)

        utype, base_unit = self.map.get(name)

        keys[name] = value
        keys[base_unit] = unit
