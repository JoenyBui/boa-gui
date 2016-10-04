import os

import wx
import wx.aui

from wx.lib.pubsub import pub

from . import BaseController
from .. import config as cfg

__author__ = 'jbui'


class ViewController(BaseController):
    """
    Isolate the view controlling methods to this class controller.

    AuiNotebook Event
        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSED, <FUNCTION>, <OBJECT>)

        EVT_AUINOTEBOOK_PAGE_CLOSE
        EVT_AUINOTEBOOK_PAGE_CLOSED
        EVT_AUINOTEBOOK_PAGE_CHANGED
        EVT_AUINOTEBOOK_PAGE_CHANGING
        EVT_AUINOTEBOOK_BUTTON
        EVT_AUINOTEBOOK_BEGIN_DRAG
        EVT_AUINOTEBOOK_END_DRAG
        EVT_AUINOTEBOOK_DRAG_MOTION
        EVT_AUINOTEBOOK_ALLOW_DND
        EVT_AUINOTEBOOK_DRAG_DONE
        EVT_AUINOTEBOOK_BG_DCLICK
        EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN
        EVT_AUINOTEBOOK_TAB_MIDDLE_UP
        EVT_AUINOTEBOOK_TAB_RIGHT_DOWN
        EVT_AUINOTEBOOK_TAB_RIGHT_UP

    AuiPane Events

        EVT_AUI_PANE_BUTTON
        EVT_AUI_PANE_CLOSE
        EVT_AUI_PANE_MAXIMIZE
        EVT_AUI_PANE_RESTORE
        EVT_AUI_PANE_ACTIVATED
        EVT_AUI_RENDER
        EVT_AUI_FIND_MANAGER

    """
    def __init__(self, parent):
        """

        :param parent:
        :return:
        """
        BaseController.__init__(self)

        self.parent = parent
        self.windows = parent.windows
        self.show_pane = parent.show_pane
        self.show_page = parent.show_page

    def sync_data(self):
        """

        :return:
        """
        pass

    def view_switch_pane(self, event):
        """
        Switch on/off pane

        :param event:
        """
        id = event.Id

        if self.windows.get(id):
            self.show_pane(self.windows[id])

    def view_switch_page(self, event):
        """

        :param event:
        :return:
        """
        id = event.Id

        if self.windows.get(id):
            self.show_page(self.windows.get(id))

    def view_tree_window(self, event=None):
        """
        Trigger the tree window.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_WINDOW_TREE):
            self.show_pane(self.windows.get(cfg.METHOD_WINDOW_TREE))

    def view_console_window(self, event=None):
        """
        Trigger the console window.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_WINDOW_CONSOLE):
            self.show_pane(self.windows.get(cfg.METHOD_WINDOW_CONSOLE))

    def view_property_grid_window(self, event=None):
        """
        Trigger the property grid window.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_WINDOW_PROP_GRID):
            self.show_pane(self.windows.get(cfg.METHOD_WINDOW_PROP_GRID))

    def view_toolbar_standard(self, event=None):
        """
        Trigger the standard toolbar view.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_TOOLBAR_STANDARD):
            self.show_pane(self.windows.get(cfg.METHOD_TOOLBAR_STANDARD))

    def view_general_window(self, event=None):
        """
        Trigger the general window.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_WINDOW_GENERAL):
            self.show_page(self.windows.get(cfg.METHOD_WINDOW_GENERAL))

    def view_chart_window(self, event=None):
        """
        Trigger the chart window.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_WINDOW_CHART):
            self.show_page(self.windows.get(cfg.METHOD_WINDOW_CHART))

    def view_xlsx_window(self, event=None):
        """
        Trigger the xlsx window.

        :param event:
        :return:
        """
        if self.windows.get(cfg.METHOD_WINDOW_XLSX):
            self.show_page(self.windows.get(cfg.METHOD_WINDOW_XLSX))
