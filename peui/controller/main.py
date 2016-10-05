import os
import uuid

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
        self.basefolder = kwargs.get('basefolder')

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

        self.toolbars = []
        self.childs = []        # Controller for specific views, dlgs, etc...
        self.trash = []

        self.master_key = master_key

        self.uuid = str(uuid.uuid4())

        self.subscribe_methods()

    def update_project_state(self, state):
        """
        Update the project state.

        :param state:
        :return:
        """
        if state == STATE_OPEN_PROJECT:
            self.update_open_project()

        elif state == STATE_NEW_PROJECT:
            self.update_new_project()

        elif state == STATE_CLOSE_PROJECT:
            self.update_clear_project()

    def bind_all_methods(self):
        """
        Bind all event menus.

        :return:
        """
        self.bind_methods()
        self.bind_aui_methods()
        self.bind_menu_bars()

    def initialize_notebook(self, frame, size=(300, 400)):
        """
        Add notebook

        :param frame:
        :param size:
        :return:
        """
        self.notebook = aui.AuiNotebook(frame, agwStyle=aui.AUI_NB_CLOSE_ON_ALL_TABS, size=size)

        self.frame.add_pane(self.notebook, wx.CENTER, 'Notebook')

    # @property
    # def evt_new_project(self):
    #     return 'EVT_NEW_PROJECT'
    #
    # @property
    # def evt_open_project(self):
    #     return 'EVT_OPEN_PROJECT'

    @property
    def evt_refresh_view(self):
        return 'EVT_REFRESH_VIEW'

    @property
    def evt_clear_controls(self):
        return 'EVT_CLEAR_CONTROLS'

    @property
    def evt_pane_close(self):
        return 'EVT_PANE_CLOSE'

    @property
    def evt_page_close(self):
        return 'EVT_PAGE_CLOSE'

    @property
    def evt_page_closed(self):
        return 'EVT_PAGE_CLOSED'

    @property
    def evt_undo(self):
        return 'EVT_UNDO'

    @property
    def evt_redo(self):
        return 'EVT_REDO'

    @property
    def evt_cut(self):
        return 'EVT_CUT'

    @property
    def evt_copy(self):
        return 'EVT_COPY'

    @property
    def evt_paste(self):
        return 'EVT_PASTE'

    def subscribe_methods(self):
        """
        Subscribe methods

        :return:
        """

        pub.subscribe(self.update_project_state, EVT_CHANGE_PROJECT)
        pub.subscribe(self.update_status_bar, EVT_UPDATE_STATUS)
        pub.subscribe(self.update_frame_title, EVT_UPDATE_TITLE)

        # pub.subscribe(self.new_project, self.evt_new_project)

        # pub.subscribe(self.refresh_clear_controls, self.evt_clear_controls)
        pub.subscribe(self.refresh_view, self.evt_refresh_view)
        # pub.subscribe(self.refresh_open_project, self.evt_open_project)
        pub.subscribe(self.on_pane_close, self.evt_pane_close)
        pub.subscribe(self.on_page_close, self.evt_page_close)
        pub.subscribe(self.on_page_closed, self.evt_page_closed)

        pub.subscribe(self.empty_trash, EVT_EMPTY_TRASH)

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
        self.master_key[METHOD_CLOSE_PROJECT]['method'] = self.dlg_ctrl.close_project_dialog
        self.master_key[METHOD_EXIT_PROJECT]['method'] = self.exit_project

        self.master_key[METHOD_UNDO]['method'] = self.on_click_undo
        self.master_key[METHOD_REDO]['method'] = self.on_click_redo
        self.master_key[METHOD_CUT]['method'] = self.on_click_cut
        self.master_key[METHOD_COPY]['method'] = self.on_click_copy
        self.master_key[METHOD_PASTE]['method'] = self.on_click_paste

        self.master_key[METHOD_WINDOW_TREE]['method'] = self.view_ctrl.view_tree_window
        self.master_key[METHOD_WINDOW_CONSOLE]['method'] = self.view_ctrl.view_console_window
        self.master_key[METHOD_WINDOW_PROP_GRID]['method'] = self.view_ctrl.view_property_grid_window
        # self.master_key[METHOD_WINDOW_GENERAL]['method'] = self.view_ctrl.view_general_window
        # self.master_key[METHOD_WINDOW_CHART]['method'] = self.view_ctrl.view_chart_window
        self.master_key[METHOD_WINDOW_XLSX]['method'] = self.view_ctrl.view_switch_page

        self.master_key[METHOD_TOOLBAR_STANDARD]['method'] = self.view_ctrl.view_toolbar_standard

        self.master_key[METHOD_DEFAULT_SETTING]['method'] = self.dlg_ctrl.setting_dialog
        self.master_key[METHOD_ABOUT]['method'] = self.dlg_ctrl.about_dialog

    def bind_aui_methods(self):
        """
        Bind aui notebook.

        :return:
        """
        self.notebook.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.bind_page_close)
        self.notebook.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSED, self.bind_page_closed)
        self.frame.Bind(aui.EVT_AUI_PANE_CLOSE, self.bind_pane_close)

    def bind_menu_bars(self):
        """
        Bind menu bars

        :return:
        """
        for id, menu in self.frame.menu_bar.menus.items():
            if self.master_key.get(id):
                if self.master_key[id].get('method'):
                    if menu:
                        self.frame.Bind(wx.EVT_MENU, self.master_key[id]['method'], menu)

        # Add History
        self.frame.Bind(wx.EVT_MENU_RANGE, self.on_file_history, id=wx.ID_FILE1, id2=wx.ID_FILE9)

    def bind_page_close(self, event):
        """
        Page close event

        :param event:
        :return:
        """
        page = self.notebook.GetPage(event.Selection)

        if page:
            if hasattr(page, 'controller'):
                if page.controller.id:
                    pub.sendMessage(self.evt_page_close, id=page.controller.id)

    def bind_page_closed(self, event):
        """
        Page closed event

        :param event:
        :return:
        """
        pass
        page = self.notebook.GetPage(event.Selection)

        if page:
            if hasattr(page, 'controller'):
                if page.controller.id:
                    pub.sendMessage(self.evt_page_closed, id=page.controller.id)

    def bind_pane_close(self, event):
        """
        Pane close event.

        :param event:
        :return:
        """
        pane = event.GetPane()

        if pane:
            pub.sendMessage(self.evt_pane_close, name=pane.name)

    def bind_pane_open(self, event):
        """
        Bind open pane.

        :param event:
        :return:
        """
        name = event.GetPane().name

    def delete_pane(self, key):
        """
        Delete Pane given key

        :param key:
        """
        # Detach pane
        self.frame.mgr.DetachPane(self.windows[key])

        # Destroy
        self.windows[key].Destroy()

        # Update pane
        self.frame.mgr.Update()

    def delete_page(self, page_index):
        """
        Delete notebook page

        :param page_index:
        """
        self.notebook.DeletePage(page_index)

    def add_toolbar(self, toolbar, key, area):
        """
        Add toolbar to the manager frame.

        :param toolbar:
        :param key:
        :param area:
        """
        self.windows[key] = toolbar

        # Add panel to model.
        pane = self.frame.add_pane(toolbar, area, None)

        self.toolbars.append(toolbar.controller)

    def add_pane(self, panel, key, area=None, name=None):
        """
        Add Pane to the main view.

        :param panel:
        :param key: menu item key
        :param area:
        :param name:
        :return:
        """
        self.windows[key] = panel

        # Add panel to model.
        pane = self.frame.add_pane(panel, area, name)

        # If has controller, add to child array.
        if panel.__dict__.get('controller'):
            self.childs.append(panel.controller)
            panel.controller.key = key

        # If have menu item, then enable/check.
        menu_item = self.frame.menu_bar.menus.get(key)
        if menu_item:
            menu_item.Enable(True)
            menu_item.Check(True)

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
            page.controller.key = key

        # If have menu item, then enable/check.
        menu_item = self.frame.menu_bar.menus.get(key)
        if menu_item:
            menu_item.Enable(True)
            menu_item.Check(True)

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

        self.frame.menu_bar = menu_bar
        self.frame.SetMenuBar(self.frame.menu_bar)

    def on_pane_close(self, name=None):
        """
        On pane close, un-check the menu item

        :param name:
        :return:
        """
        menu = self.frame.menu_bar.menus.get(name)
        if menu:
            menu.Check(False)

    def on_page_close(self, id=None):
        """

        :param id:
        :return:
        """
        menu = self.frame.menu_bar.menus.get(id)
        if menu:
            menu.Check(False)

        del self.windows[id]

    def on_page_closed(self, id=None):
        """

        :param id:
        :return:
        """
        menu = self.frame.menu_bar.menus.get(id)
        if menu:
            menu.Check(False)

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

        # Close existing project first
        pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_CLOSE_PROJECT)
        pub.sendMessage(EVT_EMPTY_TRASH)

        # Do whatever you want with the file path...
        self.open_project(self.file_path)

        # Open Project
        pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_OPEN_PROJECT)

    def set_ribbon_bar(self, key):
        """
        Set Ribbon Bar

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

    def update_new_project(self):
        """
        Update new project.

        :return:
        """
        pub.sendMessage(EVT_UPDATE_TITLE, text='*New Project*')
        pub.sendMessage(EVT_UPDATE_STATUS, text='')

    def update_open_project(self):
        """
        Update open project views

        :return:
        """
        pub.sendMessage(EVT_UPDATE_TITLE, text=self.file_path)

    def update_clear_project(self):
        """
        Refresh clear project

        :return:
        """
        pub.sendMessage(EVT_CHANGE_STATE, state=STATE_CLOSE_PROJECT)

        self.childs = []

    def update_frame_title(self, text):
        """
        Refresh the main title with the project.

        :return:
        """
        self.frame.SetTitle(text)

    def update_status_bar(self, text):
        """
        Refresh the status bar.

        :param text:
        """
        if self.frame:
            if self.frame.status_bar:
                self.frame.status_bar.SetStatusText(text, 0)

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

    def on_click_undo(self, event):
        pass

    def on_click_redo(self, event):
        pass

    def on_click_cut(self, event):
        pass

    def on_click_copy(self, event):
        pass

    def on_click_paste(self, event):
        pass

    def empty_trash(self):
        """
        Empty trash of the controls.

        :return:
        """
        for item in self.trash:
            if item in self.childs:
                self.childs.remove(item)

        self.trash = []
