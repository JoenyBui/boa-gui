import wx

__author__ = 'jbui'


class PopupMenuMixin(object):

    def __init__(self):
        super(PopupMenuMixin, self).__init__()

        # Attributes.
        self._menu = None

        # Event Handlers
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

    def OnContextMenu(self, event):
        """
        Creates and shows the Menu.
        :param event:
        :return:
        """
        if self._menu is not None:
            self._menu.Destroy()

        self._menu = wx.Menu()
        self.CreateContextMenu(self._menu)
        self.PopupMenu(self._menu)

    def CreateContextMenu(self, menu):
        raise NotImplementedError

