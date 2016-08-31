from .acceleration import AccelerationUnit
from .angle import AngleUnit
from .area import AreaUnit
from .area_density import AreaDensityUnit
from .charge import ChargeUnit
from .density import DensityUnit
from .force import ForceUnit
from .inertia import InertiaUnit
from .length import LengthUnit
from .linear_pressure import LinearPressureUnit
from .linear_density import LinearDensityUnit
from .mass import MassUnit
from .pressure import PressureUnit
from .specific_weight import SpecificWeightUnit
from .time import TimeUnit
from .tnt import TntUnit
from .torque import TorqueUnit
from .velocity import VelocityUnit
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
        self.units.append(AccelerationUnit())
        self.units.append(AngleUnit())
        self.units.append(AreaUnit())
        self.units.append(AreaDensityUnit())
        self.units.append(ChargeUnit())
        self.units.append(DensityUnit())
        self.units.append(ForceUnit())
        self.units.append(InertiaUnit())
        self.units.append(LengthUnit())
        self.units.append(LinearPressureUnit())
        self.units.append(LinearDensityUnit())
        self.units.append(MassUnit())
        self.units.append(PressureUnit())
        self.units.append(SpecificWeightUnit())
        self.units.append(TimeUnit())
        self.units.append(TntUnit())
        self.units.append(TorqueUnit())
        self.units.append(VelocityUnit())
        self.units.append(VolumeUnit())

    def get_value(self, name, unit=None):
        """
        Return the converted unit value.

        :param name: key of the unit to return
        :param unit: unit to convert the value to
        """
        if self.src:
            keys = self.__dict__[self.src]
        else:
            keys = self.__dict__

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
                    if value is None or keys[base_unit] is None:
                        return None
                    else:
                        if isinstance(value, list):
                            return map(lambda x: x*obj.get_conversion_factor(keys[base_unit], unit), value)
                        else:
                            return value * obj.get_conversion_factor(keys[base_unit], unit)

    def get_conversion_factor(self, utype, origin, destination):
        """
        Get conversion factor for the unit type

        :param utype: unit key name
        :param origin: original unit
        :param destination: destination unit
        :return:
        """

        for obj in self.units:
            if obj.key == utype:
                return obj.get_conversion_factor(origin, destination)

        return None

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
