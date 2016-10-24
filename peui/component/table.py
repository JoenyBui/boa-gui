import wx
import wx.grid

import logging

import pandas as pd

__author__ = 'jbui'


class GeneralColumnTable(wx.grid.PyGridTableBase):
    """
    General PyGridTable Column First

    1st Column
    2nd Row

    """
    def __init__(self, data, row_labels=None, col_labels=None):
        """

        :param data:
        :param row_labels:
        :param col_labels:
        """

        wx.grid.PyGridTableBase.__init__(self)

        self.data = data

        if row_labels:
            self.row_labels = row_labels
        else:
            rows = []

            for index, row in enumerate(data[0]):
                rows.append(str(index+1))

            self.row_labels = rows

        if col_labels:
            self.col_labels = col_labels
        else:
            cols = []

            for index, column in enumerate(data):
                cols.append(str(index + 1))

            self.col_labels = cols

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

    def get_dataframe(self):
        return pd.DataFrame(
            self.data, columns=self.row_labels, index=self.col_labels
        ).transpose()


class GeneralRowTable(wx.grid.PyGridTableBase):
    """
    General PyGridTable Row First

    """
    def __init__(self, data, row_labels=None, col_labels=None):
        """

        :param data:
        :param row_labels:
        :param col_labels:
        """

        wx.grid.PyGridTableBase.__init__(self)

        self.data = data


        if row_labels:
            self.row_labels = row_labels
        else:
            rows = []

            for index, row in enumerate(data):
                rows.append(str(index+1))

            self.row_labels = rows

        if col_labels:
            self.col_labels = col_labels
        else:
            cols = []

            for index, column in enumerate(data[0]):
                cols.append(str(index + 1))

            self.col_labels = cols

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

    def get_dataframe(self):
        return pd.DataFrame(
            self.data, columns=self.row_labels, index=self.col_labels
        )
