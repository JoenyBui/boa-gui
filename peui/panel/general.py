import wx

from ..textbox import LayoutDimensions
from ..textbox.smart import SmartComboBox
from ..textbox.floatbox import FloatSmartBox, FloatInputLayout
from ..textbox.intbox import IntSmartBox, IntInputLayout

__author__ = 'jbui'


class GeneralPanel(wx.Panel):

    def __init__(self, parent=None, **kwargs):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.layouts = {}

        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.Add(self.do_layout(), 1, wx.EXPAND, 1)

        self.SetSizer(vsizer)

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        ld = LayoutDimensions()
        ld.top = 4
        ld.bottom = 4
        ld.right = 4
        ld.left = 4
        ld.overall_width = 600
        ld.overall_height = 40
        ld.height = 30
        ld.widths = (300, 600, 60)
        ld.interior = 5

        self.layouts['length'] = FloatInputLayout(self, name='Length', type='length',
                                                 textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                 postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        self.layouts['pressure'] = FloatInputLayout(self,
                                                    name='Pressure', type='pressure',
                                                    textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                    postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        self.layouts['mass'] = FloatInputLayout(self,
                                                name='Mass', type='mass', value=60, unit='lbm',
                                                textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        self.layouts['charge'] = FloatInputLayout(self,
                                                  name='Charge Weight', type='charge',
                                                  value=105.5, unit='TNT',
                                                  textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                  postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                  layout=ld)

        self.layouts['int'] = IntInputLayout(self, name='Int', value=100, unit='str',
                                             textbox=IntSmartBox(self, signs=True),
                                             postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['length'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['pressure'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['mass'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['charge'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['int'], 0, wx.EXPAND | wx.ALL, 5)

        self.layouts['btn'] = wx.Button(self, id=wx.ID_ANY, style=0, name='Click Me')

        vsizer.Add(self.layouts['btn'])

        return vsizer


