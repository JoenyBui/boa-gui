import sys
import wx

from ..controller import ChildController

__author__ = 'jbui'


class Console(wx.Panel):
    """
    Output console info.

    """
    def __init__(self, parent, controller, local=None):
        """

        :param parent:
        :param controller:
        :param local:
        :return:
        """
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        # Add a panel so it looks the correct on all platforms
        style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
        log = wx.TextCtrl(self, wx.ID_ANY, size=(800, 300), style=style)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(sizer)

        log.BackgroundColour = wx.BLACK
        log.ForegroundColour = wx.WHITE

        # redirect text here
        sys.stdout = log

        if local:
            self.controller = local
        else:
            self.controller = ConsoleController(controller, self)

        self.parent = parent


class ConsoleController(ChildController):
    """

    """
    def __init__(self, parent, view):
        """

        :param parent:
        :param view:
        :return:
        """
        ChildController.__init__(self, parent, view)

    def do_layout(self):
        """

        :return:
        """
        pass

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

    def sync_data(self):
        """

        :return:
        """
        pass