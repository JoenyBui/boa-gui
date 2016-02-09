import os

from ..config import *

from ..main.menubar import CustomMenuBar

from .dlg import DlgController
from .view import ViewController

__author__ = 'jbui'


class MainController(object):
    """
    Main Controller

    Mixins are defined right to left.
    """
    def __init__(self, project, master_key, **kwargs):
        self.project = project

        # Add controller to project
        self.project.controller = self

        self.setting = kwargs.get('setting')

        self.frame = None
        self.windows = {}

        # Extend Controllers
        self.dlg_ctrl = DlgController(self)
        self.view_ctrl = ViewController(self)

        self.master_key = master_key

        self.bind_methods()

    def bind_methods(self):
        """
        Connect the keys to the function for binding at the menu bar, context menu, shortcut, etc...

        THIS METHOD MUST BE OVERRIDDEN BY CHILD CLASS.
        :return:
        """
        self.master_key[METHOD_NEW_PROJECT]['method'] = self.dlg_ctrl.new_project_dialog
        self.master_key[METHOD_OPEN_PROJECT]['method'] = self.dlg_ctrl.open_project_dialog
        self.master_key[METHOD_SAVE_PROJECT]['method'] = self.dlg_ctrl.save_project_dialog
        self.master_key[METHOD_SAVE_AS_PROJECT]['method'] = self.dlg_ctrl.save_as_project_dialog
        self.master_key[METHOD_EXIT_PROJECT]['method'] = self.exit_project
        self.master_key[METHOD_ABOUT]['method'] = self.dlg_ctrl.about_dialog
        self.master_key[METHOD_WINDOW_TREE]['method'] = self.view_ctrl.view_tree_window
        self.master_key[METHOD_WINDOW_CONSOLE]['method'] = self.view_ctrl.view_console_window
        self.master_key[METHOD_WINDOW_PROP_GRID]['method'] = self.view_ctrl.view_property_grid_window
        
    def set_key(self, key):
        """
        Establish the menu bar items.
        :param key:
        :return:
        """
        menu_bar = CustomMenuBar(self.frame, self)
        menu_bar.set_menu_item(key)

        for id, menu in menu_bar.menus.items():
            if self.master_key.get(id):
                if self.master_key[id].get('method'):
                    if menu:
                        self.frame.Bind(wx.EVT_MENU, self.master_key[id]['method'], menu)

        self.frame.menu_bar = menu_bar
        self.frame.SetMenuBar(self.frame.menu_bar)

    def refresh(self):
        self.refresh_model()
        self.refresh_view()

    def refresh_view(self):
        """
        Refresh specifically the view.
        :return:
        """
        self.frame.refresh()

    def refresh_model(self):
        """
        Refresh the model -> view.
        :return:
        """
        pass

    def show_pane(self, ctrl):
        """
        Switch pane view.
        :param ctrl:
        :return:
        """
        pane = self.frame.mgr.GetPane(ctrl)

        pane.Show(not pane.IsShown())

        self.refresh_view()

    def exit_project(self, event):
        self.frame.Close(True)
        self.frame.Destroy()
        event.Skip()
