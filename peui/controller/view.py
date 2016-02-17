import os
import wx

__author__ = 'jbui'


class ViewController(object):
    """
    Isolate the view controlling methods to this class controller.
    """
    def __init__(self, parent):
        self.parent = parent
        self.windows = parent.windows
        self.show_pane = parent.show_pane

    def view_tree_window(self, event=None):
        if self.windows.get('tree'):
            self.show_pane(self.windows.get('tree'))

    def view_console_window(self, event=None):
        if self.windows.get('console'):
            self.show_pane(self.windows.get('console'))

    def view_property_grid_window(self, event=None):
        if self.windows.get('prop grid'):
            self.show_pane(self.windows.get('prop grid'))

    def view_toolbar_standard(self, event=None):
        pass
