from ..config import *

from ..main.menubar import CustomMenuBar
from ..form.file import NewProjectDialog, OpenProjectDialog, SaveProjectDialog, SaveAsProjectDialog, CloseProjectDialog
from ..form.about import AboutDialog

__author__ = 'jbui'


class MainController(object):
    """
    Main Controller
    """

    def __init__(self, project, master_key, **kwargs):
        self.project = project

        # Add controller to project
        self.project.controller = self

        self.frame = None

        self.master_key = master_key

        self.bind_methods()

    def bind_methods(self):
        """
        Connect the keys to the function for binding at the menu bar, context menu, shortcut, etc...
        :return:
        """
        self.master_key[METHOD_NEW_PROJECT]['method'] = self.new_project
        self.master_key[METHOD_OPEN_PROJECT]['method'] = self.open_project
        self.master_key[METHOD_SAVE_PROJECT]['method'] = self.save_project
        self.master_key[METHOD_SAVE_AS_PROJECT]['method'] = self.save_as_project
        self.master_key[METHOD_EXIT_PROJECT]['method'] = self.exit_project
        self.master_key[METHOD_ABOUT]['method'] = self.about

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

    def new_project(self, event):
        dlg = NewProjectDialog(self)
        res = dlg.ShowModal()

    def open_project(self, event):
        dlg = OpenProjectDialog(self)
        res = dlg.ShowModal()

    def save_project(self, event):
        dlg = SaveProjectDialog(self)
        res = dlg.ShowModal()

    def save_as_project(self, event):
        dlg = SaveAsProjectDialog(self)
        res = dlg.ShowModal()

    def exit_project(self, event):
        self.frame.Close(True)
        self.frame.Destroy()
        event.Skip()

    def about(self, event):
        abt = AboutDialog(name='Generic Gui')
        abt.show()

