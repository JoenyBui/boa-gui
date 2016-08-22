import os
import sys
import re
import types

import wx

from pecutil.refmt import get_number_fmt, parse_number
from pecutil.types import isFloat

from peui import units
from peui.units import area, charge, length, density, torque, volume, inertia, mass, pressure, tnt
from pecutil.types import isFloat

from . import SmartToolTip
from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class FloatSmartBox(SmartTextBox):
    """
    Float Smart Box.

    """
    def __init__(self, parent, signs=False, decimal=True, exponential=False, normal=None, format_error=None,
                 range_error=None, key_up=None, message=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param signs:
        :param decimal:
        :param exponential:
        :param normal:
        :param format_error:
        :param range_error:
        :param key_up: event handler
        :param args:
        :param kwargs:
        """
        SmartTextBox.__init__(self, parent, key_up=key_up, message=message, *args, **kwargs)

        # self.signs = kwargs.get('signs', False)
        # self.decimal = kwargs.get('decimal', True)
        # self.exponential = kwargs.get('exponential', False)

        self.signs = signs
        self.decimal = decimal
        self.exponential = exponential

        self.fmt = get_number_fmt(signs=self.signs, decimal=self.decimal, exponential=self.exponential)

        # self.Bind(wx.EVT_CHAR, self.on_key_char, self)
        # self.Bind(wx.EVT_CHAR_HOOK, self.on_key_char_hook, self)
        if key_up:
            self.Bind(wx.EVT_KEY_UP, key_up, self)

        # self.Bind(wx.EVT_KEY_UP, self.on_key_up, self)
        # self.Bind(wx.EVT_KEY_DOWN, self.on_key_down, self)
        self.Bind(wx.EVT_TEXT, self.on_text, self)

        self.color_normal = kwargs.get('normal', (255, 255, 255))
        self.color_format_error = kwargs.get('format_error', (228, 115, 115))
        self.color_range_error = kwargs.get('range_error', (244, 67, 54))

        self._validator = FloatRangeValidator(signs=signs, decimal=decimal, exponential=exponential)
        self.SetValidator(self._validator)

    def on_text(self, event=None):
        """
        Check Validity of the data.

        :param event:
        """
        val = self.GetValue()
        values, src = parse_number(val, self.fmt)

        if val:
            if len(src) > 0:
                if src[0] == val:
                    self.set_normal_color()
                else:
                    self.set_format_error_color()
            else:
                self.set_format_error_color()
        else:
            self.set_normal_color()

        self.Refresh()

        event.Skip()

    def on_key_up(self, event=None):
        """

        :param event:
        """
        event.Skip()

    def on_key_down(self, event=None):
        """

        :param event:
        """
        event.Skip()

    def on_key_char(self, event=None):
        """

        :param event:
        """
        kc = event.GetKeyCode()
        event.Skip()

    def on_key_char_hook(self, event=None):
        """

        :param event:
        """
        kc = event.GetKeyCode()
        event.Skip()

    def set_normal_color(self):
        """
        Set normal color.

        """
        self.SetBackgroundColour(self.color_normal)
        self.Refresh()

    def set_format_error_color(self):
        """
        Set format error color.

        """
        self.SetBackgroundColour(self.color_format_error)
        self.Refresh()

    def set_range_error_color(self):
        """
        Set range error color.

        """
        self.SetBackgroundColour(self.color_range_error)
        self.Refresh()

    def get_value(self, key=None):
        """
        Grab the value from the textbox

        :param key:
        :return:
        """
        val = SmartTextBox.get_value(self, key=key)

        if key is None:
            if isFloat(val):
                return float(val)
            else:
                return None

        return val


class FloatInputLayout(SmartInputLayout):
    """
    Float Textbox Layout Horizontal Layout.

    """
    def __init__(self, parent, value=None, unit=None, unit_list=None, unit_system=None, type=None, max=None, min=None, layout=None,
                 textbox=None, postbox=None, *args, **kwargs):
        """
        Constructor.

        :param parent: parent panel or frame
        :param value: textbox value
        :param unit:
        :param unit_system:
        :param type:
        :param max: maximum value for the textbox
        :param min: minimum value for the textbox
        :param layout:
        :param textbox:
        :param postbox:
        :param args:
        :param kwargs:
        :return:
        """
        SmartInputLayout.__init__(self, parent, max=max, min=min, layout=layout, *args, **kwargs)

        #  Add in Textbox.
        if textbox:
            self.textbox = textbox
        else:
            self.textbox = FloatSmartBox(parent)

        if value:
            self.textbox.Value = str(value)

        if postbox:
            # Add in Unit System.
            self.postbox = postbox
            # self.postbox.SetSize(self.layout.get_size(self.INDEX_POSTBOX))

            self.postbox.unit_system = unit_system

            if type:
                self.type = type

                if type == units.UNIT_ACCELERATION_KEY:
                    self.postbox.activate_acceleration(unit_list=unit_list)
                elif type == units.UNIT_ANGLE_KEY:
                    self.postbox.activate_angle(unit_list=unit_list)
                elif type == units.UNIT_AREA_DENSITY_KEY:
                    self.postbox.activate_area_density(unit_list=unit_list)
                elif type == units.UNIT_AREA_KEY:
                    self.postbox.activate_area(unit_list=unit_list)
                elif type == units.UNIT_CHARGE_KEY:
                    self.postbox.activate_charge(unit_list=unit_list)
                elif type == units.UNIT_DENSITY_KEY:
                    self.postbox.activate_density(unit_list=unit_list)
                elif type == units.UNIT_FORCE_KEY:
                    self.postbox.activate_force(unit_list=unit_list)
                elif type == units.UNIT_INERTIA_KEY:
                    self.postbox.activate_inertia(unit_list=unit_list)
                elif type == units.UNIT_LENGTH_KEY:
                    self.postbox.activate_length(unit_list=unit_list)
                elif type == units.UNIT_LINEAR_DENSITY:
                    self.postbox.activate_linear_density(unit_list=unit_list)
                elif type == units.UNIT_LINEAR_PRESSURE:
                    self.postbox.activate_linear_pressure(unit_list=unit_list)
                elif type == units.UNIT_MASS_KEY:
                    self.postbox.activate_mass(unit_list=unit_list)
                elif type == units.UNIT_PRESSURE_KEY:
                    self.postbox.activate_pressure(unit_list=unit_list)
                elif type == units.UNIT_TIME_KEY:
                    self.postbox.activate_time(unit_list=unit_list)
                elif type == units.UNIT_TNT_KEY:
                    self.postbox.activate_tnt(unit_list=unit_list)
                elif type == units.UNIT_TORQUE_KEY:
                    self.postbox.activate_torque(unit_list=unit_list)
                elif type == units.UNIT_VELOCITY_KEY:
                    self.postbox.activate_velocity(unit_list=unit_list)
                elif type == units.UNIT_VOLUME_KEY:
                    self.postbox.activate_volume(unit_list=unit_list)

            if unit:
                if isinstance(unit, types.TupleType) or isinstance(unit, types.ListType):
                    if units.KEY_IMPERIAL == unit_system:
                        self.postbox.Value = unit[0]
                    elif units.KEY_METRIC == unit_system:
                        self.postbox.Value = unit[1]

                else:
                    self.postbox.Value = unit

        self.do_layout()

    def enable(self, enable=True):
        """
        Enable textbox and/or postbox.

        :return:
        """
        if self.textbox:
            self.textbox.Enable(enable=enable)

        if self.postbox:
            self.postbox.Enable(enable=enable)

    def disable(self):
        """
        Disable textbox and/or postbox.

        :return:
        """
        if self.textbox:
            self.textbox.Disable()

        if self.postbox:
            self.postbox.Disable()

    def set_value(self, value=None, post=None, label=None):
        """
        Set the components value.

        :param value: textbox.Value
        :param post: postbox.Value
        :param label: label.Label
        """
        if value is not None:
            self.textbox.Value = str(value)

        if post and self.postbox:
            self.postbox.Value = str(post)

        if label:
            self.label.Label = str(label)

    def get_value(self, destination_unit=None):
        """
        Return the value given destination unit.

        :param destination_unit: convert value to this unit
        :return: float
        """

        if self.postbox:
            original_unit = self.postbox.Value
            value = self.textbox.Value
            unit = self.postbox.unit

            if value == '' or unit is None:
                return None
            else:
                return float(value) * unit.get_conversion_factor(original_unit, destination_unit)
        else:
            if self.textbox.Value == '':
                return None
            else:
                return float(self.textbox.Value)

    def set_value_convert(self, original_unit, destination_unit):
        """
        Modified the textbox value given the set of conversion.

        :param original_unit:
        :param destination_unit:
        :return:
        """
        conversion_factor = 1.0
        if self.type == units.UNIT_AREA_KEY:
            conversion_factor = area.get_area_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_CHARGE_KEY:
            conversion_factor = charge.get_charge_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_LENGTH_KEY:
            conversion_factor = length.get_length_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_INERTIA_KEY:
            conversion_factor = inertia.get_inertia_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_MASS_KEY:
            conversion_factor = mass.get_mass_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_PRESSURE_KEY:
            conversion_factor = pressure.get_pressure_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_VOLUME_KEY:
            conversion_factor = volume.get_volume_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_DENSITY_KEY:
            conversion_factor = density.get_density_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_TORQUE_KEY:
            conversion_factor = torque.get_torque_conversion_factor(original_unit, destination_unit)

        self.textbox.Value = str(conversion_factor * float(self.textbox.Value))

    def value_convert(self, original_unit, destination_unit):
        """
        Return the converted value.

        :param original_unit: original unit value
        :param destination_unit: destination unit value
        :return:
        """
        conversion_factor = 1.0
        if self.type == units.UNIT_AREA_KEY:
            conversion_factor = area.get_area_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_CHARGE_KEY:
            conversion_factor = charge.get_charge_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_LENGTH_KEY:
            conversion_factor = length.get_length_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_INERTIA_KEY:
            conversion_factor = inertia.get_inertia_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_MASS_KEY:
            conversion_factor = mass.get_mass_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_PRESSURE_KEY:
            conversion_factor = pressure.get_pressure_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_VOLUME_KEY:
            conversion_factor = volume.get_volume_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_DENSITY_KEY:
            conversion_factor = density.get_density_conversion_factor(original_unit, destination_unit)
        elif self.type == units.UNIT_TORQUE_KEY:
            conversion_factor = torque.get_torque_conversion_factor(original_unit, destination_unit)

        return conversion_factor * float(self.textbox.Value)

    def validate(self):
        """
        Validate float box

        :return:
        """
        base_value = units.get_base_value(self.type, self.textbox.Value, self.postbox.Value)

        if self.min:
            base_min = units.get_base_value(self.type, self.min[0], self.min[1])

            if base_value < base_min:
                self.textbox.set_range_error_color()

                # error_tooltip = wx.ToolTip("Value is not below minimum.")
                # self.textbox.SetToolTip(error_tooltip)

                return False

        if self.max:
            base_max = units.get_base_value(self.type, self.max[0], self.max[1])

            if base_value > base_max:
                self.textbox.set_range_error_color()

                # error_tooltip = wx.ToolTip("Value is above maximum.")
                # self.textbox.SetToolTip(error_tooltip)

                return False

        self.textbox.set_normal_color()

        # if self.textbox.tooltip:
        #     self.textbox.SetToolTip(self.textbox.tooltip)

        return True


class FloatRangeValidator(wx.PyValidator):
    """
    Float Range Validator

    """
    def __init__(self, signs=False, decimal=True, exponential=False, min=None, max=None, *args, **kwargs):
        """

        :param kwargs:
        :return:
        """
        wx.PyValidator.__init__(self, *args, **kwargs)

        # self.signs = kwargs.get('signs', False)
        # self.decimal = kwargs.get('decimal', True)
        # self.exponential = kwargs.get('exponential', False)
        self.signs = signs
        self.decimal = decimal
        self.exponential = exponential

        self.fmt = get_number_fmt(signs=self.signs, decimal=self.decimal, exponential=self.exponential)

        self.allow_keys = [wx.WXK_RETURN, wx.WXK_DELETE, wx.WXK_BACK, wx.WXK_DECIMAL, ord('.')]
        if self.signs:
            self.allow_keys.append(ord('-'))
            self.allow_keys.append(ord('+'))

        if self.exponential:
            self.allow_keys.append(ord('e'))
            self.allow_keys.append(ord('E'))

        if min:
            # self._min = kwargs.get('min', -1*sys.maxint)
            self._min = min
        else:
            self._min = -1*sys.maxint

        if max:
            # self._max = kwargs.get('max', sys.maxint)
            self._max = max
        else:
            self._max = sys.maxint

        # Event Management
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self, *args, **kwargs):
        """
        Require override.

        :param arg:
        :param kwargs:
        :return:
        """
        return FloatRangeValidator(
            signs=self.signs,
            decimal=self.decimal,
            exponential=self.exponential,
            min=self._min,
            max=self._max
        )

    def Validate(self, win, *args, **kwargs):
        """
        Override called to validate the window's value.

        :param win:
        :param args:
        :param kwargs:
        :return: type-boolean
        """
        txtCtrl = self.GetWindow()
        val = txtCtrl.GetValue()
        isValid = False

        if isFloat(val):
            digit = float(val)
            if digit >= self._min and digit <= self._max:
                isValid = True

        if not isValid:
            # Notify the user of the invalid value
            msg = "Value must be between %d and %d" % (self._min, self._max)

            wx.MessageBox(msg, "Invalid Value", style=wx.OK | wx.ICON_ERROR)

        return isValid

    def OnChar(self, event):
        """

        :param event:
        :return:
        """
        txtCtrl = self.GetWindow()
        key = event.GetKeyCode()
        isDigit = False
        if key < 256:
            isDigit = chr(key).isdigit()

        if key in self.allow_keys or key > 255 or isDigit:
            # if isDigit:
            #     # Check if in range
            #     val = txtCtrl.GetValue()
            #     digit = chr(key)
            #
            #     pos = txtCtrl.GetInsertionPoint()
            #     if pos == len(val):
            #         val += digit
            #     else:
            #         val = val[:pos] + digit + val[pos:]
            #
            #     values = parse_number(val, self.fmt)
            #
            #     val = int(val)
            #     if val < self._min or val > self._max:
            #         if not wx.Validator_IsSilent():
            #             wx.Bell()
            #
            #         return
            event.Skip()

            return

        if not wx.Validator_IsSilent():
            # Beep to warn about invalid input
            wx.Bell()

        return

    def TransferToWindow(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        return True

    def TransferFromWindow(self):
        """

        :return:
        """
        return True
