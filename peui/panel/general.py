import wx

from ..textbox.smart import SmartComboBox
from ..textbox.floatbox import FloatSmartBox, FloatInputLayout
from ..textbox.intbox import IntSmartBox, IntInputLayout

__author__ = 'jbui'


class GeneralPanel(wx.Panel):

    def __init__(self, parent=None, **kwargs):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.layouts = {}

        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.Add(self.do_layout())

        self.SetSizer(vsizer)

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        self.layouts['float'] = FloatInputLayout(self, name='Float',
                                                 textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                 postbox=SmartComboBox(self))

        self.layouts['int'] = IntInputLayout(self, name='Int',
                                             textbox=IntSmartBox(self, signs=True),
                                             postbox=SmartComboBox(self))

        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['float'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['int'], 0, wx.EXPAND | wx.ALL, 5)

        return vsizer


