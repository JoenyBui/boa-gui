import os

import wx
from wx.lib.pubsub import pub

from pecutil.file import open_file

from ..model.project import Project
from ..form.file import NewProjectDialog, OpenProjectDialog, SaveProjectDialog, SaveAsProjectDialog, CloseProjectDialog
from ..form.about import AboutDialog
from ..form.setting import BaseSettingDialog
from ..config import EVT_CHANGE_PROJECT, STATE_OPEN_PROJECT, STATE_CLOSE_PROJECT, STATE_NEW_PROJECT, STATE_SAVE_PROJECT, STATE_OUTPUT_DOC, EVT_EMPTY_TRASH

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

    def new_project_dialog(self, event=None):
        """
        New Project Dialog.

        :param event:
        :return:
        """
        if self.parent.project:
            pass

        dlg = NewProjectDialog(self.frame, self.parent.setting)

        if dlg.ShowModal():
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_CLOSE_PROJECT)
            pub.sendMessage(EVT_EMPTY_TRASH)

            self.parent.new_project(dlg.get_project())

            # Reset file path
            self.parent.file_path = None

            # Broadcast new project dialog.
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_NEW_PROJECT)

        dlg.Destroy()

    def open_project_dialog(self, event=None):
        """
        Open Project Dialog.

        :param event:
        :return:
        """
        dlg = OpenProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_CLOSE_PROJECT)
            pub.sendMessage(EVT_EMPTY_TRASH)

            # Save the default file path
            self.parent.file_path = dlg.GetPath()

            # Add to file history.
            self.parent.filehistory.AddFileToHistory(self.parent.file_path)
            self.parent.filehistory.Save(self.parent.config)
            self.parent.config.Flush()

            self.parent.open_project(self.parent.file_path)

            # Send Open Project
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_OPEN_PROJECT)

        dlg.Destroy()

    def save_project_dialog(self, event=None):
        """
        Save Project Dialog.

        :param event:
        :return:
        """
        if self.parent.file_path:
            self.parent.save_project(self.parent.file_path)

            # Save Project
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_SAVE_PROJECT)
        else:
            self.save_as_project_dialog(event=event)

    def save_as_project_dialog(self, event=None):
        """
        Save As Project Dialog.

        :param event:
        :return:
        """
        dlg = SaveAsProjectDialog(self.frame)

        if dlg.ShowModal() == wx.ID_OK:
            # Override the save file project
            self.parent.file_path = dlg.GetPath()

            # Override the save file
            self.parent.save_project(self.parent.file_path)

            # Save Project As
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_SAVE_PROJECT)

        dlg.Destroy()

    def output_project_word_doc(self, event=None):
        """
        Output Project as Microsoft Word Document

        :param event:
        :return:
        """
        dlg = SaveAsProjectDialog(self.frame, title='Output to Word Docx', ext='*.docx')

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

            self.parent.output_project(path)

            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_OUTPUT_DOC)

            try:
                open_file(path)
            except Exception as e:
                print(e)

        dlg.Destroy()

    def setting_dialog(self, event=None):
        """
        Show Setting Dialog.

        :param event: NA
        :return:
        """
        dlg = BaseSettingDialog(self.frame, self.parent, size=(500, 350))
        # dlg.SetSize((500, 350))

        if dlg.ShowModal() == wx.ID_OK:
            # Save to file.
            self.parent.setting.save_to_settings()

        dlg.Destroy()

    def about_dialog(self, event=None):
        """
        About Model Dialog.

        :param event:
        :return:
        """
        abt = AboutDialog(name='Generic Gui')
        abt.show()

    def close_project_dialog(self, event=None):
        """
        Close project dialog

        :param event:
        :return:
        """

        if self.parent.project:

            dlg = wx.MessageDialog(None,
                                   'Do you want to close the project?',
                                   'Close %s Project' % self.parent.project.name,
                                   wx.YES_NO)

            if dlg.ShowModal() == wx.ID_YES:
                self.parent.project = None

                # Close Project
                pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_CLOSE_PROJECT)

        else:
            pub.sendMessage(EVT_CHANGE_PROJECT, state=STATE_CLOSE_PROJECT)

        pub.sendMessage(EVT_EMPTY_TRASH)
