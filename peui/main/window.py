import wx
# import wx.aui
import wx.lib.agw.aui as aui


from statusbar import CustomStatusBar
from ..panel.general import GeneralPanel

__author__ = 'jbui'


class MainWindow(wx.Frame):
    """
    Main Window
    """
    def __init__(self, parent, controller, title='', width=800, height=600, style=wx.DEFAULT_FRAME_STYLE, **kwargs):
        """
        Main Window.

        :param parent: parent wx.Frame
        :param controller: local controller
        :param title:
        :param width:
        :param height:
        :param style:
        :param kwargs:
        :return:
        """
        wx.Frame.__init__(self, parent, title=title, size=(width, height), style=style)

        self.parent = parent

        self.controller = controller
        self.controller.frame = self

        self.mgr = aui.AuiManager(self)

        # notify AUI which frame to use
        self.mgr.SetManagedWindow(self)
        self.mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.menu_bar = None

        # Status Bar
        self.status_bar = CustomStatusBar(self)
        self.SetStatusBar(self.status_bar)

        self.controller.bind_methods()

    def add_pane(self, panel, arg1=None, arg2=None, target=None):
        """
        Add the pane panel.

        :param panel:
        :param arg1: AuiPaneInfo or an integer value (direction) wx.LEFT, wx.RIGHT, wx.BOTTOM, wx.TOP, wx.CENTER
        :param arg2: AuiPaneInfo or a Point drop position
        :param target: AuiPaneInfo to be turned into a notebook
        :return:
        """
        pane = self.mgr.AddPane(panel, arg1=arg1, arg2=arg2, target=target)
        self.mgr.Update()
        return pane

    def refresh(self):
        """
        Refresh manager.

        :return:
        """
        self.mgr.Update()

    def on_exit(self, event):
        """
        Exit Window.

        :param event:
        :return:
        """
        self.Close(True)

    def on_close(self, event):
        """
        Close Window.

        :param event:
        :return:
        """
        # De-initialize the frame manager
        self.mgr.UnInit()

        # delete the frame
        self.Destroy()
        event.Skip()
