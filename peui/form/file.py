import os

import wx

from ..model.project import Project
from ..textbox import LayoutDimensions
from ..textbox.textbox import TextSmartBox, TextInputLayout
from ..textbox.pathbox import PathSmartBox, PathInputLayout, SmartPathInputLayout

from . import DpiAwareness

__author__ = 'jbui'


class NewProjectDialog(wx.Dialog, DpiAwareness):
    """
    New Project Dialog

    """
    def __init__(self, parent, default_settings, style=wx.OK, btn_flags=wx.OK | wx.CANCEL, **kwargs):
        """

        :param parent: main frame form
        :param default_settings: default setting file used to initialize cell
        :param style:
        :param btn_flags:
        :param kwargs:
        :return:
        """
        DpiAwareness.__init__(self)

        width = self.scale(kwargs.get('width', 500))
        height = self.scale(kwargs.get('height', 300))

        wx.Dialog.__init__(self, parent,
                           title=kwargs.get('title', 'New Project'),
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
                           size=(self.scale(width), self.scale(height)))

        self.parent = parent

        # Attributes
        self.flags = style

        self.btnsizer = self.CreateButtonSizer(btn_flags)

        # Attributes
        self.tb_project = TextSmartBox(self, value=default_settings.project_name)
        self.tb_author = TextSmartBox(self, value=default_settings.author)
        self.tb_path = PathSmartBox(self, value=default_settings.path)

        # Layout

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.do_layout(), 0, wx.EXPAND | wx.ALL, 5)
        vsizer.AddStretchSpacer()
        vsizer.Add(self.btnsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(vsizer)
        self.SetInitialSize()
        self.CenterOnParent()
        self.Fit()

    def get_project(self):
        """
        Return the project object.

        :return: Project Object
        """
        project = Project(name=self.tb_project.GetValue(),
                          author=self.tb_author.GetValue(),
                          project_folder=self.tb_path.GetValue())

        return project

    def do_layout(self):
        """
        Layout the controls

        :return: vertical sizer
        """
        BOTH_SIDES = wx.EXPAND | wx.LEFT | wx.RIGHT

        layout = LayoutDimensions(left=2, right=2, top=2, bottom=2, interior=2,
                                  widths=(125, 175, 25),
                                  stretch_factor=(0, 1, 0))
        layout.calculate()

        vsizer = wx.BoxSizer(wx.VERTICAL)

        field1_sz = TextInputLayout(self, name='Project Name:', textbox=self.tb_project, layout=layout)
        field2_sz = TextInputLayout(self, name='Author Name:', textbox=self.tb_author, layout=layout)
        field3_sz = PathInputLayout(self, name='Path', textbox=self.tb_path, layout=layout)
        field4_sz = SmartPathInputLayout(self, name='Smart Part')

        # Now finish the layout by adding the two sizers to the main vertical sizer.
        # vsizer.AddStretchSpacer()

        vsizer.AddSpacer(self.scale(10))
        vsizer.Add(field1_sz, 0, BOTH_SIDES, self.scale(20))
        vsizer.AddSpacer(self.scale(10))
        vsizer.Add(field2_sz, 0, BOTH_SIDES, self.scale(20))
        vsizer.AddSpacer(self.scale(10))
        vsizer.Add(field3_sz, 0, BOTH_SIDES, self.scale(20))
        vsizer.AddSpacer(self.scale(10))
        vsizer.Add(field4_sz, 0, BOTH_SIDES, self.scale(20))
        vsizer.AddSpacer(self.scale(10))

        return vsizer


class OpenProjectDialog(wx.FileDialog):
    """

    """
    def __init__(self, parent, *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        :return:
        """
        wx.FileDialog.__init__(self, parent, "Open a file", os.getcwd(), "", "*.*", wx.OPEN, *args, **kwargs)

        self.parent = parent


class SaveProjectDialog(wx.FileDialog):
    """

    """
    def __init__(self, parent, *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        :return:
        """
        wx.FileDialog.__init__(self, parent, "Save project", os.getcwd(), "", "*.json", wx.SAVE | wx.OVERWRITE_PROMPT, *args, **kwargs)

        self.parent = parent


class SaveAsProjectDialog(wx.FileDialog):
    """

    """
    def __init__(self, parent, title='Save project as...', ext='*.json', *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        :return:
        """
        wx.FileDialog.__init__(self, parent,
                               title,
                               os.getcwd(),
                               "",
                               ext,
                               wx.SAVE | wx.OVERWRITE_PROMPT,
                               *args,
                               **kwargs)

        self.parent = parent


class CloseProjectDialog(wx.Dialog):
    """

    """
    def __init__(self, parent, **kwargs):
        """

        :param parent:
        :param kwargs:
        :return:
        """
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent


class SaveXYDialog(wx.FileDialog):
    """
    Save XY data and dplot chart

    """
    def __init__(self, parent, *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        :return:
        """
        if kwargs.get('wildcard'):
            wildcard = kwargs.get('wildcard')
            kwargs.pop('wildcard')
        else:
            wildcard = "DPlot (*.grf)|*.grf| Comma Separated Value (*.csv)|*.csv"

        if kwargs.get('message'):
            message = kwargs.get('message')
            kwargs.pop('message')
        else:
            message = "Save data as..."

        wx.FileDialog.__init__(self,
                               parent,
                               message=message,
                               defaultDir=os.getcwd(),
                               defaultFile="",
                               wildcard=wildcard,
                               style=wx.SAVE | wx.OVERWRITE_PROMPT,
                               *args,
                               **kwargs)

        self.parent = parent
