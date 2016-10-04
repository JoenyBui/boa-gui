import sys

import wx
import wx.lib.newevent

from ..controller import PaneController

__author__ = 'jbui'

# Create Event Type
wxLogEvent, EVT_WX_LOG_EVENT = wx.lib.newevent.NewEvent()


class Console(wx.ScrolledWindow):
    """
    Output console info.

    """
    def __init__(self, parent, controller, local=None, *args, **kwargs):
        """

        :param parent:
        :param controller:
        :param local:
        :return:
        """
        wx.ScrolledWindow.__init__(self, parent=parent, size=wx.Size(200, 200), id=wx.ID_ANY, style=wx.VSCROLL)
        self.SetScrollRate(5, 5)

        if local:
            self.controller = local
            self.controller.view = self
        else:
            self.controller = ConsoleController(controller, self, *args, **kwargs)

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


class ConsoleController(PaneController):
    """

    """
    def __init__(self, parent, view, *args, **kwargs):
        """

        :param parent:
        :param view:
        :return:
        """
        PaneController.__init__(self, parent, view, *args, **kwargs)

    def do_layout(self):
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
