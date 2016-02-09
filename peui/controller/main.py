import os

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

        self.setting = kwargs.get('setting')

        self.frame = None
        self.windows = {}

        self.master_key = master_key

        self.bind_methods()

    def show_pane(self, ctrl):
        """
        Switch pane.
        :param ctrl:
        :return:
        """
        pane = self.frame.mgr.GetPane(ctrl)

        pane.Show(not pane.IsShown())

        self.refresh_view()

    def bind_methods(self):
        """
        Connect the keys to the function for binding at the menu bar, context menu, shortcut, etc...

        THIS METHOD MUST BE OVERRIDEN BY CHILD CLASS.
        :return:
        """
        self.master_key[METHOD_NEW_PROJECT]['method'] = self.new_project
        self.master_key[METHOD_OPEN_PROJECT]['method'] = self.open_project
        self.master_key[METHOD_SAVE_PROJECT]['method'] = self.save_project
        self.master_key[METHOD_SAVE_AS_PROJECT]['method'] = self.save_as_project
        self.master_key[METHOD_EXIT_PROJECT]['method'] = self.exit_project
        self.master_key[METHOD_ABOUT]['method'] = self.about
        self.master_key[METHOD_WINDOW_TREE]['method'] = self.view_tree
        self.master_key[METHOD_WINDOW_CONSOLE]['method'] = self.view_console

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

    def new_project(self, event):
        dlg = NewProjectDialog(self, width=4000, height=3000)

        if dlg.ShowModal():
            pass

        dlg.Destroy()

    def open_project(self, event):
        dlg = OpenProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            mypath = os.path.basename(path)

        dlg.Destroy()

    def save_project(self, event):
        #TODO: Check if there if the file already exists.
        dlg = SaveProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

    def save_as_project(self, event):
        dlg = SaveAsProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

    def exit_project(self, event):
        self.frame.Close(True)
        self.frame.Destroy()
        event.Skip()

    def about(self, event):
        abt = AboutDialog(name='Generic Gui')
        abt.show()

    def view_tree(self, event):
        if self.windows.get('tree'):
            self.show_pane(self.windows.get('tree'))

    def view_console(self, event):
        if self.windows.get('console'):
            self.show_pane(self.windows.get('console'))
