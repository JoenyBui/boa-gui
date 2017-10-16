import wx

from ..form.general import GeneralDialog
from ..textbox import LayoutDimensions
from ..textbox.textbox import TextInputLayout, TextSmartBox
from ..textbox.floatbox import FloatInputLayout, FloatSmartBox
from ..controller import ChildController

from ..model.bind import BindObject

__author__ = 'jbui'

ID_AXES_SCALE_LINEAR = 'linear'
ID_AXES_SCALE_LOG = 'log'
ID_AXES_SCALE_SYMLOG = 'symlog'
ID_AXES_SCALE_LOGIT = 'logit'


class FigureSetting(object):
    """
    Figure Setting model.

    """
    def __init__(self, *args, **kwargs):
        """
        Figure Setting Constructor

        :param args:
        :param kwargs:
        :return:
        """
        self.title = kwargs.get('title', 'Title')
        self.x_label = kwargs.get('x_label', 'X Title')
        self.x_sublabel = kwargs.get('x_sublabel', '')
        self.y_label = kwargs.get('y_label', 'Y Title')
        self.y_sublabel = kwargs.get('y_sublabel', '')

        self.x_min = kwargs.get('x_min', None)
        self.x_max = kwargs.get('x_max', None)
        self.y_min = kwargs.get('y_min', None)
        self.y_max = kwargs.get('y_max', None)

        self.x_scale = kwargs.get('x_scale', 'linear')
        self.y_scale = kwargs.get('y_scale', 'linear')

        self.linewidth = kwargs.get('linewidth', 2)
        self.legend = kwargs.get('legend', [])

        self.show_origin_axis = kwargs.get('show_origin_axis')
        self.grid = kwargs.get('grid')
        self.grid_minor = kwargs.get('grid_minor')
        self.margin = kwargs.get('margin')


class FigureSettingPanel(wx.Panel):
    """
    Particular Figure Setting

    """
    def __init__(self, parent, setting, *args, **kwargs):
        """

        :param setting:
        :param args:
        :param kwargs:
        :return:
        """
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.layouts = {}
        self.bind_objects = {}

        self.setting = setting

        self.SetSizerAndFit(self.do_layout())

    def do_layout(self):
        """
        Layout form

        :return:
        """
        vsizer = wx.BoxSizer(wx.VERTICAL)

        layout = LayoutDimensions(top=2, bottom=2, left=4, right=4, interior=2,
                                  widths=(100, 200),
                                  stretch_factor=(0, 1), height=24)
        layout.calculate()

        self.layouts['title'] = TextInputLayout(self,
                                                name='Title',
                                                layout=layout,
                                                textbox=TextSmartBox(self))
        self.layouts['x_label'] = TextInputLayout(self,
                                                  name='X Label',
                                                  layout=layout,
                                                  textbox=TextSmartBox(self))
        self.layouts['y_label'] = TextInputLayout(self,
                                                  name='Y Label',
                                                  layout=layout,
                                                  textbox=TextSmartBox(self))

        self.layouts['x_min'] = FloatInputLayout(self,
                                                 name='X Min',
                                                 layout=layout,
                                                 textbox=FloatSmartBox(self, signs=True))

        self.layouts['x_max'] = FloatInputLayout(self,
                                                 name='X Max',
                                                 layout=layout,
                                                 textbox=FloatSmartBox(self, signs=True))

        self.layouts['y_min'] = FloatInputLayout(self,
                                                 name='Y Min',
                                                 layout=layout,
                                                 textbox=FloatSmartBox(self, signs=True))

        self.layouts['y_max'] = FloatInputLayout(self,
                                                 name='Y Max',
                                                 layout=layout,
                                                 textbox=FloatSmartBox(self, signs=True))

        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['title'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['x_label'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['y_label'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['x_min'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['x_max'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['y_min'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['y_max'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)

        return vsizer

    def sync_data(self):
        """
        Sync textbox data

        """
        self.bind_objects['title'] = BindObject(self.setting.__dict__,
                                                self.layouts['title'].textbox,
                                                'title')
        self.bind_objects['x_label'] = BindObject(self.setting.__dict__,
                                                  self.layouts['x_label'].textbox,
                                                  'x_label')
        self.bind_objects['y_label'] = BindObject(self.setting.__dict__,
                                                  self.layouts['y_label'].textbox,
                                                  'y_label')
        self.bind_objects['x_min'] = BindObject(self.setting.__dict__,
                                                self.layouts['x_min'].textbox,
                                                'x_min')
        self.bind_objects['x_max'] = BindObject(self.setting.__dict__,
                                                self.layouts['x_max'].textbox,
                                                'x_max')
        self.bind_objects['y_min'] = BindObject(self.setting.__dict__,
                                                self.layouts['y_min'].textbox,
                                                'y_min')
        self.bind_objects['y_max'] = BindObject(self.setting.__dict__,
                                                self.layouts['y_max'].textbox,
                                                'y_max')


class FigureSettingDialog(GeneralDialog):
    """
    Modify figure setting.

    """
    def __init__(self, parent, controller=None, setting=None, local=None, btn_flags=wx.OK | wx.CANCEL, **kwargs):
        """
        Figure setting dialog.

        :param parent:
        :param controller:
        :param setting:
        :param btn_flags:
        :param kwargs:
        :return:
        """
        self.nb = None
        self.pages = {}

        if local:
            self.local = local
            self.local.view = self
        else:
            self.local = FigureSettingController(parent, self, setting)

        GeneralDialog.__init__(self,
                               parent,
                               title="Figure Setting",
                               style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
                               controller=controller,
                               local=self.local,
                               btn_flags=btn_flags,
                               **kwargs)

        self.btnsizer.AffirmativeButton.Bind(wx.EVT_BUTTON, self.local.button_ok_click)

    def do_layout(self):
        """
        Draw layout

        :return:
        """
        self.nb = wx.Notebook(self)

        for index, setting in enumerate(self.local.settings):
            # Create Panel.
            self.pages[index] = FigureSettingPanel(self.nb, setting)

            # Add to tab page.
            self.nb.AddPage(self.pages[index], "Plot %d" % (index + 1))

            # Sync Data
            self.pages[index].sync_data()

        return self.nb


class FigureSettingController(ChildController):
    """
    Figure Setting Controller

    """
    def __init__(self, parent, view, settings):
        """

        :param parent:
        :param view:
        :return:
        """
        ChildController.__init__(self, parent, view, settings)

        self.settings = settings

    def sync_data(self):
        """
        Sync Data

        :return:
        """
        pass

    def do_layout(self):
        pass

    def refresh(self):
        pass

    def update_layout(self, state):
        pass

    def button_ok_click(self, event):
        """
        Button ok click

        :param event:
        :return:
        """
        error = False

        #TODO: Need to bind the textbox with the data.

        if error is False:
            event.Skip()
        else:
            if not wx.Validator_IsSilent():
                wx.Bell()

    def delete_control(self):
        pass

# import wx
#
# from ..form.general import GeneralDialog
# from ..textbox import LayoutDimensions
# from ..textbox.textbox import TextInputLayout, TextSmartBox
# from ..textbox.floatbox import FloatInputLayout, FloatSmartBox
# from ..controller import ChildController
#
# from ..model.bind import BindOjbect
#
# __author__ = 'Joeny'
#
#
# class FigureSetting(object):
#     """
#     Figure Setting model.
#
#     """
#     def __init__(self, *args, **kwargs):
#         """
#         Figure Setting Constructor
#
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         self.title = kwargs.get('title', 'Title')
#         self.x_title = kwargs.get('x_title', 'X Title')
#         self.x_subtitle = kwargs.get('x_subtitle', '')
#         self.y_title = kwargs.get('y_title', 'Y Title')
#         self.y_subtitle = kwargs.get('y_subtitle', '')
#
#         self.x_min = kwargs.get('x_min', None)
#         self.x_max = kwargs.get('x_max', None)
#         self.y_min = kwargs.get('y_min', None)
#         self.y_max = kwargs.get('y_max', None)
#
#         self.linewidth = kwargs.get('linewidth', 2)
#         self.legend = kwargs.get('legend', [])
#
#
# class FigureSettingPanel(wx.Panel):
#     """
#     Particular Figure Setting
#
#     """
#     def __init__(self, parent, setting, *args, **kwargs):
#         """
#
#         :param setting:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         wx.Panel.__init__(self, parent, *args, **kwargs)
#
#         self.layouts = {}
#         self.bind_objects = {}
#
#         self.setting = setting
#
#         self.SetSizerAndFit(self.do_layout())
#
#     def do_layout(self):
#         """
#         Layout form
#
#         :return:
#         """
#         vsizer = wx.BoxSizer(wx.VERTICAL)
#
#         layout = LayoutDimensions(top=2, bottom=2, left=4, right=4, interior=2,
#                                   widths=(100, 200),
#                                   stretch_factor=(0, 1), height=24)
#         layout.calculate()
#
#         self.layouts['title'] = TextInputLayout(self,
#                                                 name='Title',
#                                                 layout=layout,
#                                                 textbox=TextSmartBox(self))
#         self.layouts['x_title'] = TextInputLayout(self,
#                                                   name='X Title',
#                                                   layout=layout,
#                                                   textbox=TextSmartBox(self))
#         self.layouts['y_title'] = TextInputLayout(self,
#                                                   name='Y Title',
#                                                   layout=layout,
#                                                   textbox=TextSmartBox(self))
#
#         self.layouts['x_min'] = FloatInputLayout(self,
#                                                  name='X Min',
#                                                  layout=layout,
#                                                  textbox=FloatSmartBox(self, signs=True))
#
#         self.layouts['x_max'] = FloatInputLayout(self,
#                                                  name='X Max',
#                                                  layout=layout,
#                                                  textbox=FloatSmartBox(self, signs=True))
#
#         self.layouts['y_min'] = FloatInputLayout(self,
#                                                  name='Y Min',
#                                                  layout=layout,
#                                                  textbox=FloatSmartBox(self, signs=True))
#
#         self.layouts['y_max'] = FloatInputLayout(self,
#                                                  name='Y Max',
#                                                  layout=layout,
#                                                  textbox=FloatSmartBox(self, signs=True))
#
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['title'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['x_title'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['y_title'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['x_min'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['x_max'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['y_min'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#         vsizer.Add(self.layouts['y_max'], 1, wx.EXPAND | wx.ALL, 0)
#         vsizer.AddSpacer(5)
#
#         return vsizer
#
#     def sync_data(self):
#         """
#         Sync textbox data
#
#         """
#         self.bind_objects['title'] = BindOjbect(self.setting.__dict__,
#                                                 self.layouts['title'].textbox,
#                                                 'title')
#         self.bind_objects['x_title'] = BindOjbect(self.setting.__dict__,
#                                                   self.layouts['x_title'].textbox,
#                                                   'x_title')
#         self.bind_objects['y_title'] = BindOjbect(self.setting.__dict__,
#                                                   self.layouts['y_title'].textbox,
#                                                   'y_title')
#         self.bind_objects['x_min'] = BindOjbect(self.setting.__dict__,
#                                                 self.layouts['x_min'].textbox,
#                                                 'x_min')
#         self.bind_objects['x_max'] = BindOjbect(self.setting.__dict__,
#                                                 self.layouts['x_max'].textbox,
#                                                 'x_max')
#         self.bind_objects['y_min'] = BindOjbect(self.setting.__dict__,
#                                                 self.layouts['y_min'].textbox,
#                                                 'y_min')
#         self.bind_objects['y_max'] = BindOjbect(self.setting.__dict__,
#                                                 self.layouts['y_max'].textbox,
#                                                 'y_max')
#
#
# class FigureSettingDialog(GeneralDialog):
#     """
#     Modify figure setting.
#
#     """
#     def __init__(self, parent, controller=None, setting=None, local=None, btn_flags=wx.OK | wx.CANCEL, **kwargs):
#         """
#         Figure setting dialog.
#
#         :param parent:
#         :param controller:
#         :param setting:
#         :param btn_flags:
#         :param kwargs:
#         :return:
#         """
#         self.nb = None
#         self.pages = {}
#
#         if local:
#             self.local = local
#             self.local.view = self
#         else:
#             self.local = FigureSettingController(parent, self, setting)
#
#         GeneralDialog.__init__(self,
#                                parent,
#                                title="Figure Setting",
#                                style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
#                                controller=controller,
#                                local=self.local,
#                                btn_flags=btn_flags,
#                                **kwargs)
#
#         self.btnsizer.AffirmativeButton.Bind(wx.EVT_BUTTON, self.local.button_ok_click)
#
#     def do_layout(self):
#         """
#         Draw layout
#
#         :return:
#         """
#         self.nb = wx.Notebook(self)
#
#         for index, setting in enumerate(self.local.settings):
#             # Create Panel.
#             self.pages[index] = FigureSettingPanel(self.nb, setting)
#
#             # Add to tab page.
#             self.nb.AddPage(self.pages[index], "Plot %d" % (index + 1))
#
#             # Sync Data
#             self.pages[index].sync_data()
#
#         return self.nb
#
#
# class FigureSettingController(ChildController):
#     """
#     Figure Setting Controller
#
#     """
#     def __init__(self, parent, view, settings):
#         """
#
#         :param parent:
#         :param view:
#         :return:
#         """
#         ChildController.__init__(self, parent, view, settings)
#
#         self.settings = settings
#
#     def sync_data(self):
#         """
#         Sync Data
#
#         :return:
#         """
#         pass
#
#     def do_layout(self):
#         pass
#
#     def refresh(self):
#         pass
#
#     def update_layout(self, state):
#         pass
#
#     def button_ok_click(self, event):
#         """
#         Button ok click
#
#         :param event:
#         :return:
#         """
#         error = False
#
#         #TODO: Need to bind the textbox with the data.
#
#         if error is False:
#             event.Skip()
#         else:
#             if not wx.Validator_IsSilent():
#                 wx.Bell()
#
#     def delete_control(self):
#         pass
