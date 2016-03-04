import wx
from wx.lib.agw import aui
from wx.lib.agw.aui import auibar

from ..controller import ChildController


__author__ = 'jbui'


class CustomToolBar(auibar.AuiToolBar):
    """
    Custom Toolbar
    """
    def __init__(self, parent, controller, menu_items, local=None, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0, agwStyle=aui.AUI_TB_DEFAULT_STYLE):
        auibar.AuiToolBar.__init__(self, parent, id=id, pos=pos, size=size, style=style, agwStyle=agwStyle)

        bitmap_size = wx.Size(16, 16)
        self.SetToolBitmapSize(bitmap_size)
        #
        # tb4_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_TOOLBAR, bitmap_size)
        # tb4_bmp2 = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, bitmap_size)
        #
        # self.AddSimpleTool(wx.ID_NEW, "New Project", tb4_bmp1)
        # self.AddSimpleTool(-1, "Item 2", tb4_bmp2)
        # self.AddRadioTool(wx.ID_EDIT, 'Yikes', tb4_bmp1, tb4_bmp2)
        # self.AddSeparator()
        # self.AddSimpleTool(-1, "Item 3", wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_TOOLBAR, bitmap_size))
        #
        # self.SetToolDisabledBitmap(wx.ID_NEW, tb4_bmp1)
        # self.SetToolTipString("Hello")

        # self.AddLabel(-1, 'Help ME', 16)
        # self.SetAuiManager()

        if local:
            self.controller = local
        else:
            self.controller = CustomToolBarController(controller, self, menu_items)

        self.parent = parent
        self.SetGripperVisible(True)


class CustomToolBarController(ChildController):
    def __init__(self, parent, view, menu_items):
        ChildController.__init__(self, parent, view)

        self.menu_items = menu_items
        self.bitmap_size = wx.Size(16, 16)

        self.do_layout()

    def do_layout(self):
        for menu in self.menu_items:
            if menu['id'] == wx.ID_SEPARATOR:
                self.view.AddSeparator()
            else:
                tb = wx.ArtProvider.GetBitmap(menu['bitmap'], wx.ART_TOOLBAR, self.bitmap_size)

                self.view.AddSimpleTool(menu['id'], menu['label'], tb)

    def update_layout(self):
        pass

    def refresh(self):
        pass

    def sync_data(self):
        pass
