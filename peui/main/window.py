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
    def __init__(self, parent, controller, title='', width=800, height=600, **kwargs):
        wx.Frame.__init__(self, parent, title=title, size=(width, height))

        self.parent = parent

        self.controller = controller
        self.controller.frame = self

        self._mgr = aui.AuiManager(self)

        # notify AUI which frame to use
        self._mgr.SetManagedWindow(self)
        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.menu_bar = None

        # Status Bar
        self.status_bar = CustomStatusBar(self)
        self.SetStatusBar(self.status_bar)

    def add_pane(self, panel, area, name):
        """
        Add the pane panel.
        :param panel:
        :param area: wx.LEFT, wx.RIGHT, wx.BOTTOM, wx.TOP, wx.CENTER
        :param name:
        :return:
        """
        self._mgr.AddPane(panel, area, name)
        self._mgr.Update()

    def on_about(self, event):
        """

        :param event:
        :return:
        """
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def on_exit(self, event):
        """

        :param event:
        :return:
        """
        self.Close(True)

    def on_close(self, event):
        """

        :param event:
        :return:
        """
        # De-initialize the frame manager
        self._mgr.UnInit()

        # delete the frame
        self.Destroy()
        event.Skip()
