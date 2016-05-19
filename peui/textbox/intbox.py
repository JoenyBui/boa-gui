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
    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args)

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
        self.SetBackgroundColour(self.color_normal)

    def set_format_error_color(self):
        self.SetBackgroundColour(self.color_format_error)

    def set_range_error_color(self):
        self.SetBackgroundColour(self.color_range_error)


class IntInputLayout(SmartInputLayout):

    def __init__(self, parent, value=None, unit=None, unit_system=None, type=None, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        # self.label = kwargs.get('label', 'Input Label:')

        if kwargs.get('textbox'):
            self.textbox = kwargs.get('textbox')
        else:
            self.textbox = IntSmartBox(parent, **kwargs)

        self.postbox.unit_system = unit_system
        if type:
            if type == units.UNIT_AREA_KEY:
                pass
            elif type == units.UNIT_CHARGE_KEY:
                pass
            elif type == units.UNIT_INERTIA_KEY:
                pass
            elif type == units.UNIT_LENGTH_KEY:
                pass
            elif type == units.UNIT_MASS_KEY:
                pass
            elif type == units.UNIT_PRESSURE_KEY:
                pass
            elif type == units.UNIT_VOLUME_KEY:
                pass

        if value:
            self.textbox.Value = str(value)

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
        if value:
            self.textbox.Value = str(value)

        if post and self.postbox:
            self.postbox.Value = str(post)

        if label:
            self.label.Label = str(label)

    def validate(self):
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
        """
        return IntRangeValidator(
            signs=self.signs,
            min=self._min,
            max=self._max
        )

    def Validate(self, win, *args, **kwargs):
        """
        Override called to validate the window's value.
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
        return True

    def TransferFromWindow(self):
        return True
