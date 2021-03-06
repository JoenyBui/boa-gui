import wx

from wx.lib.agw.supertooltip import SuperToolTip

from . import LayoutDimensions
from .smart import SmartComboBox, SmartInputLayout
from ..types import is_int

__author__ = 'Joeny'


class ComboBoxInputLayout(SmartInputLayout):
    """
    ComboBox Input Layout

    """

    def __init__(self, parent, combobox=None, event_on_select=None, event_text_change=None, layout=None, *args, **kwargs):
        """
        Combobox input layout.

        :param parent: main form
        :param combobox:
        :param event_on_select:
        :param layout:
        :param args:
        :param kwargs:
        :return:
        """
        SmartInputLayout.__init__(self, parent, event_on_select=event_on_select, layout=layout, *args, **kwargs)

        # Establish the combobox.
        if combobox:
            self.combobox = combobox
        else:
            self.combobox = SmartComboBox(self)

        if event_on_select:
            self.combobox.Bind(wx.EVT_COMBOBOX, event_on_select)

        if event_text_change:
            self.combobox.Bind(wx.EVT_TEXT, event_text_change)

        self.do_layout()

    def get_value(self):
        """
        Get the combobox value.

        :return:
        """
        return self.combobox.Value

    def set_value(self, value, label=None):
        """
        Set the combobox value.

        :param value:
        :param label:
        :return:
        """
        if value:
            self.combobox.Value = str(value)

        if label:
            self.label.Label = str(label)

    def set_list(self, list_values):
        """
        Set the list.

        :param list_values:
        :return:
        """
        self.combobox.SetItems(list_values)

    def set_dict(self, dict_values):
        """
        Set the combobox with a new dictionary set.

        :param dict_values:
        :return:
        """
        self.combobox.Clear()

        for key, index in dict_values.items():
            self.append(index, key)

    def set_selection(self, value):
        """
        Set the selection value.

        :param value: index
        :return:
        """
        if value is not None:
            if is_int(value):
                self.combobox.SetSelection(value)

    def set_selection_by_data(self, value):
        """
        Set the selection given the data input.

        :param value:
        :return:
        """
        self.combobox.set_selection_by_data(value)

    def append(self, label, obj):
        """
        Append data into combobox.

        :param label: title
        :param obj: object data
        :return:
        """
        self.combobox.Append(label, obj)

    def get_data(self):
        """
        Get the data.

        :return:
        """
        return self.combobox.GetClientData(self.combobox.GetSelection())

    def enable(self):
        """
        Enable textbox and/or postbox.

        :return:
        """
        if self.combobox:
            self.combobox.Enable(True)

    def disable(self):
        """
        Disable textbox and/or postbox.

        :return:
        """
        if self.combobox:
            self.combobox.Disable()
