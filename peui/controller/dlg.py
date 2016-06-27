import os

import wx
from wx.lib.pubsub import pub

from ..model.project import Project
from ..form.file import NewProjectDialog, OpenProjectDialog, SaveProjectDialog, SaveAsProjectDialog, CloseProjectDialog
from ..form.about import AboutDialog

__author__ = 'jbui'


class DlgController(object):
    """
    Mixins for main controller.
    """
    def __init__(self, parent):
        """

        :param parent:
        :return:
        """
        self.parent = parent

    @property
    def frame(self):
        """

        :return:
        """
        return self.parent.frame

    @frame.setter
    def frame(self, value):
        """

        :param value:
        :return:
        """
        self.parent.frame = value

    def sync_data(self):
        """

        :return:
        """
        pass

    def new_project_dialog(self, event):
        """
        New Project Dialog.

        :param event:
        :return:
        """
        dlg = NewProjectDialog(self.frame, self.parent.setting)

        if dlg.ShowModal():
            self.parent.new_project(dlg.get_project())

            # Broadcast new project dialog.
            pub.sendMessage(self.parent.evt_new_project)

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

            # Add to file history.
            self.parent.filehistory.AddFileToHistory(path)
            self.parent.filehistory.Save(self.parent.config)
            self.parent.config.Flush()

            self.parent.open_project(path)

            pub.sendMessage(self.parent.evt_open_project)


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

            self.parent.save_project(path)

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

            self.parent.save_project(path)

        dlg.Destroy()

    def about_dialog(self, event):
        """
        About Model Dialog.

        :param event:
        :return:
        """
        abt = AboutDialog(name='Generic Gui')
        abt.show()
