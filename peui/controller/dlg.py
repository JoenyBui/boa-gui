import os
import wx

from ..model.project import Project
from ..form.file import NewProjectDialog, OpenProjectDialog, SaveProjectDialog, SaveAsProjectDialog, CloseProjectDialog
from ..form.about import AboutDialog

__author__ = 'jbui'


class DlgController(object):
    """
    Mixins for main controller.
    """
    def __init__(self, parent):
        self.parent = parent

    @property
    def frame(self):
        return self.parent.frame

    @frame.setter
    def frame(self, value):
        self.parent.frame = value

    def sync_data(self):
        pass

    def new_project_dialog(self, event):
        """
        New Project Dialog.
        :param event:
        :return:
        """
        dlg = NewProjectDialog(self.parent, width=4000, height=3000)

        if dlg.ShowModal():
            self.parent.new_project(dlg.get_project())

        dlg.Destroy()

    def open_project_dialog(self, event):
        """
        Open Project Dialog.
        :param event:
        :return:
        """
        dlg = OpenProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            mypath = os.path.basename(path)

        dlg.Destroy()

    def save_project_dialog(self, event):
        """
        Save Project Dialog.
        :param event:
        :return:
        """
        #TODO: Check if there if the file already exists.
        dlg = SaveProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

    def save_as_project_dialog(self, event):
        """
        Save As Project Dialog.
        :param event:
        :return:
        """
        dlg = SaveAsProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        dlg.Destroy()

    def about_dialog(self, event):
        """
        About Model Dialog.
        :param event:
        :return:
        """
        abt = AboutDialog(name='Generic Gui')
        abt.show()
