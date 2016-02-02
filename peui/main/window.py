import wx
import wx.aui

from menubar import CustomMenuBar
from statusbar import CustomStatusBar
from ..panel.general import GeneralPanel

__author__ = 'jbui'


class MainWindow(wx.Frame):
    """
    Main Window
    """
    def __init__(self, parent=None, title='', width=800, height=600, **kwargs):
        wx.Frame.__init__(self, parent, title=title, size=(width, height))

        self._parent = parent
        self._mgr = wx.aui.AuiManager(self)

        # create several text controls
        text1 = wx.TextCtrl(self, -1, 'Pane 1 - sample text',
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)

        text2 = wx.TextCtrl(self, -1, 'Pane 2 - sample text',
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)

        # text3 = wx.TextCtrl(self, -1, 'Main content window',
        #                     wx.DefaultPosition, wx.Size(200,150),
        #                     wx.NO_BORDER | wx.TE_MULTILINE)

        self._tree = wx.TreeCtrl(self, -1)

        # add the panes to the manager
        self._mgr.AddPane(text1, wx.LEFT, 'Pane Number One')
        self._mgr.AddPane(text2, wx.BOTTOM, 'Pane Number Two')
        # self._mgr.AddPane(text3, wx.CENTER)
        self._mgr.AddPane(self._tree, wx.RIGHT, 'COME ON')

        # Notebook
        self._mgr.AddPane(GeneralPanel(self), wx.CENTER)
        # self._notebook = wx.aui.AuiNotebook(self)
        # self._panelOne = GeneralPanel(self._notebook)
        # self._panelTwo = GeneralPanel(self._notebook)
        #
        # self._mgr.AddPane(self._notebook, wx.CENTER)
                          # wx.aui.AuiPaneInfo().Name("notebook_content").CenterPane().PaneBorder(False))
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self._notebook.Refresh()
        # self._notebook.Update()

        # self._mgr.AddPane(self)
        # tell the manager to 'commit' all the changes just made
        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # self._notebook.Set

        # # self.CreateStatusBar()
        #
        filemenu = wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program.")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)


        # Status Bar
        self.status_bar = CustomStatusBar(self)
        self.SetStatusBar(self.status_bar)

        # Show Window
        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def OnClose(self, event):
        # De-initialize the frame manager
        self._mgr.UnInit()
        # delete the frame
        self.Destroy()
