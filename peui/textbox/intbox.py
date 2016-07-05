import os
import sys
import types

import wx

from pecutil.refmt import get_number_fmt, parse_number

from peui import units

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class IntSmartBox(SmartTextBox):
    """
    Integer Smart Box.

    """
    def __init__(self, parent, signs=False, format_error=None, key_up=None, message=None, *args, **kwargs):
        """
        Integer Smart Box.s

        :param parent:
        :param signs:
        :param format_error:
        :param key_up:
        :param message:
        :param args:
        :param kwargs:
        :return:
        """
        SmartTextBox.__init__(self, parent, key_up=key_up, message=message, *args, **kwargs)

        self.fmt = get_number_fmt(signs=kwargs.get('signs'), decimal=False, exponential=False)

        self.color_normal = kwargs.get('normal', (255, 255, 255))
        self.color_format_error = kwargs.get('format_error', (228, 115, 115))
        self.color_range_error = kwargs.get('range_error', (244, 67, 54))

        self._validator = IntRangeValidator(**kwargs)
        self.SetValidator(self._validator)

        self.Bind(wx.EVT_TEXT, self.on_text, self)

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

    def set_normal_color(self):
        """
        Set the normal color

        """
        self.SetBackgroundColour(self.color_normal)

    def set_format_error_color(self):
        """
        Set the format color

        """
        self.SetBackgroundColour(self.color_format_error)

    def set_range_error_color(self):
        """
        Set the background color

        """
        self.SetBackgroundColour(self.color_range_error)


class IntInputLayout(SmartInputLayout):
    """
    Int Input Layout.

    """
    def __init__(self, parent, value=None, unit=None, unit_system=None, type=None, max=None, min=None,
                 layout=None, textbox=None, postbox=None, *args, **kwargs):
        """

        :param parent:
        :param value:
        :param unit:
        :param unit_system:
        :param type:
        :param max:
        :param min:
        :param layout:
        :param textbox:
        :param postbox:
        :param args:
        :param kwargs:
        :return:
        """

        SmartInputLayout.__init__(self, parent, max=max, min=min, layout=layout, *args, **kwargs)

        if textbox:
            self.textbox = textbox
        else:
            self.textbox = IntSmartBox(parent, **kwargs)

        # self.textbox.SetSize(self.layout.get_size(self.INDEX_TEXTBOX))

        if value:
            self.textbox.Value = str(value)

        if postbox:
            self.postbox = postbox
            # self.postbox.SetSize(self.layout.get_size(self.INDEX_POSTBOX))

            self.postbox.unit_system = unit_system

            if type:
                if type == units.UNIT_AREA_KEY:
                    self.postbox.activate_area()
                    self.type = type
                elif type == units.UNIT_CHARGE_KEY:
                    self.postbox.activate_charge()
                    self.type = type
                elif type == units.UNIT_INERTIA_KEY:
                    self.postbox.activate_inertia()
                    self.type = type
                elif type == units.UNIT_LENGTH_KEY:
                    self.postbox.activate_length()
                    self.type = type
                elif type == units.UNIT_MASS_KEY:
                    self.postbox.activate_mass()
                    self.type = type
                elif type == units.UNIT_PRESSURE_KEY:
                    self.postbox.activate_pressure()
                    self.type = type
                elif type == units.UNIT_VOLUME_KEY:
                    self.postbox.activate_volume()
                    self.type = type

            if unit:
                if isinstance(unit, types.TupleType) or isinstance(unit, types.ListType):
                    if units.KEY_IMPERIAL == unit_system:
                        self.postbox.Value = unit[0]
                    elif units.KEY_METRIC == unit_system:
                        self.postbox.Value = unit[1]

                else:
                    self.postbox.Value = unit

        self.do_layout()

    def set_value(self, value, post=None, label=None):
        """

        :param value:
        :param post:
        :param label:
        :return:
        """
        if value:
            self.textbox.Value = str(value)

        if post and self.postbox:
            self.postbox.Value = str(post)

        if label:
            self.label.Label = str(label)

    def get_value(self, unit):
        """

        :param unit:
        :return:
        """
        conversion_factor = 1.0
        if self.type == units.UNIT_AREA_KEY:
            conversion_factor = units.get_area_conversion_factor(self.postbox.Value, unit)
        elif self.type == units.UNIT_CHARGE_KEY:
            conversion_factor = units.get_charge_conversion_factor(self.postbox.Value, unit)
        elif self.type == units.UNIT_LENGTH_KEY:
            conversion_factor = units.get_length_conversion_factor(self.postbox.Value, unit)
        elif self.type == units.UNIT_INERTIA_KEY:
            conversion_factor = units.get_inertia_conversion_factor(self.postbox.Value, unit)
        elif self.type == units.UNIT_MASS_KEY:
            conversion_factor = units.get_mass_conversion_factor(self.postbox.Value, unit)
        elif self.type == units.UNIT_PRESSURE_KEY:
            conversion_factor = units.get_pressure_conversion_factor(self.postbox.Value, unit)
        elif self.type == units.UNIT_VOLUME_KEY:
            conversion_factor = units.get_volume_conversion_factor(self.postbox.Value, unit)

        return int(conversion_factor * int(self.textbox.Value))

    def validate(self):
        """

        :return:
        """
        return False


class IntRangeValidator(wx.PyValidator):
    """
    Int Range Validator
    """
    def __init__(self, signs=False, *args, **kwargs):
        wx.PyValidator.__init__(self)

        self.signs = kwargs.get('signs', False)
        # self.decimal = kwargs.get('decimal', False)
        # self.exponential = kwargs.get('exponential', False)

        self.fmt = get_number_fmt(signs=self.signs, decimal=False, exponential=False)

        self.allow_keys = [wx.WXK_RETURN, wx.WXK_DELETE, wx.WXK_BACK]
        if self.signs:
            self.allow_keys.append(ord('-'))
            self.allow_keys.append(ord('+'))

        self._min = kwargs.get('min', -1*sys.maxint)
        self._max = kwargs.get('max', sys.maxint)

        # Event Management
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self, *args, **kwargs):
        """
        Require override.

        :param args:
        :param kwargs:
        """
        return IntRangeValidator(
            signs=self.signs,
            min=self._min,
            max=self._max
        )

    def Validate(self, win, *args, **kwargs):
        """
        Override called to validate the window's value.

        :param win:
        :param args:
        :param kwargs:
        """
        txtCtrl = self.GetWindow()
        val = txtCtrl.GetValue()
        isValid = False

        if val.isdigit():
            digit = int(val)
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
        # if key in self.allow_keys or isDigit:
            # if isDigit:
            #     # Check if in range
            #     val = txtCtrl.get_value(key)
            #
            #     value, src = parse_number(self.fmt, val)

                # val = int(val)
                # if val < self._min or val > self._max:
                #     if not wx.Validator_IsSilent():
                #         wx.Bell()

                    # return

            # if key == ord('-'):
            #     val = txtCtrl.get_value(key)
            #
            #     values, src = parse_number(val, self.fmt)
            #
            #     if len(values) != 1 and val != '-' and val != '+':
            #         if not wx.Validator_IsSilent():
            #             wx.Bell()
            #             txtCtrl.set_format_error_color()
            #         # return


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
