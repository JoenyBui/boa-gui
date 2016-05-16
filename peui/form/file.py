import os

import wx

from ..model.project import Project
from ..textbox.textbox import TextSmartBox, TextInputLayout
from ..textbox.pathbox import PathSmartBox, PathInputLayout

__author__ = 'jbui'


class NewProjectDialog(wx.Dialog):
    """
    New Project Dialog
    """
    def __init__(self, parent, style=wx.OK, btn_flags=wx.OK | wx.CANCEL, panel=None, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', 'New Project'),
                           size=(kwargs.get('width', 500), kwargs.get('height', 300)))

        self.parent = parent

        # Attributes
        self.flags = style

        if panel:
            self.panel = panel
        else:
            self.panel = NewProjectPanel(self, parent.setting)

        # Layout
        btnsizer = self.CreateButtonSizer(btn_flags)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        sizer.Add(btnsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        self.SetInitialSize()

        # self.bind()

    def get_project(self):
        """
        Return the project object.
        """
        return Project(name=self.panel.tb_project.GetValue(),
                       author=self.panel.tb_author.GetValue(),
                       project_folder=self.panel.tb_path.GetValue())

    # def bind(self):
    #     self.Bind(wx.EVT_BUTTON, self.on_okay, self.panel.btn_okay)
    #     self.Bind(wx.EVT_BUTTON, self.on_cancel, self.panel.btn_cancel)
    #
    # def on_okay(self, event):
    #     self.Close()
    #
    # def on_cancel(self, event):
    #     self.Destroy()


class NewProjectPanel(wx.Panel):
    """

    """
    def __init__(self, parent, default_settings, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        # Attributes
        self.tb_project = TextSmartBox(self, value=default_settings.project_name)
        self.tb_author = TextSmartBox(self, value=default_settings.author)
        self.tb_path = PathSmartBox(self, value=default_settings.path)

        # self.btn_okay = wx.Button(self, wx.ID_ANY, 'OK')
        # self.btn_cancel = wx.Button(self, wx.ID_ANY, 'Cancel')

        self.do_layout()

    def do_layout(self):
        """
        Layout the controls
        """
        vsizer = wx.BoxSizer(wx.VERTICAL)

        field1_sz = TextInputLayout(self, name='Project Name:', textbox=self.tb_project)
        field2_sz = TextInputLayout(self, name='Author Name:', textbox=self.tb_author)
        field3_sz = PathInputLayout(self, name='Path', textbox=self.tb_path)

        # btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        # btnSizer.Add(self.btn_okay, 0, wx.ALL | wx.LEFT, 5)
        # btnSizer.Add(self.btn_cancel, 0, wx.ALL | wx.RIGHT, 5)

        # Now finish the layout by adding the two sizers to the main vertical sizer.
        vsizer.AddStretchSpacer()

        BOTH_SIDES = wx.EXPAND | wx.LEFT | wx.RIGHT

        vsizer.Add(field1_sz, 0, BOTH_SIDES | wx.TOP, 20)
        vsizer.AddSpacer(15)
        vsizer.Add(field2_sz, 0, BOTH_SIDES, 20)
        vsizer.AddSpacer(15)
        vsizer.Add(field3_sz, 0, BOTH_SIDES, 20)
        vsizer.AddSpacer(15)
        # vsizer.Add(btnSizer, 0, BOTH_SIDES | wx.BOTTOM, 20)
        # vsizer.AddStretchSpacer()

        # Finally assign the main outer sizer to the panel
        self.SetSizer(vsizer)


class OpenProjectDialog(wx.FileDialog):
    def __init__(self, parent, *args, **kwargs):
        wx.FileDialog.__init__(self, parent, "Open a file", os.getcwd(), "", "*.*", wx.OPEN, *args, **kwargs)

        self.parent = parent


class SaveProjectDialog(wx.FileDialog):
    def __init__(self, parent, *args, **kwargs):
        wx.FileDialog.__init__(self, parent, "Save project", os.getcwd(), "", "*.json", wx.SAVE | wx.OVERWRITE_PROMPT, *args, **kwargs)

        self.parent = parent


class SaveAsProjectDialog(wx.FileDialog):
    def __init__(self, parent, *args, **kwargs):
        wx.FileDialog.__init__(self, parent, "Save project as...", os.getcwd(), "", "*.json", wx.SAVE | wx.OVERWRITE_PROMPT, *args, **kwargs)

        self.parent = parent


class CloseProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent

