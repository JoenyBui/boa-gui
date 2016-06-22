import wx

__author__ = 'jbui'


class PopupMenuMixin(object):

    def __init__(self):
        super(PopupMenuMixin, self).__init__()

        # Attributes.
        self._menu = None
        self._data = {}

        # Event Handlers
        self.Bind(wx.EVT_CONTEXT_MENU, self.on_context_menu)

    def on_context_menu(self, event):
        """
        Creates and shows the Menu.
        :param event:
        :return:
        """
        if self._menu is not None:
            self._menu.Destroy()

        self._menu = wx.Menu()
        self._data = {}

        self.create_context_menu()

        # Set the popup menu.
        self.PopupMenu(self._menu)

    def create_context_menu(self):
        """
        Create context menu.

        :return:
        """
        raise NotImplementedError

    def add_menu_item(self, label, handler, object=None):
        """
        Add the menu item.

        :param label:
        :param handler:
        :param object:
        """
        # Create new menu item.
        item = wx.MenuItem(self._menu, wx.ID_ANY, label)

        # Bind menu item.
        self.Bind(wx.EVT_MENU, handler, item)

        # Add menu item.
        self._menu.AppendItem(item)

        # Add in data.
        self._data[item.GetId()] = object
