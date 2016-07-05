import wx

from ..textbox.smart import SmartComboBox
from ..textbox.floatbox import FloatSmartBox, FloatInputLayout
from ..textbox.intbox import IntSmartBox, IntInputLayout

__author__ = 'jbui'


class GeneralDialog(wx.Dialog):
    """

    Flags
        wx.OK               Creates an OK button
        wx.CANCEL           Creates a Cancel button
        wx.YES              Creates a Yes button
        wx.NO               Creates a No button
        wx.HELP             Creates a Help button
        wx.NO_DEFAULT       Sets the No button as the default
    """
    def __init__(self, parent, controller=None, local=None, btn_flags=wx.OK | wx.CANCEL, **kwargs):
        wx.Dialog.__init__(self, parent, **kwargs)

        self.parent = parent
        self.controller = controller
        self.local = local
        self.layouts = {}

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)

        self.Bind(wx.EVT_BUTTON, self.on_okay, id=wx.ID_OK)

        self.btnsizer = self.CreateButtonSizer(btn_flags)

        vsizer.Add(self.do_layout(), 0, wx.EXPAND, wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.btnsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(vsizer)
        self.SetInitialSize()
        self.CenterOnParent()
        self.Fit()

    def on_okay(self, event):
        self.local.set_component()
        event.Skip()

    def add_layout(self, key, object):
        self.layouts[key] = object

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        self.layouts['float'] = FloatInputLayout(self, label='Float',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self))

        self.layouts['int'] = IntInputLayout(self, label='Int',
                                             textbox=IntSmartBox(self),
                                             postbox=SmartComboBox(self))

        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['float'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['int'], 0, wx.EXPAND | wx.ALL, 5)

        return vsizer
