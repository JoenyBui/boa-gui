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

            # Add menu to item array.
            # self.menus[menu['id']] = menu_item

        # f_menu = wx.Menu()
        # e_menu = wx.Menu()
        # v_menu = wx.Menu()
        # t_menu = wx.Menu()
        # w_menu = wx.Menu()
        #
        # # Append the menu items to the menus
        # f_menu.Append(-1, "Simple   Ctrl+N", "Text")
        # e_menu.Append(-1, "FlatMenu", "Text")
        # v_menu.Append(-1, "Example", "Text")
        # t_menu.Append(-1, "Hello", "Text")
        # w_menu.Append(-1, "World", "Text")
        #
        # # Append menus to the menubar
        # self.Append(f_menu, "&File")
        # self.Append(e_menu, "&Edit")
        # self.Append(v_menu, "&View")
        # self.Append(t_menu, "&Options")
        # self.Append(w_menu, "&Help")
        #
        # menu_bar = wx.MenuBar()
        #
        # # File Menu
        # menu_file = wx.Menu()
        #
        # self.Bind(wx.EVT_MENU, self.OnClickNewProject, menu_file.Append(wx.ID_NEW, "&New Project"))
        # self.Bind(wx.EVT_MENU, self.OnClickOpenProject, menu_file.Append(wx.ID_OPEN, "&Open Project"))
        # self.Bind(wx.EVT_MENU, self.OnClickSaveProject, menu_file.Append(wx.ID_SAVE, "&Save Project"))
        # self.Bind(wx.EVT_MENU, self.OnClickCloseProject, menu_file.Append(wx.ID_CLOSE, "&Close Project"))
        # menu_file.AppendSeparator()
        #
        # self.Bind(wx.EVT_MENU, self.OnClickProjectFolder, menu_file.Append(self.ID_OPEN_PROJECT_FOLDER, "&Open Data Path"))
        # self.Bind(wx.EVT_MENU, self.OnClickImportMiscData, menu_file.Append(wx.NewId(), "&Import Misc. Data"))
        # menu_file.AppendSeparator()
        # self.Bind(wx.EVT_MENU, self.OnExit, menu_file.Append(wx.ID_EXIT, "E&xit", 'Exit Application'))
        # menu_bar.Append(menu_file, '&File')
        #
        # # Edit Menu
        # menu_edit = wx.Menu()
        #
        # self.Bind(wx.EVT_MENU, self.OnClickAddConversion,
        #           menu_edit.Append(self.ID_ADD_CONVERSION, '&Add Conversion'))
        # self.Bind(wx.EVT_MENU, self.OnClickModifyConversion,
        #           menu_edit.Append(self.ID_MODIFY_CONVERSION, '&Modify Conversion'))
        #
        # menu_bar.Append(menu_edit, '&Edit')
        #
        # # Run Menu
        # menu_run = wx.Menu()
        #
        # self.Bind(wx.EVT_MENU, self.OnRunMovie2d, menu_run.Append(wx.NewId(), "Movie 2d"))
        # self.Bind(wx.EVT_MENU, self.OnRunMovie3d, menu_run.Append(wx.NewId(), "Movie 3d"))
        # self.Bind(wx.EVT_MENU, self.OnRunMovieFilter, menu_run.Append(wx.NewId(), "Movie Filter"))
        # self.Bind(wx.EVT_MENU, self.OnRunMovieFull, menu_run.Append(wx.NewId(), "Movie Full"))
        # self.Bind(wx.EVT_MENU, self.OnRunMovieSection, menu_run.Append(wx.NewId(), "Movie Section"))
        # menu_run.AppendSeparator()
        # self.Bind(wx.EVT_MENU, self.OnRunChartSection, menu_run.Append(wx.NewId(), "&Chart Section"))
        #
        # menu_bar.Append(menu_run, '&Run')
        #
        # # Help Menu
        # menu_help = wx.Menu()
        # self.Bind(wx.EVT_MENU, self.OnAboutBox, menu_help.Append(wx.ID_ABOUT, "&About", "About Application"))
        #
        # menu_bar.Append(menu_help, '&Help')
