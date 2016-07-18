import wx

from ..controller import ChildController

__author__ = 'jbui'


class BaseSettingDialog(wx.Dialog):
    """
    Base Setting Dialog form that should be inherited.

    """
    def __init__(self, parent, controller=None, local=None, btn_flags=wx.OK | wx.CANCEL, **kwargs):

        wx.Dialog.__init__(self, parent, **kwargs)

        self.parent = parent
        self.controller = controller

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

        self.SetSizer(vsizer)
        self.SetInitialSize()
        self.CenterOnParent()
        self.Fit()


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

    def sync_data(self):
        pass

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        return vsizer

    def update_layout(self):
        pass

    def refresh(self):
        pass

