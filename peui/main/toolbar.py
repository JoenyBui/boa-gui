import wx
from wx.lib.agw import aui
from wx.lib.agw.aui import auibar
from wx.lib.pubsub import pub

from ..controller import ChildController
from ..config import EVT_UPDATE_TITLE, EVT_UPDATE_STATUS


__author__ = 'jbui'


class CustomToolBar(auibar.AuiToolBar):
    """
    Custom Toolbar
    """
    def __init__(self, parent, controller, menu_items, local=None, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, agwStyle=aui.AUI_TB_DEFAULT_STYLE):
        """
        Constructor

        :param parent:
        :param controller:
        :param menu_items:
        :param local:
        :param id:
        :param pos:
        :param size:
        :param style:
        :param agwStyle:
        :return:
        """
        auibar.AuiToolBar.__init__(self, parent, id=id, pos=pos, size=size, style=style, agwStyle=agwStyle)

        bitmap_size = wx.Size(16, 16)
        self.SetToolBitmapSize(bitmap_size)

        if local:
            self.controller = local
        else:
            self.controller = CustomToolBarController(controller, self, menu_items)

        self.parent = parent
        self.SetGripperVisible(True)


class CustomToolBarController(ChildController):
    """
    Custom Toolbar Controller.

    """
    def __init__(self, parent, view, menu_items):
        """

        :param parent:
        :param view:
        :param menu_items:
        :return:
        """
        ChildController.__init__(self, parent, view)

        self.buttons = {}
        self.menu_items = menu_items
        self.bitmap_size = wx.Size(16, 16)

        self.do_layout()

        self.view.Bind(wx.EVT_SET_CURSOR, self.evt_on_hover)

    def evt_on_hover(self, event):
        self.view.StopPreviewTimer()

        action_item = self.view.FindToolForPosition(event.GetX(), event.GetY())

        if action_item:
            pub.sendMessage(EVT_UPDATE_STATUS, text=action_item.short_help)

        event.Skip()

    def do_layout(self):
        """

        :return:
        """
        for menu in self.menu_items:
            if menu['id'] == wx.ID_SEPARATOR:
                self.view.AddSeparator()

            elif menu.get('icon'):
                icon = wx.Bitmap(menu['icon'])
                # icon.SetSize(self.bitmap_size)

                self.view.AddSimpleTool(menu['id'], menu['label'], icon, menu['label'])

            else:
                tb = wx.ArtProvider.GetBitmap(menu['bitmap'], wx.ART_TOOLBAR, self.bitmap_size)

                self.buttons[menu['id']] = self.view.AddSimpleTool(menu['id'], menu['label'], tb, menu['label'])

    def update_layout(self, state):
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

    def clear_control(self):
        """

        :return:
        """
        pass

    def delete_control(self):
        pass
