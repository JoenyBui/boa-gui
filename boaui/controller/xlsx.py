import wx
import wx.grid as grid

import pandas as pd

from . import TabPageController

from ..form.file import SaveXYDialog
from ..contextmenu.popup import PopupMenu
from ..component.table import GeneralRowTable, GeneralColumnTable
from ..config import STATE_NEW_PROJECT, STATE_CLOSE_PROJECT

__author__ = 'Joeny'


class XlsxController(TabPageController):
    """
    Spreadsheet Controller

    """
    def __init__(self, parent, view, table=None, data=None, row_label=None, col_label=None, *args, **kwargs):
        """

        :param parent: parent controller
        :param view: local view
        :return:
        """
        TabPageController.__init__(self, parent, view, *args, **kwargs)

        if table:
            self.table = table
        elif data:
            self.table = GeneralRowTable(data, row_labels=row_label, col_labels=col_label)
        else:
            self.table = None

        self.state = STATE_NEW_PROJECT

    def bind_methods(self):
        """
        Bind the handles at the end of initialization.

        :return:
        """
        self.view.Bind(grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_grid_right_click)

    def do_layout(self):
        """
        Draw layout data

        :return:
        """

        self.view.AutoSize()

    def update_layout(self, state):
        """
        Update layout

        :return:
        """
        if state == STATE_CLOSE_PROJECT:
            self.delete_control()
        else:
            self.sync_data()
            self.view.AutoSize()

    def refresh(self):
        """

        :return:
        """
        pass

    def sync_data(self):
        """
        Sync data table

        :return:
        """
        self.view.SetTable(self.table, True)

    def get_popup_menu(self):
        """
        Return the popup menu.

        :return:
        """
        popup = PopupMenu(self.view)

        popup.add_menu_item('Output CSV', self.on_output_csv)

        return popup

    def on_grid_right_click(self, event):
        """
        On grid right click.

        :param event:
        :return:
        """
        self.view.PopupMenu(self.get_popup_menu())

    def on_output_csv(self, event):
        """
        Output data to CSV.

        :param event:
        :return:
        """
        dlg = SaveXYDialog(self.view, message='Save to csv.', wildcard="Comma Separated Value (*.csv)|*.csv")

        if dlg.ShowModal() == wx.ID_OK:
            # Override the save file project
            file_path = dlg.GetPath()

            df = self.table.get_dataframe()
            df.to_csv(file_path)

            ret_val = wx.ID_OK
        else:
            ret_val = wx.ID_CANCEL

        dlg.Destroy()

        return ret_val
