import wx

from ..form.general import GeneralDialog
from ..textbox import LayoutDimensions
from ..textbox.textbox import TextInputLayout, TextSmartBox
from ..controller import ChildController

from ..model.bind import BindOjbect

__author__ = 'jbui'


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
        self.x_title = kwargs.get('x_title', 'X Title')
        self.x_subtitle = kwargs.get('x_subtitle', '')
        self.y_title = kwargs.get('y_title', 'Y Title')
        self.y_subtitle = kwargs.get('y_subtitle', '')


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
        GeneralDialog.__init__(self, parent, title="Figure Setting", controller=controller, btn_flags=btn_flags, **kwargs)

        self.btnsizer.AffirmativeButton.Bind(wx.EVT_BUTTON, self.button_ok_click)

        if local:
            self.local = local
        else:
            self.local = FigureSettingController(self.parent, self, setting)

        self.local.sync_data()

    def do_layout(self):
        """
        Layout form

        :return:
        """
        vsizer = wx.BoxSizer(wx.VERTICAL)

        layout = LayoutDimensions(top=2, bottom=2, left=4, right=4, interior=2, widths=(100, 200), height=24)
        layout.calculate()

        self.layouts['title'] = TextInputLayout(self,
                                                name='Title',
                                                layout=layout,
                                                textbox=TextSmartBox(self))
        self.layouts['x_title'] = TextInputLayout(self,
                                                  name='X Title',
                                                  layout=layout,
                                                  textbox=TextSmartBox(self))
        self.layouts['y_title'] = TextInputLayout(self,
                                                  name='Y Title',
                                                  layout=layout,
                                                  textbox=TextSmartBox(self))

        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['title'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['x_title'], 1, wx.EXPAND | wx.ALL, 0)
        vsizer.AddSpacer(5)
        vsizer.Add(self.layouts['y_title'], 1, wx.EXPAND | wx.ALL, 0)

        return vsizer

    def button_ok_click(self, event):
        """

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
        ChildController.__init__(self, parent, view)

        self.setting = FigureSetting()

    def sync_data(self):
        """
        Sync Data

        :return:
        """
        self.bind_objects['title'] = BindOjbect(self.setting.__dict__,
                                                self.view.layouts['title'].textbox,
                                                'title')
        self.bind_objects['x_title'] = BindOjbect(self.setting.__dict__,
                                                  self.view.layouts['x_title'].textbox,
                                                  'x_title')
        self.bind_objects['y_title'] = BindOjbect(self.setting.__dict__,
                                                  self.view.layouts['y_title'].textbox,
                                                  'y_title')

    def do_layout(self):
        pass

    def refresh(self):
        pass

    def update_layout(self):
        pass
