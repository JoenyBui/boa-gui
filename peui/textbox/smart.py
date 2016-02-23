import re

import wx
from wx import GridSizer

__author__ = 'jbui'


class SmartTextBox(wx.TextCtrl):
    """
    Create a smarter text box that could capture keys and process them
    to see if the format is correct.
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
    def __init__(self, parent, *args, **kwargs):
        wx.ComboBox.__init__(self, parent, *args, **kwargs)


class SmartInputLayout(wx.BoxSizer):
    """
    Create the horizontal layout of smart textbox.


    * --------------------------------------------*
    * |     |                      |              |
    * |     |                      |              |
    * --------------------------------------------*

    """
    def __init__(self, parent, *args, **kwargs):

        wx.BoxSizer.__init__(self, wx.HORIZONTAL)

        self.parent = parent

        label_width = 150
        if kwargs.get('label_width'):
            label_width = kwargs.get('label_width')

        if kwargs.get('label'):
            self.label = None
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
        # Additional placeholder that is significant (unit box, path button, etc.)

        # Call do_layout after you have populate the label, textbox, and/or postbox

    def do_layout(self):
        """

        :return:
        """
        border_space = 10

        if self.label:
            self.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border_space)

        if self.textbox:
            self.Add(self.textbox, 0, wx.EXPAND, border_space)

        if self.postbox:
            self.Add(self.postbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border_space)
