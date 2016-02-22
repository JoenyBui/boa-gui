import os
import sys
import re

import wx

from pecutil.refmt import get_number_fmt, parse_number

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class FloatSmartBox(SmartTextBox):
    """

    """
    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args)

        self.signs = kwargs.get('signs', False)
        self.decimal = kwargs.get('decimal', True)
        self.exponential = kwargs.get('exponential', False)

        self.fmt = get_number_fmt(signs=self.signs, decimal=self.decimal, exponential=self.exponential)

        # self.Bind(wx.EVT_CHAR, self.on_key_char, self)
        # self.Bind(wx.EVT_CHAR_HOOK, self.on_key_char_hook, self)
        # self.Bind(wx.EVT_KEY_UP, self.on_key_up, self)
        # self.Bind(wx.EVT_KEY_DOWN, self.on_key_down, self)
        self.Bind(wx.EVT_TEXT, self.on_text, self)

        self.color_normal = kwargs.get('normal', (255, 255, 255))
        self.color_format_error = kwargs.get('format_error', (228, 115, 115))
        self.color_range_error = kwargs.get('range_error', (244, 67, 54))

        self._validator = FloatRangeValidator(**kwargs)
        self.SetValidator(self._validator)

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

    def on_key_up(self, event=None):
        event.Skip()

    def on_key_down(self, event=None):
        event.Skip()

    def on_key_char(self, event=None):
        kc = event.GetKeyCode()
        event.Skip()

    def on_key_char_hook(self, event=None):
        kc = event.GetKeyCode()
        event.Skip()

    def set_normal_color(self):
        self.SetBackgroundColour(self.color_normal)

    def set_format_error_color(self):
        self.SetBackgroundColour(self.color_format_error)

    def set_range_error_color(self):
        self.SetBackgroundColour(self.color_range_error)


class FloatInputLayout(SmartInputLayout):
    """

    """
    def __init__(self, parent, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        self.label = kwargs.get('label', 'Float Label:')

        if kwargs.get('textbox'):
            self.textbox = kwargs.get('textbox')
        else:
            self.textbox = FloatSmartBox(parent, **kwargs)

        if kwargs.get('postbox'):
            self.postbox = kwargs.get('postbox')

        self.do_layout()


class FloatRangeValidator(wx.PyValidator):
    """
    Float Range Validator
    """
    def __init__(self, **kwargs):
        wx.PyValidator.__init__(self)

        self.signs = kwargs.get('signs', False)
        self.decimal = kwargs.get('decimal', True)
        self.exponential = kwargs.get('exponential', False)

        self.fmt = get_number_fmt(signs=self.signs, decimal=self.decimal, exponential=self.exponential)

        self.allow_keys = [wx.WXK_RETURN, wx.WXK_DELETE, wx.WXK_BACK, wx.WXK_DECIMAL, ord('.')]
        if self.signs:
            self.allow_keys.append(ord('-'))
            self.allow_keys.append(ord('+'))

        if self.exponential:
            self.allow_keys.append(ord('e'))
            self.allow_keys.append(ord('E'))

        self._min = kwargs.get('min', -1*sys.maxint)
        self._max = kwargs.get('max', sys.maxint)

        # Event Management
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self, *args, **kwargs):
        """
        Require override.
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
        return True

    def TransferFromWindow(self):
        return True
