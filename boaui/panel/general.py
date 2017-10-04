import copy

import wx

from ..textbox import LayoutDimensions
from ..textbox.smart import SmartComboBox, SmartButton
from ..textbox.floatbox import FloatSmartBox, FloatInputLayout
from ..textbox.intbox import IntSmartBox, IntInputLayout
from ..textbox.combobox import ComboBoxInputLayout

from ..controller import TabPageController

__author__ = 'Joeny'


class GeneralPanel(wx.ScrolledWindow):
    """

    """
    def __init__(self, parent=None, *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        :return:
        """
        wx.ScrolledWindow.__init__(self, parent=parent, size=wx.Size(200, 200), id=wx.ID_ANY, style=wx.VSCROLL)

        if kwargs.get('local'):
            self.controller = kwargs.get('local')
            self.controller.view = self
        else:
            controller = kwargs.get('controller')

            self.controller = GeneralChartController(controller, self)

        self.SetScrollRate(5, 5)

        self.layouts = {}

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.controller.do_layout(), 1, wx.EXPAND | wx.ALL, 1)
        self.SetSizerAndFit(self.sizer)
        self.SetAutoLayout(True)

        # if not local
        if hasattr(self.controller, 'sync_data'):
            self.controller.sync_data()


class GeneralChartController(TabPageController):

    def __init__(self, parent, view, *args, **kwargs):
        TabPageController.__init__(self, parent, view, *args, **kwargs)

    def refresh(self):
        pass

    def sync_data(self):
        pass

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

        self.view.layouts['int'] = IntInputLayout(self.view, name='Int', value=100, unit='str',
                                             textbox=IntSmartBox(self.view, signs=True, message="Input Layout"),
                                             postbox=SmartComboBox(self.view, style=wx.CB_READONLY),
                                                 layout=ld)

        self.view.layouts['combobox'] = ComboBoxInputLayout(self.view, name='ComboBox',
                                                       combobox=SmartComboBox(self.view, message='I am a combobox'),
                                                       layout=cd)

        # Add Unit ComboBox.
        self.view.layouts['acceleration'] = FloatInputLayout(self.view,
                                                        name='Acceleration', type='acceleration',
                                                        value=105.5, unit='TNT',
                                                        textbox=FloatSmartBox(self.view, message='Acceleration'),
                                                        postbox=SmartComboBox(self.view),
                                                        layout=ld)

        self.view.layouts['area'] = FloatInputLayout(self.view,
                                                name='Area', type='area',
                                                value=105.5, unit='TNT',
                                                textbox=FloatSmartBox(self.view),
                                                postbox=SmartComboBox(self.view),
                                                layout=ld)

        self.view.layouts['charge'] = FloatInputLayout(self.view,
                                                  name='Charge Weight', type='charge',
                                                  value=105.5, unit='TNT',
                                                  textbox=FloatSmartBox(self.view, signs=True, decimal=True, exponential=True, message='Charge Layout'),
                                                  postbox=SmartComboBox(self.view, style=wx.CB_READONLY),
                                                  layout=ld)

        self.view.layouts['density'] = FloatInputLayout(self.view,
                                                   name='Density', type='density',
                                                   value=105.5, unit='TNT',
                                                   textbox=FloatSmartBox(self.view),
                                                   postbox=SmartComboBox(self.view),
                                                   layout=ld)

        self.view.layouts['force'] = FloatInputLayout(self.view,
                                                 name='Force', type='force',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['inertia'] = FloatInputLayout(self.view,
                                                 name='Inertia', type='inertia',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['length'] = FloatInputLayout(self.view, name='Length', type='length',
                                                 textbox=FloatSmartBox(self.view, signs=True, decimal=True, exponential=True),
                                                 postbox=SmartComboBox(self.view, style=wx.CB_READONLY),
                                                 layout=ld)

        self.view.layouts['linear_density'] = FloatInputLayout(self.view,
                                                 name='Linear Density', type='linear_density',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['linear_pressure'] = FloatInputLayout(self.view,
                                                 name='Linear Pressure', type='linear_pressure',
                                                 value=105.5, unit='TNT',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['mass'] = FloatInputLayout(self.view,
                                                name='Mass', type='mass', value=60, unit='lbm',
                                                textbox=FloatSmartBox(self.view, signs=True, decimal=True, exponential=True),
                                                postbox=SmartComboBox(self.view, style=wx.CB_READONLY),
                                                layout=ld)

        self.view.layouts['pressure'] = FloatInputLayout(self.view,
                                                    name='Pressure', type='pressure',
                                                    textbox=FloatSmartBox(self.view, signs=True, decimal=True, exponential=True),
                                                    postbox=SmartComboBox(self.view, style=wx.CB_READONLY),
                                                    layout=ld)

        self.view.layouts['time'] = FloatInputLayout(self.view,
                                                 name='Time', type='time',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['tnt'] = FloatInputLayout(self.view,
                                                 name='Tnt', type='tnt',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['torque'] = FloatInputLayout(self.view,
                                                 name='Torque', type='torque',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['velocity'] = FloatInputLayout(self.view,
                                                 name='Velocity', type='velocity',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        self.view.layouts['volume'] = FloatInputLayout(self.view,
                                                 name='Volume', type='volume',
                                                 value=105.5, unit='s',
                                                 textbox=FloatSmartBox(self.view),
                                                 postbox=SmartComboBox(self.view),
                                                 layout=ld)

        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['int'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['combobox'], 0, wx.EXPAND | wx.ALL, 5)

        vsizer.Add(wx.StaticText(self.view, label='Units'), 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['acceleration'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['area'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['charge'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['density'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['force'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['inertia'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['length'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['linear_density'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['linear_pressure'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['mass'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['pressure'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['time'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['tnt'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['torque'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['velocity'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)
        vsizer.Add(self.view.layouts['volume'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(5)

        self.view.layouts['btn'] = SmartButton(self.view, id=wx.ID_ANY, style=0, label='Click Me')

        vsizer.Add(self.view.layouts['btn'])

        return vsizer


