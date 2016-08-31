import re

import wx

from wx import GridSizer
from wx.lib.agw.supertooltip import SuperToolTip

from peui.units import area, charge, inertia, length, mass, pressure, volume, tnt, density, torque

from .label import SmartLabel
from . import LayoutDimensions, SmartToolTip

from ..units import KEY_IMPERIAL, KEY_METRIC
from ..units.acceleration import AccelerationUnit
from ..units.angle import AngleUnit
from ..units.area_density import AreaDensityUnit
from ..units.area import AreaUnit
from ..units.charge import ChargeUnit
from ..units.density import DensityUnit
from ..units.force import ForceUnit
from ..units.inertia import InertiaUnit
from ..units.length import LengthUnit
from ..units.linear_density import LinearDensityUnit
from ..units.linear_pressure import LinearPressureUnit
from ..units.mass import MassUnit
from ..units.pressure import PressureUnit
from ..units.time import TimeUnit
from ..units.tnt import TntUnit
from ..units.torque import TorqueUnit
from ..units.velocity import VelocityUnit
from ..units.volume import VolumeUnit

__author__ = 'jbui'


class SmartTextBox(wx.TextCtrl):
    """
    Create a smarter text box that could capture keys and process them
    to see if the format is correct.

    The validation method goes through three process:

        1. OnChar(): Capture ony the key character that are necessary.
        2. wx.EVT_TEXT: Validate that the input is actually a number.
        3. Validate(): Check against the tolerance level.

    """
    def __init__(self, parent, key_up=None, message=None, enabled_message='',
                 disabled_messages=None, disabled_index=None, value=None, enable=None, *args, **kwargs):
        """

        :param parent: parent ui
        :param key_up: bind key up handler
        :param message: add in tooltip message
        :param enabled_message: message once the box is enabled
        :param disabled_messages: list of array messages
        :param disabled_index: index of the which messages to display
        :param value: initial value for smart box
        :param args:
        :param kwargs:
        """
        wx.TextCtrl.__init__(self, parent, *args, **kwargs)

        if value is not None:
            self.Value = str(value)

        self.keys = kwargs.get('keys', {})
        self.parent = parent

        if key_up:
            self.Bind(wx.EVT_KEY_UP, key_up, self)

        self.tooltip = None
        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

        self.enabled_message = enabled_message
        self.disabled_messages = disabled_messages

        if disabled_index is None and self.disabled_messages:
            self.disabled_index = 0
        else:
            self.disabled_index = disabled_index

        if enable is not None:
            self.Enable(enable)

    @property
    def min(self):
        """
        Return the minimum value.

        :return: minimum value
        """
        return self.keys.get('min')

    @min.setter
    def min(self, value):
        """
        Set the minimum value.

        :param value:
        """
        self.keys['min'] = value

    @property
    def max(self):
        """
        Return the maximum value.

        :return: return max value
        """
        return self.keys.get('max')

    @max.setter
    def max(self, value):
        """
        Set the maximum value.

        :param: value
        """
        self.keys['max'] = value

    def set_value(self, value, fmt=None):
        """
        Set the textbox value

        :param value: text
        :return:
        """
        if value is not None:
            if fmt:
                self.Value = fmt%(value)
            else:
                self.Value = str(value)
        else:
            self.Value = ""

    def get_value(self, key=None):
        """
        Get the value

        :param key:
        :return:
        """
        val = self.GetValue()

        if key is not None:
            # When key is strike we capture.
            digit = chr(key)

            pos = self.GetInsertionPoint()
            if pos == len(val):
                val += digit
            else:
                val = val[:pos] + digit + val[pos:]

        return val

    def Enable(self, *args, **kwargs):
        """
        On enable, clean data if needed.

        :param args:
        :param kwargs:
        """
        wx.TextCtrl.Enable(self, *args, **kwargs)

        if self.disabled_messages:
            if self.Value in self.disabled_messages:
                self.Value = self.enabled_message

    def Disable(self, *args, **kwargs):
        """
        On disable, add message if needed.

        :param args:
        :param kwargs:
        """
        wx.TextCtrl.Disable(self, *args, **kwargs)

        if self.disabled_messages:
            self.Value = self.disabled_messages[self.disabled_index]


class SmartComboBox(wx.ComboBox):
    """
    Smart ComboBox is used for units conversion.

    """
    def __init__(self, parent, data=None, style=wx.CB_READONLY, value='', message=None, unit=None, unit_system=None,
                 enabled_message='', disabled_messages=None, disabled_index=None, enable=None, *args, **kwargs):
        """
        Constructor

        :param parent: parent panel or frame
        :param data: list of values
        :param style: combobox style
        :param value: display value
        :param message: tooltip message
        :param unit: Unit object
        :param unit_system: 'imperial' or 'metric'
        :param args:
        :param kwargs:
        :return:
        """
        wx.ComboBox.__init__(self, parent, style=style, *args, **kwargs)

        self.convert = None
        self.unit_system = unit_system
        self.unit = unit

        if data:
            self.AppendItems(data)

        if value:
            self.Value = value

        self.tooltip = None
        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

        self.previous_index = 0
        self.enabled_message = enabled_message
        self.disabled_messages = disabled_messages

        if disabled_index is None and self.disabled_messages:
            self.disabled_index = 0
        else:
            self.disabled_index = disabled_index

        if unit:
            # If unit is passed in, activate it.
            self.activate()

        self.current_dropbox_selection = None

        self.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.on_dropdown_open, self)

        if enable is not None:
            self.Enable(enable)

    def Enable(self, *args, **kwargs):
        """
        On enable, clean data if needed.

        :param args:
        :param kwargs:
        """
        wx.ComboBox.Enable(self, *args, **kwargs)

        if self.disabled_messages:
            if self.Value in self.disabled_messages:
                for index, label in enumerate(self.Strings):
                    if label in self.disabled_messages:
                        self.Delete(index)

                self.SetSelection(self.previous_index)

    def Disable(self, *args, **kwargs):
        """
        On disable, add message if needed.

        :param args:
        :param kwargs:
        """
        wx.ComboBox.Disable(self, *args, **kwargs)

        if self.disabled_messages:
            self.previous_index = self.GetCurrentSelection()
            self.Append(self.disabled_messages[self.disabled_index])
            self.SetSelection(self.GetCount() - 1)

    def on_dropdown_open(self, event=None):
        """
        Event handler to store the current selection

        :param:
        """
        self.current_dropbox_selection = self.GetCurrentSelection()

    def is_selection_change(self):
        """
        Check if the dropbox selection different from the previous selection before the dropbox is open.

        :return: boolean
        """
        if self.current_dropbox_selection is self.GetSelection():
            return False
        else:
            return True

    def append(self, label, obj):
        """
        Append data into combobox.

        :param label: title
        :param obj: object data
        :return:
        """
        self.Append(label, obj)

    def set_selection_by_data(self, value):
        """
        Set the selection given the data input.

        :param value:
        :return:
        """
        for index, text in enumerate(self.Strings):
            if self.HasClientData():
                if self.GetClientData(index) == value:
                    self.SetSelection(index)

                    # Leave loop
                    return

    def get_data(self):
        """
        Get the data.

        :return:
        """
        return self.GetClientData(self.GetSelection())

    def set_value(self, value):
        """
        Set the value

        :param value: string
        :return:
        """
        self.Value = str(value)

    def get_value(self):
        """
        Get the combobox value

        :return:
        """
        return self.Value

    def activate(self):
        """
        Activate Units.

        :return:
        """
        self.Clear()
        self.AppendItems(self.unit.get_list())
        self.SetSelection(self.unit.get_default_selection())
        self.convert = self.unit.get_conversion_factor

    def activate_acceleration(self, *args, **kwargs):
        """
        Activate acceleration unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = AccelerationUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_angle(self, *args, **kwargs):
        """
        Activate angle unit

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = AngleUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_area_density(self, *args, **kwargs):
        """
        Activate area density unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = AreaDensityUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_area(self, *args, **kwargs):
        """
        Activate area unit.

        :param kwargs:
        """
        self.unit = AreaUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_charge(self, *args, **kwargs):
        """
        Activate charge weight.

        :param kwargs:
        """
        self.unit = ChargeUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_density(self, *args, **kwargs):
        """
        Activate density unit.

        :param args:
        :param kwargs:
        """
        self.unit = DensityUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_force(self, *args, **kwargs):
        """
        Active force unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = ForceUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_inertia(self, *args, **kwargs):
        """
        Activate Inertia unit.

        :param args:
        :param kwargs:
        """
        self.unit = InertiaUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_length(self, *args, **kwargs):
        """
        Activate length unit.

        :param args:
        :param kwargs:
        """
        self.unit = LengthUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_linear_density(self, *args, **kwargs):
        """
        Activate linear density unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = LinearDensityUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_linear_pressure(self, *args, **kwargs):
        """
        Activate linear pressure unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = LinearPressureUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_mass(self, *args, **kwargs):
        """
        Activate mass units.

        :param kwargs:
        """
        self.unit = MassUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_pressure(self, *args, **kwargs):
        """
        Activate pressure unit.

        :param kwargs:
        """
        self.unit = PressureUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_time(self, *args, **kwargs):
        """
        Activate time unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = TimeUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_tnt(self, *args, **kwargs):
        """
        Activate tnt unit.

        :param args:
        :param kwargs:
        """
        self.unit = TntUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_torque(self, *args, **kwargs):
        """
        Activate Torque unit.

        :param args:
        :param kwargs:
        """
        self.unit = TorqueUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_velocity(self, *args, **kwargs):
        """
        Activate Velocity unit.

        :param args:
        :param kwargs:
        :return:
        """
        self.unit = VelocityUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def activate_volume(self, *args, **kwargs):
        """
        Activate volume unit.

        :param args:
        :param kwargs:
        """
        self.unit = VolumeUnit(*args, **kwargs)

        if kwargs.get('unit_list'):
            unit_list = kwargs.get('unit_list')

            self.unit.metric_list = unit_list['metric']
            self.unit.imperial_list = unit_list['imperial']

        self.unit.unit_system = self.unit_system
        self.activate()

    def get_factor(self, origin, destination):
        """
        Get the factor.

        :param origin: origin unit
        :param destination: destination unit
        """
        return self.convert(origin, destination)


class SmartInputLayout(wx.BoxSizer):
    """
    Create the horizontal layout of smart textbox.

    /---------------- OVERALL WIDTH ----------------------/
    |                                                     |
    |                                                     |

    *******************************************************     ----/
    *    *     * *                     * *              * *         |
    *******************************************************         |
    *    *     * *                     * *              * *
    *    * (1) * *         (2)         * *     (3)      * *     OVERALL HEIGHT
    *    *     * *                     * *              * *
    *******************************************************         |
    *    *     * *                     * *              * *         |
    *******************************************************     ----/

    """

    MAKE_VERTICAL_STRETCHABLE = 1

    def __init__(self, parent, max=None, min=None, layout=None, label=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param width:
        :param max: maximum value for the textbox
        :param min: minimum value for the textbox
        :param layout:
        :param label: pass in wx.Label or SmartLabel
        :param args:
        :param kwargs:
        """
        wx.BoxSizer.__init__(self, wx.VERTICAL)

        self.components = []
        self.parent = parent
        self.hsizer = None
        self._next_id = 0
        self.INDEX_LABEL = None
        self.INDEX_TEXTBOX = None
        self.INDEX_POSTBOX = None
        self.INDEX_COMBOBOX = None

        if layout:
            self.layout = layout
        else:
            self.layout = LayoutDimensions()

            self.layout.calculate()

        # Add in the label.
        if label:
            self.label = label
        elif kwargs.get('name'):
            self.label = SmartLabel(self.parent, label=kwargs.get('name'))
        else:
            self.label = SmartLabel(self.parent, label='Textbox Label:')

        self.min = min
        self.max = max

        # Set minimum size.
        size = self.GetSize()
        size.Height = self.layout.overall_height
        self.SetMinSize(size)

    def rename(self, name=None):
        self.label = wx.StaticText(self.parent,
                                   label=name)

    @property
    def next_id(self):
        """

        :return:
        """
        nid = self._next_id
        self._next_id += 1
        return nid

    @property
    def label(self):
        """

        :return:
        """
        if self.INDEX_LABEL is None:
            return None

        return self.components[self.INDEX_LABEL]

    @label.setter
    def label(self, value):
        """

        :param value:
        :return:
        """
        if value is None:
            return

        self.INDEX_LABEL = self.next_id
        self.components.append(value)

    @property
    def textbox(self):
        """

        :return:
        """
        if self.INDEX_TEXTBOX is None:
            return None

        return self.components[self.INDEX_TEXTBOX]

    @textbox.setter
    def textbox(self, value):
        """

        :param value:
        :return:
        """
        if value is None:
            return

        self.INDEX_TEXTBOX = self.next_id
        self.components.append(value)

    @property
    def postbox(self):
        """

        :return:
        """
        if self.INDEX_POSTBOX is None:
            return None

        return self.components[self.INDEX_POSTBOX]

    @postbox.setter
    def postbox(self, value):
        """

        :param value:
        :return:
        """
        if value is None:
            return

        self.INDEX_POSTBOX = self.next_id
        self.components.append(value)

    @property
    def combobox(self):
        """

        :return:
        """
        if self.INDEX_COMBOBOX is None:
            return None

        return self.components[self.INDEX_COMBOBOX]

    @combobox.setter
    def combobox(self, value):
        """

        :param value:
        :return:
        """
        if value is None:
            return

        self.INDEX_COMBOBOX = self.next_id
        self.components.append(value)

    def do_layout(self):
        """
        Do Layout.

        :return:
        """

        # Start with the vertical margin.
        self.AddSpacer(self.layout.top)

        # Move from left to right.
        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        # self.hsizer.SetMinSize(wx.Size(self.layout.overall_width, self.layout.height))

        self.hsizer.AddSpacer(self.layout.left)

        for id in range(0, len(self.components)):
            """
                wx.BoxSizer.Add(window, proportion=0, flag=0, border=0, userData=None)
                    Append a child to the sizer

                    :param window: a window, a spacer or another sizer to be added to the sizer.  Its initial size
                        (either set explicitly by the user or calculated internally) is interpreted as the minimal and
                        in many cases also the initial size.
                    :param proportion: (int) the parameter is used in wx.BoxSizer to indicate if a child of a sizer can
                        change its size in the main orientation of the wx.BoxSizer - where 0 stands for non changeable
                        and a value of more than zero is interpreted relative to the value of other children of the
                        same wx.BosSizer.  For example, you might have a horizontal wx.BoxSizer with three children,
                        two of which are supposed to change their size with the sizer.  Then the two stretchable
                        windows would get a value of 1 each to make item grow and shrink equally with the sizer's
                        horizontal dimension.
                    :param flag: (int): combinations of flags affecting sizer's behavior
                    :param border: (int): determines the border width, if the flag parameter is set to include any
                        border flag
                    :param userData: (object) allows an extra object to be attached to the sizer item, for use in
                        derived classes when sizing information

            """
            self.components[id].SetMinSize(self.layout.get_size(id))

            self.hsizer.AddSpacer(self.layout.interior)
            self.hsizer.Add(self.components[id],
                            self.layout.stretch_factor[id],
                            wx.ALL | wx.EXPAND,
                            self.layout.border_width[id])

        # Add blank space if no component exists.
        for id_blank in range(id+1, len(self.layout.widths)):
            self.hsizer.AddSpacer(self.layout.interior)

            blank_label = wx.StaticText(self.parent, label="")
            blank_label.SetMinSize(self.layout.get_size(id_blank))

            self.hsizer.Add(blank_label,
                            self.layout.stretch_factor[id_blank],
                            wx.ALL | wx.EXPAND,
                            self.layout.border_width[id_blank])


        self.hsizer.AddSpacer(self.layout.right)

        self.Add(self.hsizer, 1, wx.EXPAND | wx.ALL, 0)
        self.AddSpacer(self.layout.bottom)

    def add(self, item, proportion=0, flag=0, border=0, userData=None):
        """
        Appends a child item to the sizer.

        :param item: The item can be one of three kind of objects:

            * window: A wx.Window to be managed by the sizer. Its minimal size (either set explicitly by the user or
                calculated internally when constructed with wx.DefaultSize) is interpreted as the minimal size to use
                when laying out item in the sizer. This is particularly useful in connection with
                wx.Window.SetSizeHints.

            * sizer: The (child-)sizer to be added to the sizer. This allows placing a child sizer in a sizer and thus
                to create hierarchies of sizers (for example a vertical box as the top sizer and several horizontal
                boxes on the level beneath).

            * size: A wx.Size or a 2-element sequence of integers that represents the width and height of a spacer to
                be added to the sizer. Adding spacers to sizers gives more flexibility in the design of dialogs;
                imagine for example a horizontal box with two buttons at the bottom of a dialog: you might want to
                insert a space between the two buttons and make that space stretchable using the proportion value and
                the result will be that the left button will be aligned with the left side of the dialog and the right
                button with the right side - the space in between will shrink and grow with the dialog.

        :param proportion: Although the meaning of this parameter is undefined in wx.Sizer, it is used in wx.BoxSizer
            to indicate if a child of a sizer can change its size in the main orientation of the wx.BoxSizer - where 0
            stands for not changeable and a value of more than zero is interpreted relative (a proportion of the total)
            to the value of other children of the same wx.BoxSizer. For example, you might have a horizontal
            wx.BoxSizer with three children, two of which are supposed to change their size with the sizer. Then the
            two stretchable windows should each be given proportion value of 1 to make them grow and shrink equally
            with the sizer's horizontal dimension. But if one of them had a proportion value of 2 then it would get a
            double share of the space available after the fixed size items are positioned.

            (type int)

        :param flag: This parameter can be used to set a number of flags which can be combined using the binary OR
            operator |. Two main behaviours are defined using these flags. One is the border around a window: the
            border parameter determines the border width whereas the flags given here determine which side(s) of the
            item that the border will be added. The other flags determine how the sizer item behaves when the space
            allotted to the sizer changes, and is somewhat dependent on the specific kind of sizer used.

            * wx.TOP
            * wx.BOTTOM
            * wx.LEFT
            * wx.RIGHT
            * wx.ALL

            * wx.EXPAND

            * wx.SHAPED

            * wx.FIXED_MINSIZE

            * wx.ALIGN_CENTER
            * wx.ALIGN_LEFT
            * wx.ALIGN_RIGHT
            * wx.ALIGN_TOP
            * wx.ALIGN_BOTTOM
            * wx.ALIGN_CENTER_VERTICAL
            * wx.ALIGN_CENTER_HORIZONTAL

            (type int)

        :param border: Determines the border width, if the flag parameter is set to include any border flag.

            (type int)

        :param userData: Allows an extra object to be attached to the sizer item, for use in derived classes when
            sizing information is more complex than the proportion and flag will allow for.

            (type=PyObject)
        """
        self.Add(item, proportion, flag, border, userData)

    def add_stretch_spacer(self, prop=1):
        """
        Add a stretchable spacer.

        :param prop:
        :return:
        """
        self.AddStretchSpacer(prop=prop)

    def add_spacer(self, size):
        """
        Add a spacer that is (size, size) pixels.

        :param size:
        :return:
        """
        self.AddSpacer(size)

    def fit(self, window):
        """
        Tell the sizer to resize the window to match the sizer's minimal size. This is commonly done in the constructor
        of the window itself in order to set its initial size to match the needs of the children as determined by the
        sizer. Returns the new size.

        For a top level window this is the total window size, not the client size.

        :param window:
        :return:
        """
        self.Fit(window)

    def enable(self):
        """
        Must inherit enable input layout.

        """
        pass

    def disable(self):
        """
        Must inherit disable input layout.

        """
        pass

    def validate(self):
        """
        Must inherit validate().

        """
        pass


class SmartButton(wx.Button):
    """
    Smarter Button Class

    """
    def __init__(self, parent, label='', evt_button=None, message=None, enable=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param label:
        :param evt_button:
        :param message:
        :param args:
        :param kwargs:
        :return:
        """
        wx.Button.__init__(self, parent, label=label, *args, **kwargs)

        if evt_button:
            self.Bind(wx.EVT_BUTTON, evt_button)

        self.tooltip = None
        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

        if enable is not None:
            self.Enable(enable)


class SmartCheckBox(wx.CheckBox):
    """
    **Smarter CheckBox**

    """
    def __init__(self, parent, id=-1, label='', evt_click=None, message=None, enable=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param id:
        :param label:
        :param args:
        :param kwargs:
        :return:
        """
        wx.CheckBox.__init__(self, parent, id=id, label=label, *args, **kwargs)

        self.tooltip = None
        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

        if evt_click:
            self.Bind(wx.EVT_CHECKBOX, evt_click)

        if enable is not None:
            self.Enable(enable)

    def get_value(self):
        """
        Return the true/false

        :return:
        """
        return self.Value
