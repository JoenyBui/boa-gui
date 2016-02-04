import wx

__author__ = 'jbui'


class NewProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent


class OpenProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent


class SaveProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent


class SaveAsProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent


class CloseProjectDialog(wx.Dialog):
    def __init__(self, parent, **kwargs):
        wx.Dialog.__init__(self, None, title=kwargs.get('title', ''))

        self.parent = parent

