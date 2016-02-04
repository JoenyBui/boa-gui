import wx

__author__ = 'jbui'


class CustomMenuBar(wx.MenuBar):
    """
    Custom Menu Bar
    """

    def __init__(self, parent, controller, **kwargs):
        wx.MenuBar.__init__(self)
        self.controller = controller

        self.menus = {}

    def build_sub_menu(self, menu_item):
        sub_menu_object = wx.Menu()

        if menu_item.get('keys'):
            for item in menu_item['keys']:
                # Allow now to add separators
                if not item:
                    sub_menu_object.AppendSeparator()
                    continue

                title, sub_menu = self.build_sub_menu(item)

                self.menus[item['id']] = sub_menu_object.AppendMenu(item['id'], title, sub_menu)
        else:
            sub_menu_object = None

        return menu_item['name'], sub_menu_object

    def set_menu_item(self, menus):
        """

        :param menu_key:
        :return:
        """
        for menu in menus:
            name, menu_item = self.build_sub_menu(menu)

            self.Append(menu_item, name)
