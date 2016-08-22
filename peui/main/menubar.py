import wx

__author__ = 'jbui'

MB_ICON_SIZE = wx.Size(14, 14)


class CustomMenuBar(wx.MenuBar):
    """
    Custom Menu Bar

    """
    def __init__(self, parent, controller, **kwargs):
        """

        :param parent:
        :param controller:
        :param kwargs:
        :return:
        """
        wx.MenuBar.__init__(self)
        self.controller = controller

        self.menus = {}

    def build_sub_menu(self, menu_item):
        """
        Build Sub Menu Items.

        :param menu_item:
        :return:
        """
        sub_menu_object = wx.Menu()

        if menu_item.get('keys'):
            for item in menu_item['keys']:
                # Allow now to add separators
                if not item:
                    sub_menu_object.AppendSeparator()
                    continue

                if item.get('history'):
                    recent = wx.Menu()
                    self.controller.filehistory.UseMenu(recent)
                    self.controller.filehistory.AddFilesToMenu()

                    sub_menu_object.AppendMenu(item['id'], item['name'], recent)
                    continue

                title, sub_menu = self.build_sub_menu(item)

                if item.get('kind'):
                    mi = wx.MenuItem(sub_menu_object, item['id'], title, kind=item.get('kind'))
                else:
                    mi = wx.MenuItem(sub_menu_object, item['id'], title)

                if item.get('bitmap'):
                    mi.SetBitmap(wx.ArtProvider.GetBitmap(item['bitmap'], wx.ART_MENU, MB_ICON_SIZE))

                # if item.get('icon'):
                #     mi.SetBitmap(wx.Icon(item['icon'], wx.BITMAP_TYPE_ICO))

                mi.SetSubMenu(sub_menu)

                self.menus[item['id']] = mi

                sub_menu_object.AppendItem(self.menus[item['id']])

                # Add Check Status if ITEM Check.
                if item.get('kind') == wx.ITEM_CHECK:
                    if item.get('checked'):
                        mi.Check(True)
        else:
            sub_menu_object = None

        return menu_item['name'], sub_menu_object

    def set_menu_item(self, menus):
        """
        Set Menu Item.

        :param menus:
        :return:
        """
        for menu in menus:
            name, menu_item = self.build_sub_menu(menu)

            self.Append(menu_item, name)
