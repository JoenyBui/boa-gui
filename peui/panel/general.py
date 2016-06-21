import copy

import wx

from ..textbox import LayoutDimensions
from ..textbox.smart import SmartComboBox
from ..textbox.floatbox import FloatSmartBox, FloatInputLayout
from ..textbox.intbox import IntSmartBox, IntInputLayout
from ..textbox.combobox import ComboBoxInputLayout

__author__ = 'jbui'


class GeneralPanel(wx.Panel):

    def __init__(self, parent=None, **kwargs):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.layouts = {}

        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.Add(self.do_layout(), 1, wx.EXPAND | wx.ALL, 1)

        self.SetSizer(vsizer)

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        ld = LayoutDimensions()
        ld.top = 2
        ld.bottom = 2
        ld.right = 2
        ld.left = 2
        ld.height = 26
        ld.widths = (150, 300, 60)
        ld.interior = 3
        ld.stretch_factor = (0, 0, 0)
        ld.calculate()

        cd = copy.deepcopy(ld)
        cd.widths = (150, 300)
        cd.calculate()

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
                                                  textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True, message='Charge Layout'),
                                                  postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                  layout=ld)

        self.layouts['int'] = IntInputLayout(self, name='Int', value=100, unit='str',
                                             textbox=IntSmartBox(self, signs=True, message="Input Layout"),
                                             postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        self.layouts['combobox'] = ComboBoxInputLayout(self, name='ComboBox',
                                                       combobox=SmartComboBox(self),
                                                       layout=cd)

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
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['combobox'], 0, wx.EXPAND | wx.ALL, 5)

        self.layouts['btn'] = wx.Button(self, id=wx.ID_ANY, style=0, name='Click Me')

        vsizer.Add(self.layouts['btn'])

        return vsizer


