import wx

__author__ = 'jbui'


class CustomMenuBar(wx.MenuBar):

    def __init__(self, parent, **kwargs):
        wx.MenuBar.__init__(self)

        f_menu = wx.Menu()
        e_menu = wx.Menu()
        v_menu = wx.Menu()
        t_menu = wx.Menu()
        w_menu = wx.Menu()

        # Append the menu items to the menus
        f_menu.Append(-1, "Simple   Ctrl+N", "Text")
        e_menu.Append(-1, "FlatMenu", "Text")
        v_menu.Append(-1, "Example", "Text")
        t_menu.Append(-1, "Hello", "Text")
        w_menu.Append(-1, "World", "Text")

        # Append menus to the menubar
        self.Append(f_menu, "&File")
        self.Append(e_menu, "&Edit")
        self.Append(v_menu, "&View")
        self.Append(t_menu, "&Options")
        self.Append(w_menu, "&Help")
