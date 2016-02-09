import os
import wx

from ..form.file import NewProjectDialog, OpenProjectDialog, SaveProjectDialog, SaveAsProjectDialog, CloseProjectDialog
from ..form.about import AboutDialog

__author__ = 'jbui'


class DlgController(object):
    """
    Mixins for main controller.
    """
    def __init__(self, parent):
        self.parent = parent
        self.frame = parent.frame

    def new_project_dialog(self, event):
        dlg = NewProjectDialog(self, width=4000, height=3000)

        if dlg.ShowModal():
            pass

        dlg.Destroy()

    def open_project_dialog(self, event):
        dlg = OpenProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            mypath = os.path.basename(path)

        dlg.Destroy()

    def save_project_dialog(self, event):
        #TODO: Check if there if the file already exists.
        dlg = SaveProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

    def save_as_project_dialog(self, event):
        dlg = SaveAsProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

    def about_dialog(self, event):
        abt = AboutDialog(name='Generic Gui')
        abt.show()
