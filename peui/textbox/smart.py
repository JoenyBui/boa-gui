import re

import wx

from wx import GridSizer
from wx.lib.agw.supertooltip import SuperToolTip

from peui.units import area, charge, inertia, length, mass, pressure, volume, tnt, density, torque, misc

from . import LayoutDimensions
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
    def __init__(self, parent, key_up=None, message=None, *args, **kwargs):
        """

        :param parent:
        :param key_up: bind key up handler
        :param message: add in tooltip message
        :param args:
        :param kwargs:
        """
        wx.TextCtrl.__init__(self, parent, *args, **kwargs)

        self.keys = kwargs.get('keys', {})
        self.parent = parent

        if key_up:
            self.Bind(wx.EVT_KEY_UP, key_up, self)

        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

    @property
    def min(self):
        """

        :return: minimum value
        """
        return self.keys.get('min')

    @min.setter
    def min(self, value):
        """

        :param value:
        """
        self.keys['min'] = value

    @property
    def max(self):
        """

        :return: return max value
        """
        return self.keys.get('max')

    @max.setter
    def max(self, value):
        """

        :param: value
        """
        self.keys['max'] = value

    def get_value(self, key):
        """

        :param key:
        :return:
        """
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

        :param kwargs:
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

        :param kwargs:
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

        :param: kwargs:
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

        :param kwargs:
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

        :param kwargs:
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

        :param kwargs:
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
        """

        :param kwargs:
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', volume.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', volume.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', volume.DEFAULT_VOLUME_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = volume.get_volume_conversion_factor

    def activate_density(self, **kwargs):
        """

        :param kwargs:
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', density.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', density.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', density.DEFAULT_DENSITY_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = density.get_density_conversion_factor

    def activate_torque(self, **kwargs):
        """

        :param kwargs:
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', torque.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', torque.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', torque.DEFAULT_TORQUE_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = torque.get_torque_conversion_factor

    def activate_misc(self, **kwargs):
        """

        :param kwargs:
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', misc.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', misc.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', misc.DEFAULT_MISC_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = misc.get_misc_conversion_factor

    def activate_tnt(self, **kwargs):
        """

        :param kwargs:
        """
        if self.unit_system == KEY_IMPERIAL:
            self.AppendItems(kwargs.get('list', tnt.DEFAULT_IMPERIAL_LIST))
        elif self.unit_system == KEY_METRIC:
            self.AppendItems(kwargs.get('list', tnt.DEFAULT_METRIC_LIST))
        else:
            self.AppendItems(kwargs.get('list', tnt.DEFAULT_TNT_LIST))

        self.SetSelection(kwargs.get('default', 0))
        self.convert = tnt.get_tnt_conversion_factor

    def get_factor(self, destination):
        """

        :param destination:
        """
        return self.convert


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

    def __init__(self, parent, max=None, min=None, layout=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param width:
        :param max: maximum value for the textbox
        :param min: minimum value for the textbox
        :param overall_width:
        :param overall_height:
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
        if kwargs.get('label'):
            self.label = kwargs.get('label')
        else:
            if kwargs.get('name'):
                self.label = wx.StaticText(self.parent,
                                           label=kwargs.get('name'))
            else:
                self.label = wx.StaticText(self.parent,
                                           label="TextBox Label:")

        # self.label.SetMinSize(self.layout.get_size(self.INDEX_LABEL))
        #
        # self.textbox = None
        #
        # self.postbox = kwargs.get('postbox', None)

        self.tooltip = kwargs.get('tooltip', SuperToolTip("HELP"))
        # self.tooltip.SetIcon(wx.ICON_WARNING)
        # self.tooltip.SetTarget(self.textbox)

        # Additional placeholder that is significant (unit box, path button, etc.)

        # Call do_layout after you have populate the label, textbox, and/or postbox
        # self.border_space = kwargs.get('border_space', 5)
        # self.border_space_label = kwargs.get('border_space_label', self.border_space)
        # self.border_space_textbox = kwargs.get('border_space_textbox', self.border_space)
        # self.border_space_postbox = kwargs.get('border_space_postbox', self.border_space)

        self.min = min
        self.max = max

        # Set minimum size.
        size = self.GetSize()
        size.Height = self.layout.overall_height
        self.SetMinSize(size)

    @property
    def next_id(self):
        nid = self._next_id
        self._next_id += 1
        return nid

    @property
    def label(self):
        if self.INDEX_LABEL is None:
            return None

        return self.components[self.INDEX_LABEL]

    @label.setter
    def label(self, value):
        if value is None:
            return

        self.INDEX_LABEL = self.next_id
        self.components.append(value)

    @property
    def textbox(self):
        if self.INDEX_TEXTBOX is None:
            return None

        return self.components[self.INDEX_TEXTBOX]

    @textbox.setter
    def textbox(self, value):
        if value is None:
            return

        self.INDEX_TEXTBOX = self.next_id
        self.components.append(value)

    @property
    def postbox(self):
        if self.INDEX_POSTBOX is None:
            return None

        return self.components[self.INDEX_POSTBOX]

    @postbox.setter
    def postbox(self, value):
        if value is None:
            return

        self.INDEX_POSTBOX = self.next_id
        self.components.append(value)

    @property
    def combobox(self):
        if self.INDEX_COMBOBOX is None:
            return None

        return self.components[self.INDEX_COMBOBOX]

    @combobox.setter
    def combobox(self, value):
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
        self.hsizer.SetMinSize(wx.Size(self.layout.overall_width, self.layout.height))

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

    def validate(self):
        pass
