import wx

from ..form.general import GeneralDialog
from ..textbox.textbox import TextInputLayout, TextSmartBox
from ..controller import ChildController

__author__ = 'jbui'


class FigureSetting(object):

    def __init__(self):
        self.title = 'Title'
        self.x_title = 'X Title'
        self.x_subtitle = ''
        self.y_title = 'Y Title'
        self.y_subtitle = ''


class FigureSettingDialog(GeneralDialog):

    def __init__(self, parent, controller=None, setting=None, btn_flags=wx.OK | wx.CANCEL, **kwargs):
        self.setting = setting

        GeneralDialog.__init__(self, parent, controller=controller, btn_flags=btn_flags, **kwargs)

        self.btnsizer.AffirmativeButton.Bind(wx.EVT_BUTTON, self.button_ok_click)

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        self.layouts['title'] = TextInputLayout(self, label='Title', textbox=TextSmartBox(self, value=self.setting.title))
        self.layouts['x_title'] = TextInputLayout(self, label='X Title', textbox=TextSmartBox(self, value=self.setting.x_title))
        self.layouts['x_subtitle'] = TextInputLayout(self, label='X SubTitle', textbox=TextSmartBox(self, value=self.setting.x_subtitle))
        self.layouts['y_title'] = TextInputLayout(self, label='Y Title', textbox=TextSmartBox(self, value=self.setting.y_title))
        self.layouts['y_subtitle'] = TextInputLayout(self, label='Y SubTitle', textbox=TextSmartBox(self, value=self.setting.y_subtitle))

        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['title'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['x_title'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['x_subtitle'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['y_title'], 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddSpacer(10)
        vsizer.Add(self.layouts['y_subtitle'], 0, wx.EXPAND | wx.ALL, 5)

        return vsizer

    def button_ok_click(self, event):
        error = False

        #TODO: Need to bind the textbox with the data.

        if error is False:
            event.Skip()
        else:
            if not wx.Validator_IsSilent():
                wx.Bell()


class FigureSettingController(ChildController):

    def __init__(self, parent, view):
        ChildController.__init__(self, parent, view)

        self.figure_setting = FigureSetting()

    def sync_data(self):
        self.register_two_way_bind(
            self.view.layout['title'],
            self.figure_setting.title
        )

    def bind_textctrl_model(self):
        pass
