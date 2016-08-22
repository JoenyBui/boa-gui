import wx

from wx.lib import sheet

from ..controller.xlsx import XlsxController

__author__ = 'jbui'


class SpreadSheet(sheet.CSheet):
    """

    """
    def __init__(self, parent, controller, *args, **kwargs):
        """

        :param parent:
        :param controller:
        :param args:
        :param kwargs:
        :return:
        """
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetNumberRows(55)
        self.SetNumberCols(25)

        for i in range(55):
            self.SetRowSize(i, 20)

        self.controller = XlsxController(controller, self)

    def OnGridSelectCell(self, event):
        pass
        # self.row, self.col = event.GetRow(), event.GetCol()
        # control = self.GetParent().GetParent().position
        # value = self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        # control.SetValue(value)
        # event.Skip()
