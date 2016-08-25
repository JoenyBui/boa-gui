import wx

from wx.lib import sheet

from ..controller.xlsx import XlsxController

__author__ = 'jbui'


class SpreadSheet(sheet.CSheet):
    """
    Spreadsheet view

        * Clear(self)
            Clear the currently selected cells
        * Copy(self)
            Copy the currently selected cells to the clipboard
        * OnCellChange(self, event)
        * OnColSize(self, event)
        * OnGridSelectCell(self, event)
            Track cell selections
        * OnLeftClick(self, event)
            Override left-click behavior to prevent left-click edit initiation
        * OnLeftDoubleClick(self, event)
            Initiate the cell editor on a double-click
        * OnRangeSelect(self, event)
            Track which cells are selected so that copy/paste behavior can be implemented
        * OnRightClick(self, event)
            Move grid cursor when a cell is right-clicked
        * OnRowSize(self, event)
        * Paste(self)
            Paste the contents of the clipboard into the currently selected cells
        * SetNumberCols(self, numCols)
            Set the number of columns in the sheet
        * SetNumberRows(self, numRows)
            Set the number of rows in the sheet
    """
    def __init__(self, parent, controller, local=None, *args, **kwargs):
        """
        Constructor

        :param parent: parent view
        :param controller: parent controller
        :param local: local controller
        :param args:
        :param kwargs:
        :return:
        """
        if local:
            self.controller = local
            self.controller.view = self
        else:
            self.controller = XlsxController(controller, self)

        sheet.CSheet.__init__(self, parent)

        self.SetLabelBackgroundColour('#DBD4D4')
        self.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        if hasattr(self.controller, 'do_layout'):
            self.controller.do_layout()

    def OnGridSelectCell(self, event):
        pass
        # self.row, self.col = event.GetRow(), event.GetCol()
        # control = self.GetParent().GetParent().position
        # value = self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        # control.SetValue(value)
        # event.Skip()

