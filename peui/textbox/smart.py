import re

import wx

from wx import GridSizer
from wx.lib.agw.supertooltip import SuperToolTip

from peui.units import area, charge, inertia, length, mass, pressure, volume, density, torque, misc

from ..units import KEY_IMPERIAL, KEY_METRIC

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
    def __init__(self, parent, data=None, style=wx.CB_READONLY, value='', *args, **kwargs):
        wx.ComboBox.__init__(self, parent, style=style, *args, **kwargs)

        self.convert = None
        self.unit_system = None

        if data:
            self.AppendItems(data)

        if value:
            self.Value = value

    def activate_area(self, **kwargs):
        """
        Activate the area.
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', area.DEFAULT_IMPERIAL__LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', area.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', area.DEFAULT_AREA_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = area.get_area_conversion_factor

    def activate_charge(self, **kwargs):
        """
        Activate charge weight.
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', charge.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', charge.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', charge.DEFAULT_CHARGE_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = charge.get_charge_conversion_factor

    def activate_inertia(self, **kwargs):
        """
        Activate Inertia
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', inertia.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', inertia.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', inertia.DEFAULT_INERTIA_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = inertia.get_inertia_conversion_factor

    def activate_length(self, **kwargs):
        """
        Activate length.
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', length.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', length.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', length.DEFAULT_LENGTH_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = length.get_length_conversion_factor

    def activate_mass(self, **kwargs):
        """
        Activate the mass units.
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', mass.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', mass.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', mass.DEFAULT_MASS_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = mass.get_mass_conversion_factor

    def activate_pressure(self, **kwargs):
        """
        Activate the pressure.
        """

        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', pressure.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', pressure.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', pressure.DEFAULT_PRESSURE_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = pressure.get_pressure_conversion_factor

    def activate_volume(self, **kwargs):
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', volume.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', volume.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', volume.DEFAULT_VOLUME_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = volume.get_volume_conversion_factor

    def activate_density(self, **kwargs):
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', density.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', density.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', density.DEFAULT_DENSITY_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = density.get_density_conversion_factor

    def activate_torque(self, **kwargs):
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', torque.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', torque.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', torque.DEFAULT_TORQUE_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = torque.get_torque_conversion_factor

    def activate_misc(self, **kwargs):
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', misc.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', misc.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', misc.DEFAULT_MISC_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = misc.get_misc_conversion_factor

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
        self.border_space = kwargs.get('border_space', 5)
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
            self.Add(self.label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, self.border_space_label)
            # self.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_label)

        if self.textbox:
            self.Add(self.textbox, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, self.border_space_textbox)
            # self.Add(self.textbox, 0, wx.EXPAND, self.border_space_textbox)

        if self.postbox:
            # self.Add(self.postbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_postbox)

            # self.Add(self.postbox, 0, wx.ALIGN_RIGHT, self.border_space_postbox)
            self.Add(self.postbox)

        # self.AddStretchSpacer()


    def validate(self):
        pass
