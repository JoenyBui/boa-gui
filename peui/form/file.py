import os

import wx

from ..textbox.textbox import TextSmartBox

__author__ = 'jbui'


class NewProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent

        # Attributes
        self.panel = NewProjectPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()


class NewProjectPanel(wx.Panel):
    """

    """
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        # Attributes
        self._field1 = TextSmartBox(self)
        self._field2 = TextSmartBox(self)

        self._do_layout()

    def _do_layout(self):
        """Layout the controls"""
        vsizer = wx.BoxSizer(wx.VERTICAL)
        field1_sz = wx.BoxSizer(wx.HORIZONTAL)
        field2_sz = wx.BoxSizer(wx.HORIZONTAL)

        # Make the labels
        field1_lbl = wx.StaticText(self, label="Field 1:")
        field2_lbl = wx.StaticText(self, label="Field 2:")

        # Make the first row by adding the label and field
        # to the first horizontal sizer
        field1_sz.AddSpacer(50)
        field1_sz.Add(field1_lbl)
        field1_sz.AddSpacer(5) # put 5px of space between
        field1_sz.Add(self._field1)
        field1_sz.AddSpacer(50)

        # Do the same for the second row
        field2_sz.AddSpacer(50)
        field2_sz.Add(field2_lbl)
        field2_sz.AddSpacer(5)
        field2_sz.Add(self._field2)
        field2_sz.AddSpacer(50)

        # Now finish the layout by adding the two sizers
        # to the main vertical sizer.
        vsizer.AddSpacer(50)
        vsizer.Add(field1_sz)
        vsizer.AddSpacer(15)
        vsizer.Add(field2_sz)
        vsizer.AddSpacer(50)

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

