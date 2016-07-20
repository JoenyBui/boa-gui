import wx

from peui.textbox import LayoutDimensions
from peui.textbox.floatbox import FloatInputLayout
from peui.textbox.pathbox import PathInputLayout, PathSmartBox
from peui.textbox.smart import SmartComboBox
from peui.textbox.textbox import TextInputLayout

from ..controller import ChildController

__author__ = 'jbui'


class BaseSettingDialog(wx.Dialog):
    """
    Base Setting Dialog form that should be inherited.

    """
    def __init__(self, parent, controller=None, local=None, btn_flags=wx.SAVE | wx.CANCEL, title='Setting Dialog', **kwargs):
        """
        Constructor

        :param parent:
        :param controller:
        :param local:
        :param btn_flags:
        :param title:
        :param kwargs:
        :return:
        """

        wx.Dialog.__init__(self, parent, title=title, **kwargs)

        self.parent = parent
        self.controller = controller

        self.nb = wx.Notebook(self)
        if local:
            self.local = local
        else:
            self.local = ControllerBaseDialog(controller, self)

        self.layouts = {}

        self.btnsizer = self.CreateButtonSizer(btn_flags)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.local.do_layout(), 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddStretchSpacer()
        vsizer.Add(self.btnsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.Bind(wx.EVT_BUTTON, self.on_okay, id=wx.ID_SAVE)
        self.SetSizer(vsizer)
        self.SetInitialSize()
        self.CenterOnParent()
        self.Fit()

        self.local.load_component()

    def on_okay(self, event):
        """
        On okay event.

        :param event:
        :return:
        """
        self.local.set_component()

        event.Skip()


class ControllerBaseDialog(ChildController):
    """
    Controller for the Base Setting Dialog.

    To customize for each project, must inherit.

    """
    def __init__(self, parent, view, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param view:
        :param scenario:
        :param unit_system:
        :param args:
        :param kwargs:
        :return:
        """
        ChildController.__init__(self, parent, view, *args, **kwargs)

        self.parent = parent
        self.view = view

    def sync_data(self):
        pass

    def settings_layout(self, parent_pnl):
        """
        Material Layout
        """
        # Panel
        pnl = wx.ScrolledWindow(parent_pnl, id=wx.ID_ANY, style=wx.VSCROLL)
        pnl.SetScrollRate(5, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)

        tb_layout = LayoutDimensions(top=2, bottom=2, right=4, left=4, widths=(150, 195, 75), interior=5,
                                     stretch_factor=(1, 0, 0))
        tb_layout.calculate()
        cb_layout = LayoutDimensions(top=2, bottom=2, right=4, left=4, widths=(150, 275), interior=5,
                                     stretch_factor=(1, 0))
        cb_layout.calculate()

        # Author
        self.view.layouts['author'] = TextInputLayout(pnl, name='Author:', layout=cb_layout)

        # Project Name
        self.view.layouts['project_name'] = TextInputLayout(pnl, name='Project Name:', layout=cb_layout)

        # Path
        self.view.layouts['path'] = PathInputLayout(pnl, name='Path:', layout=tb_layout)

        # E-Signature
        self.view.layouts['esignature'] = PathInputLayout(pnl, name='E-Signature:', layout=tb_layout, is_file=True)

        # E-Key
        self.view.layouts['ekey'] = PathInputLayout(pnl, name='E-Key:', layout=tb_layout, is_file=True)

        # E-File
        self.view.layouts['efile'] = PathInputLayout(pnl, name='E-File:', layout=tb_layout, is_file=True)

        sizer.AddSpacer(5)
        sizer.Add(self.view.layouts['author'], 0, wx.ALL | wx.EXPAND, 0)
        sizer.AddSpacer(5)
        sizer.Add(self.view.layouts['project_name'], 0, wx.ALL | wx.EXPAND, 0)
        sizer.AddSpacer(5)
        sizer.Add(self.view.layouts['path'], 0, wx.ALL | wx.EXPAND, 0)
        sizer.AddSpacer(5)
        sizer.Add(self.view.layouts['esignature'], 0, wx.ALL | wx.EXPAND, 0)
        sizer.AddSpacer(5)
        sizer.Add(self.view.layouts['ekey'], 0, wx.ALL | wx.EXPAND, 0)
        sizer.AddSpacer(5)
        sizer.Add(self.view.layouts['efile'], 0, wx.ALL | wx.EXPAND, 0)
        sizer.AddSpacer(5)
        sizer.AddStretchSpacer(1)

        pnl.SetSizer(sizer)

        return pnl

    def check(self, event=None):
        return 5

    def do_layout(self):
        """

        :return:
        """
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.view.layouts['settings'] = self.settings_layout(self.view.nb)

        self.view.nb.AddPage(self.view.layouts['settings'], 'Settings')

        sizer.Add(self.view.nb, 1, wx.ALL | wx.EXPAND, 0)

        # sizer.SetMinSize(wx.Size(600, 400))

        return sizer

    def load_component(self):
        """

        :return:
        """
        self.view.layouts['author'].textbox.Value = str(self.view.controller.setting.author)
        self.view.layouts['project_name'].textbox.Value = str(self.view.controller.setting.project_name)
        self.view.layouts['path'].textbox.Value = str(self.view.controller.setting.path)
        self.view.layouts['esignature'].textbox.Value = str(self.view.controller.setting.esignature)
        self.view.layouts['ekey'].textbox.Value = str(self.view.controller.setting.ekey)
        self.view.layouts['efile'].textbox.Value = str(self.view.controller.setting.efile)

    def set_component(self):
        """

        :return:
        """
        self.view.controller.setting.author = self.view.layouts['author'].textbox.Value
        self.view.controller.setting.project_name = self.view.layouts['project_name'].textbox.Value
        self.view.controller.setting.path = self.view.layouts['path'].textbox.Value
        self.view.controller.setting.esignature = self.view.layouts['esignature'].textbox.Value
        self.view.controller.setting.ekey = self.view.layouts['ekey'].textbox.Value
        self.view.controller.setting.efile = self.view.layouts['efile'].textbox.Value

    def update_layout(self):
        """

        :return:
        """
        pass

    def refresh(self):
        """

        :return:
        """
        pass

