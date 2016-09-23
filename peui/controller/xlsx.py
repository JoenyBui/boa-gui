import logging

import wx
import wx.grid

from . import ChildController

__author__ = 'jbui'


class GeneralColumnTable(wx.grid.PyGridTableBase):
    """
    General PyGridTable Column First

    """
    def __init__(self, data=None, row_labels=None, col_labels=None):
        """

        :param data:
        :param row_labels:
        :param col_labels:
        """

        wx.grid.PyGridTableBase.__init__(self)

        self.data = data
        self.row_labels = row_labels
        self.col_labels = col_labels

    def GetNumberRows(self):
        return len(self.data[0])

    def GetNumberCols(self):
        return len(self.data)

    def GetColLabelValue(self, col):
        if self.col_labels:
            return self.col_labels[col]

        return wx.grid.PyGridTableBase.GetColLabelValue(self, col)

    def GetRowLabelValue(self, row):
        if self.row_labels:
            return self.row_labels[row]

        return wx.grid.PyGridTableBase.GetRowLabelValue(self, row)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        try:
            return self.data[col][row]
        except IndexError as e:
            return ''

    def SetValue(self, row, col, value):
        try:
            self.data[col][row] = value
        except Exception as e:
            logging.error('GeneralColumnTable->SetValue error')
            logging.error(str(e))


class GeneralRowTable(wx.grid.PyGridTableBase):
    """
    General PyGridTable Row First

    """
    def __init__(self, data=None, row_labels=None, col_labels=None):
        """

        :param data:
        :param row_labels:
        :param col_labels:
        """

        wx.grid.PyGridTableBase.__init__(self)

        self.data = data
        self.row_labels = row_labels
        self.col_labels = col_labels

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetColLabelValue(self, col):
        if self.col_labels:
            return self.col_labels[col]

        return wx.grid.PyGridTableBase.GetColLabelValue(self, col)

    def GetRowLabelValue(self, row):
        if self.row_labels:
            return self.row_labels[row]

        return wx.grid.PyGridTableBase.GetRowLabelValue(self, row)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        try:
            return self.data[row][col]
        except IndexError as e:
            return ''

    def SetValue(self, row, col, value):
        self.data[row][col] = value


class XlsxController(ChildController):
    """
    Spreadsheet Controller

    """
    def __init__(self, parent, view, data=None, row_label=None, col_label=None, *args, **kwargs):
        """

        :param parent: parent controller
        :param view: local view
        :return:
        """
        ChildController.__init__(self, parent, view, *args, **kwargs)

        self.table = kwargs.get('table', GeneralRowTable())
        self.data = data
        self.row_label = row_label
        self.col_label = col_label

    def do_layout(self):
        """
        Draw layout data

        :return:
        """
        # self.table.data = self.data
        # self.table.row_labels = self.row_label
        # self.table.col_labels = self.col_label
        #
        # self.view.SetTable(self.table)
        #
        pass

    def update_layout(self, state):
        """

        :return:
        """
        self.sync_data()

    def refresh(self):
        """

        :return:
        """
        pass

    def sync_data(self):
        """

        :return:
        """
        self.table.data = self.data
        self.table.row_labels = self.row_label
        self.table.col_labels = self.col_label

        self.view.SetTable(self.table, True)
