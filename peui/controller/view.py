import os
import wx

from .. import config as cfg

__author__ = 'jbui'


class ViewController(object):
    """
    Isolate the view controlling methods to this class controller.
    """
    def __init__(self, parent):
        self.parent = parent
        self.windows = parent.windows
        self.show_pane = parent.show_pane
        self.show_page = parent.show_page

    def view_tree_window(self, event=None):
        if self.windows.get(cfg.METHOD_WINDOW_TREE):
            self.show_pane(self.windows.get(cfg.METHOD_WINDOW_TREE))

    def view_console_window(self, event=None):
        if self.windows.get(cfg.METHOD_WINDOW_CONSOLE):
            self.show_pane(self.windows.get(cfg.METHOD_WINDOW_CONSOLE))

    def view_property_grid_window(self, event=None):
        if self.windows.get(cfg.METHOD_WINDOW_PROP_GRID):
            self.show_pane(self.windows.get(cfg.METHOD_WINDOW_PROP_GRID))

    def view_toolbar_standard(self, event=None):
        if self.windows.get(cfg.METHOD_TOOLBAR_STANDARD):
            self.show_pane(self.windows.get(cfg.METHOD_TOOLBAR_STANDARD))

    def view_general_window(self, event=None):
        if self.windows.get(cfg.METHOD_WINDOW_GENERAL):
            self.show_page(self.windows.get(cfg.METHOD_WINDOW_GENERAL))

    def view_chart_window(self, event=None):
        if self.windows.get(cfg.METHOD_WINDOW_CHART):
            self.show_page(self.windows.get(cfg.METHOD_WINDOW_CHART))

    def view_xlsx_window(self, event=None):
        if self.windows.get(cfg.METHOD_WINDOW_XLSX):
            self.show_page(self.windows.get(cfg.METHOD_WINDOW_XLSX))
