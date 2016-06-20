import wx

from wx.lib.agw.supertooltip import SuperToolTip

from . import LayoutDimensions
from .smart import SmartComboBox, SmartInputLayout

__author__ = 'jbui'


class ComboBoxInputLayout(SmartInputLayout):
    """
    ComboBox Input Layout

    """

    def __init__(self, parent, event_on_select=None, layout=None, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, event_on_select=event_on_select, layout=layout, *args, **kwargs)
        #
        # self.parent = parent
        # self.hsizer = None

        # self.ID_LABEL = None

        # if layout:
        #     self.layout = layout
        # else:
        #     self.layout = LayoutDimensions()

        label_width = self.layout.widths[0]
        cb_width = self.layout.widths[1]

        # Establish the label.
        # if kwargs.get('label'):
        #     self.label = kwargs.get('label')
        # else:
        #     if kwargs.get('name'):
        #         self.label = wx.StaticText(self.parent,
        #                                    label=kwargs.get('name'),
        #                                    size=(label_width, self.layout.height))
        #     else:
        #         self.label = wx.StaticText(self.parent,
        #                                    label="TextBox Label:",
        #                                    size=(label_width, self.layout.height))

        # Establish the combobox.
        self.combobox = kwargs.get('combobox', None)
        if self.combobox:
            self.combobox.SetSize(wx.BoxSizer(cb_width, self.layout.height))

        if event_on_select:
            self.combobox.Bind(wx.EVT_COMBOBOX, event_on_select)

        # self.tooltip = kwargs.get('tooltip', SuperToolTip)
        #
        # # Call do_layout after you have populate the label, textbox, and/or postbox
        # self.border_space = kwargs.get('border_space', 10)
        # self.border_space_label = kwargs.get('border_space_label', self.border_space)
        # self.border_space_textbox = kwargs.get('border_space_textbox', self.border_space)
        # self.border_space_postbox = kwargs.get('border_space_postbox', self.border_space)

        self.do_layout()

    # def do_layout(self):
    #     """
    #
    #     :return:
    #     """
    #     if self.label:
    #         self.Add(self.label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, self.border_space_label)
    #         # self.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_label)
    #
    #     if self.combobox:
    #         # self.Add(self.combobox, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_postbox)
    #         self.Add(self.combobox, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, self.border_space_postbox)
    #
    #     self.AddStretchSpacer()

    def get_value(self):
        """

        :return:
        """
        return self.combobox.Value

    def set_value(self, value, label=None):
        """

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

        :param list_values:
        :return:
        """
        self.combobox.SetItems(list_values)

    def set_selection(self, value):
        """

        :param value:
        :return:
        """
        self.combobox.SetSelection(value)

    def append(self, label, obj):
        """

        :param label:
        :param obj:
        :return:
        """
        self.combobox.Append(label, obj)

    def get_data(self):
        """

        :return:
        """
        return self.combobox.GetClientData(self.combobox.GetSelection())
