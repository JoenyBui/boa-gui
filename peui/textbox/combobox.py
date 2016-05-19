import wx

from wx.lib.agw.supertooltip import SuperToolTip

from .smart import SmartComboBox, SmartInputLayout

__author__ = 'jbui'


class ComboBoxInputLayout(wx.BoxSizer):
    """
    ComboBox Input Layout
    """
    def __init__(self, parent, label_width=150, *args, **kwargs):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)

        self.parent = parent

        label_width = label_width

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

        self.combobox = kwargs.get('combobox', None)
        self.tooltip = kwargs.get('tooltip', SuperToolTip)

        # Call do_layout after you have populate the label, textbox, and/or postbox
        self.border_space = kwargs.get('border_space', 10)
        self.border_space_label = kwargs.get('border_space_label', self.border_space)
        self.border_space_textbox = kwargs.get('border_space_textbox', self.border_space)
        self.border_space_postbox = kwargs.get('border_space_postbox', self.border_space)

        self.do_layout()

    def do_layout(self):

        if self.label:
            self.Add(self.label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, self.border_space_label)
            # self.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_label)

        if self.combobox:
            # self.Add(self.combobox, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, self.border_space_postbox)
            self.Add(self.combobox, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, self.border_space_postbox)

        self.AddStretchSpacer()

    def set_value(self, value, label=None):
        if value:
            self.combobox.Value = str(value)

        if label:
            self.label.Label = str(label)
