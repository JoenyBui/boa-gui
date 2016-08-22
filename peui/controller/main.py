import os
import uuid

import wx
import wx.lib.agw.aui as aui
from wx.lib.pubsub import pub

from pecutil.threads import threaded

from ..config import *

from ..main.menubar import CustomMenuBar
from ..main.ribbon import CustomRibbonBar

from .dlg import DlgController
from .view import ViewController

__author__ = 'jbui'


class MainController(object):
    """
    Main Controller

    Mixins are defined right to left.
    """
    def __init__(self, project, master_key, **kwargs):
        """

        :param project:
        :param master_key:
        :param kwargs:
        :return:
        """
        self.project = project

        # Add controller to project
        self.project.controller = self

        self.setting = kwargs.get('setting')

        self.frame = None
        self.windows = {}
        self.notebook = None

        # Save File Path
        self.file_path = None

        # File History
        self.filehistory = wx.FileHistory(8)
        self.config = wx.Config(kwargs.get("config", "peui"), style=wx.CONFIG_USE_LOCAL_FILE)
        self.filehistory.Load(self.config)

        # Extend Controllers
        self.dlg_ctrl = kwargs.get('dlg_ctrl', DlgController(self))
        self.view_ctrl = kwargs.get('view_ctrl', ViewController(self))

        self.childs = []        # Controller for specific views, dlgs, etc...

        self.master_key = master_key

        self.uuid = str(uuid.uuid4())

        self.subscribe_methods()

    @property
    def evt_new_project(self):
        """

        :return:
        """
        return 'EVT_NEW_PROJECT'

    @property
    def evt_open_project(self):
        """

        :return:
        """
        return 'EVT_OPEN_PROJECT'

    @property
    def evt_refresh_view(self):
        """

        :return:
        """
        return 'EVT_REFRESH_VIEW'

    @property
    def evt_clear_controls(self):
        return 'EVT_CLEAR_CONTROLS'

    def subscribe_methods(self):
        """

        :return:
        """
        pub.subscribe(self.new_project, self.evt_new_project)
        pub.subscribe(self.refresh_clear_controls, self.evt_clear_controls)
        pub.subscribe(self.refresh_view, self.evt_refresh_view)
        pub.subscribe(self.refresh_open_project, self.evt_open_project)

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
        self.master_key[METHOD_OUTPUT_PROJECT]['method'] = self.dlg_ctrl.output_project_word_doc
        self.master_key[METHOD_EXIT_PROJECT]['method'] = self.exit_project

        self.master_key[METHOD_UNDO]['method'] = self.evt_undo
        self.master_key[METHOD_REDO]['method'] = self.evt_redo
        self.master_key[METHOD_CUT]['method'] = self.evt_cut
        self.master_key[METHOD_COPY]['method'] = self.evt_copy
        self.master_key[METHOD_PASTE]['method'] = self.evt_paste

        self.master_key[METHOD_WINDOW_TREE]['method'] = self.view_ctrl.view_tree_window
        self.master_key[METHOD_WINDOW_CONSOLE]['method'] = self.view_ctrl.view_console_window
        self.master_key[METHOD_WINDOW_PROP_GRID]['method'] = self.view_ctrl.view_property_grid_window
        # self.master_key[METHOD_WINDOW_GENERAL]['method'] = self.view_ctrl.view_general_window
        # self.master_key[METHOD_WINDOW_CHART]['method'] = self.view_ctrl.view_chart_window
        # self.master_key[METHOD_WINDOW_XLSX]['method'] = self.view_ctrl.view_xlsx_window

        self.master_key[METHOD_TOOLBAR_STANDARD]['method'] = self.view_ctrl.view_toolbar_standard

        self.master_key[METHOD_DEFAULT_SETTING]['method'] = self.dlg_ctrl.setting_dialog
        self.master_key[METHOD_ABOUT]['method'] = self.dlg_ctrl.about_dialog

    def evt_undo(self, event=None):
        """
        Event Undo.
        :param event:
        :return:
        """
        print('Undo')

    def evt_redo(self, event=None):
        """
        Event Redo.
        :param event:
        :return:
        """
        print('Redo')

    def evt_cut(self, event=None):
        """

        :param event:
        :return:
        """
        print('Cut')

    def evt_copy(self, event=None):
        """

        :param event:
        :return:
        """
        print('Copy')

    def evt_paste(self, event=None):
        """

        :param event:
        :return:
        """
        print('Paste')

    def add_pane(self, panel, key, area=None, name=None):
        """
        Add Pane to the main view.

        :param panel:
        :param key:
        :param area:
        :param name:
        :return:
        """
        self.windows[key] = panel

        pane = self.frame.add_pane(panel, area, name)

        if panel.__dict__.get('controller'):
            self.childs.append(panel.controller)

        return pane

    def add_page(self, page, key, name, close=True):
        """
        Add page to the central view.

        :param page:
        :param key:
        :param name:
        :param close:
        :return:
        """
        self.windows[key] = page

        pane = self.notebook.AddPage(page, name)

        if not close:
            ctrl, idx = self.notebook.FindTab(page)

            self.notebook.SetCloseButton(idx, False)

        if page.__dict__.get('controller'):
            self.childs.append(page.controller)

        return pane

    def set_key(self, key):
        """
        Establish the menu bar items.

        :param key:
        :return:
        """
        if True:
            self.set_menu_bar(key)
        else:
            self.set_ribbon_bar(key)

    def set_menu_bar(self, key):
        """

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

        # Add History
        self.frame.Bind(wx.EVT_MENU_RANGE, self.on_file_history, id=wx.ID_FILE1, id2=wx.ID_FILE9)

    def on_file_history(self, event):
        """
        On File History click

        :param event:
        :return:
        """
        fileNum = event.GetId() - wx.ID_FILE1
        self.file_path = self.filehistory.GetHistoryFile(fileNum)

        # Move up the list
        self.filehistory.AddFileToHistory(self.file_path)

        # Do whatever you want with the file path...
        self.open_project(self.file_path)

        pub.sendMessage(self.evt_open_project)

    def set_ribbon_bar(self, key):
        """

        :param key:
        :return:
        """
        menu_bar = CustomRibbonBar(self.frame, self)

        self.frame.menu_bar = menu_bar
        self.add_pane(self.frame.menu_bar, 'ribbon', wx.TOP, 'RIBBON')

        # self.frame.SetMenuBar(self.frame.menu_bar)

    def new_project(self, project):
        """
        New Project is transferred.

        :param project:
        :return:
        """

        self.project = project
        self.project.controller = self

        self.refresh()

    def save_project(self, path):
        """
        Save Project to file path.

        :param path:
        :return:
        """
        self.project.save(path)

    def output_project(self, file_path):
        """
        Output PEC Document

        :param file_path:
        :return:
        """
        from ..docs import PecDocument

        doc = PecDocument(None)
        doc.context = dict(company_name='World Company')
        doc.save(file_path)

    def open_project(self, path):
        """
        Open project model

        :param path:
        :return:
        """
        self.project.load(path)

    def refresh_open_project(self):
        """
        Refresh open project

        :return:
        """
        self.refresh_clear_project()

    def refresh_clear_project(self):
        """
        Refresh clear project

        :return:
        """
        pass

    def refresh_clear_controls(self):
        """
        Clear controls and remove tab.

        :return:
        """
        for child in self.childs:
            if hasattr(child, 'clear_control'):
                child.clear_control()

        for index in range(0, self.notebook.GetPageCount()):
            # Loop and remove all the pages inside the viewer.
            self.notebook.DeletePage(0)

    def refresh(self):
        """
        Total refresh of all the components.

        :return:
        """
        self.refresh_model()
        self.refresh_view()

    def refresh_view(self):
        """
        Refresh specifically the view.

        :return:
        """
        for child in self.childs:
            child.refresh()

        if self.frame:
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

        self.frame.mgr.Update()

    def show_page(self, ctrl):
        """
        Show page

        :param ctrl:
        """
        ctrl, idx = self.notebook.FindTab(ctrl)
        page = self.notebook.GetPage(idx)
        #TODO: Page is now shown.
        page.Show(not page.IsShown())

        self.refresh_view()

    def exit_project(self, event):
        """
        Exit the application.

        :param event:
        """
        self.frame.Close(True)
        self.frame.Destroy()
        event.Skip()
