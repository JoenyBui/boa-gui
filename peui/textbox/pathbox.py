import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class PathSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)

        self.Bind(wx.EVT_KEY_DOWN, self.key_down)

    def key_down(self, event=None):
        pass


class PathInputLayout(SmartInputLayout):

    def __init__(self, parent, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        # self.label = kwargs.get('label', 'Path:')

        if kwargs.get('textbox'):
            self.textbox = kwargs.get('textbox')
        else:
            self.textbox = PathSmartBox(parent)

        if kwargs.get('postbox'):
            self.postbox = kwargs.get('postbox')
        else:
            self.postbox = wx.Button(parent, id=wx.ID_ANY, size=(24, 24))

        self.do_layout()

        if self.postbox:
            self.postbox.Bind(wx.EVT_BUTTON, self.pick_folder_path)
            self.postbox.SetToolTip(wx.ToolTip("Choose Path"))

    def pick_folder_path(self, event):
        dlg = wx.DirDialog(self.parent)

        if dlg.ShowModal():
            self.textbox.SetValue(dlg.GetPath())

        dlg.Destroy()
