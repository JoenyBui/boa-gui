import re

import wx

from wx import GridSizer
from wx.lib.agw.supertooltip import SuperToolTip

from peui.units import length, charge, pressure, mass

__author__ = 'jbui'


class SmartTextBox(wx.TextCtrl):
    """
    Create a smarter text box that could capture keys and process them
    to see if the format is correct.

    The validation method goes through three process:
    1.) OnChar(): Capture ony the key character that are necessary.
    2.) wx.EVT_TEXT: Validate that the input is actually a number.
    3.) Validate(): Check against the tolerance level.
    """
    def __init__(self, parent, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, *args, **kwargs)

        self.keys = kwargs.get('keys', {})
        self.parent = parent

    @property
    def min(self):
        return self.keys.get('min')

    @min.setter
    def min(self, value):
        self.keys['min'] = value

    @property
    def max(self):
        return self.keys.get('max')

    @max.setter
    def max(self, value):
        self.keys['max'] = value

    def get_value(self, key):
        val = self.GetValue()
        digit = chr(key)

        pos = self.GetInsertionPoint()
        if pos == len(val):
            val += digit
        else:
            val = val[:pos] + digit + val[pos:]

        return val


class SmartComboBox(wx.ComboBox):
    """
    Smart ComboBox is used for units conversion.
    """
    def __init__(self, parent, style=wx.CB_READONLY, *args, **kwargs):
        wx.ComboBox.__init__(self, parent, style=style, *args, **kwargs)

        self.convert = None

    def activate_length(self, **kwargs):
        self.AppendItems(kwargs.get('list', length.DEFAULT_LENGTH_LIST))
        self.SetSelection(kwargs.get('default', 0))

        self.convert = length.get_length_conversion_factor

    def activate_mass(self, **kwargs):
        self.AppendItems(kwargs.get('list', mass.DEFAULT_MASS_LIST))
        self.SetSelection(kwargs.get('default', 0))

        self.convert = mass.get_mass_conversion_factor

    def activate_charge(self, **kwargs):
        self.AppendItems(kwargs.get('list', charge.DEFAULT_CHARGE_LIST))
        self.SetSelection(kwargs.get('default', 0))

        self.convert = charge.get_charge_conversion_factor

    def activate_pressure(self, **kwargs):
        self.AppendItems(kwargs.get('list', pressure.DEFAULT_PRESSURE_LIST))
        self.SetSelection(kwargs.get('default', 0))

        self.convert = pressure.get_pressure_conversion_factor

    def get_factor(self, destination):
        return self.convert()


class SmartInputLayout(wx.BoxSizer):
    """
    Create the horizontal layout of smart textbox.


    * --------------------------------------------*
    * |     |                      |              |
    * |     |                      |              |
    * --------------------------------------------*

    """
    def __init__(self, parent, label_width=150, max=None, min=None, *args, **kwargs):

        wx.BoxSizer.__init__(self, wx.HORIZONTAL)

        self.parent = parent

        label_width = label_width
        # if kwargs.get('label_width'):
        #     label_width = kwargs.get('label_width')

        if kwargs.get('label'):
            self.label = kwargs.get('label')
        else:
            if kwargs.get('name'):
                self.label = wx.StaticText(self.parent,
                                           label=kwargs.get('name'),
                                           size=(label_width, -1))
            else:
                self.label = wx.StaticText(self.parent,
                                           label="TextBox Label:",
                                           size=(label_width, -1))

        self.textbox = None

        self.postbox = kwargs.get('postbox', None)

        self.tooltip = kwargs.get('tooltip', SuperToolTip("HELP"))
        # self.tooltip.SetIcon(wx.ICON_WARNING)
        # self.tooltip.SetTarget(self.textbox)

        # Additional placeholder that is significant (unit box, path button, etc.)

        # Call do_layout after you have populate the label, textbox, and/or postbox
        self.border_space = kwargs.get('border_space', 10)
        self.border_space_label = kwargs.get('border_space_label', self.border_space)
        self.border_space_textbox = kwargs.get('border_space_textbox', self.border_space)
        self.border_space_postbox = kwargs.get('border_space_postbox', self.border_space)

        self.min = min
        self.max = max

    def do_layout(self):
        """
        Do Layout.
        :return:
        """

        if self.label:
            self.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_label)

        if self.textbox:
            self.Add(self.textbox, 0, wx.EXPAND, self.border_space_textbox)

        if self.postbox:
            self.Add(self.postbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_postbox)

    def validate(self):
        pass
