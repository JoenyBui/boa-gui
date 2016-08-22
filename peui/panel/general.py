import copy

import wx

from ..textbox import LayoutDimensions
from ..textbox.smart import SmartComboBox, SmartButton
from ..textbox.floatbox import FloatSmartBox, FloatInputLayout
from ..textbox.intbox import IntSmartBox, IntInputLayout
from ..textbox.combobox import ComboBoxInputLayout

__author__ = 'jbui'


class GeneralPanel(wx.ScrolledWindow):
    """

    """
    def __init__(self, parent=None, **kwargs):
        """

        :param parent:
        :param kwargs:
        :return:
        """
        wx.ScrolledWindow.__init__(self, parent=parent, id=wx.ID_ANY, style=wx.VSCROLL)
        self.SetScrollRate(5, 5)

        self.layouts = {}

        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.Add(self.do_layout(), 1, wx.EXPAND | wx.ALL, 1)

        self.SetSizer(vsizer)

    def do_layout(self):
        """

        :return:
        """
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

        self.layouts['int'] = IntInputLayout(self, name='Int', value=100, unit='str',
                                             textbox=IntSmartBox(self, signs=True, message="Input Layout"),
                                             postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        self.layouts['combobox'] = ComboBoxInputLayout(self, name='ComboBox',
                                                       combobox=SmartComboBox(self, message='I am a combobox'),
                                                       layout=cd)

        # Add Unit ComboBox.
        self.layouts['acceleration'] = FloatInputLayout(self,
                                                        name='Acceleration', type='acceleration',
                                                        value=105.5, unit='TNT',
                                                        textbox=FloatSmartBox(self, message='Acceleration'),
                                                        postbox=SmartComboBox(self),
                                                        layout=ld)

        self.layouts['area'] = FloatInputLayout(self,
                                                name='Area', type='area',
                                                value=105.5, unit='TNT',
                                                textbox=FloatSmartBox(self),
                                                postbox=SmartComboBox(self),
                                                layout=ld)

        self.layouts['charge'] = FloatInputLayout(self,
                                                  name='Charge Weight', type='charge',
                                                  value=105.5, unit='TNT',
                                                  textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True, message='Charge Layout'),
                                                  postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                  layout=ld)

        self.layouts['density'] = FloatInputLayout(self,
                                                   name='Density', type='density',
                                                   value=105.5, unit='TNT',
                                                   textbox=FloatSmartBox(self),
                                                   postbox=SmartComboBox(self),
                                                   layout=ld)

        self.layouts['force'] = FloatInputLayout(self,
                                                 name='Force', type='force',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['inertia'] = FloatInputLayout(self,
                                                 name='Inertia', type='inertia',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['length'] = FloatInputLayout(self, name='Length', type='length',
                                                 textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                 postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                 layout=ld)

        self.layouts['linear_density'] = FloatInputLayout(self,
                                                 name='Linear Density', type='linear_density',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['linear_pressure'] = FloatInputLayout(self,
                                                 name='Linear Pressure', type='linear_pressure',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['mass'] = FloatInputLayout(self,
                                                name='Mass', type='mass', value=60, unit='lbm',
                                                textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                layout=ld)

        self.layouts['pressure'] = FloatInputLayout(self,
                                                    name='Pressure', type='pressure',
                                                    textbox=FloatSmartBox(self, signs=True, decimal=True, exponential=True),
                                                    postbox=SmartComboBox(self, style=wx.CB_READONLY),
                                                    layout=ld)

        self.layouts['time'] = FloatInputLayout(self,
                                                 name='Time', type='time',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['tnt'] = FloatInputLayout(self,
                                                 name='Tnt', type='tnt',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['torque'] = FloatInputLayout(self,
                                                 name='Torque', type='torque',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['velocity'] = FloatInputLayout(self,
                                                 name='Velocity', type='velocity',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        self.layouts['volume'] = FloatInputLayout(self,
                                                 name='Volume', type='volume',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self),
                                                 postbox=SmartComboBox(self),
                                                 layout=ld)

        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['int'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['combobox'], 0, wx.EXPAND | wx.ALL, 5)

        vsizer.Add(wx.StaticText(self, label='Units'), 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['acceleration'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['area'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['charge'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['density'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['force'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['inertia'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['length'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['linear_density'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['linear_pressure'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['mass'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['pressure'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['time'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['tnt'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['torque'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['velocity'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['volume'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)

        self.layouts['btn'] = SmartButton(self, id=wx.ID_ANY, style=0, label='Click Me')

        vsizer.Add(self.layouts['btn'])

        return vsizer


