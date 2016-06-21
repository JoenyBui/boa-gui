import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class PathSmartBox(SmartTextBox):
    """
    Path Smart Box.

    """
    def __init__(self, parent, *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        """
        SmartTextBox.__init__(self, parent, *args, **kwargs)

        self.Bind(wx.EVT_KEY_DOWN, self.key_down)

    def key_down(self, event=None):
        pass


class PathInputLayout(SmartInputLayout):
    """
    Path Input Layout.

    """
    def __init__(self, parent, textbox=None, postbox=None, layout=None, *args, **kwargs):
        """

        :param parent:
        :param layout:
        :param args:
        :param kwargs:
        :return:
        """
        SmartInputLayout.__init__(self, parent, layout=layout, *args, **kwargs)

        # self.label = kwargs.get('label', 'Path:')

        if textbox:
            self.textbox = textbox
        else:
            self.textbox = PathSmartBox(parent)

        # self.textbox.SetSize(self.layout.get_size(self.INDEX_TEXTBOX))

        if postbox:
            self.postbox = postbox
        else:
            self.postbox = wx.Button(parent, id=wx.ID_ANY, size=(24, 24))

        # self.postbox.SetSize(self.layout.get_size(self.INDEX_POSTBOX))

        if self.postbox:
            self.postbox.Bind(wx.EVT_BUTTON, self.pick_folder_path)
            self.postbox.SetToolTip(wx.ToolTip("Choose Path"))

        self.do_layout()

    def pick_folder_path(self, event):
        """
        Pick the folder path.

        :param event:
        :return:
        """
        dlg = wx.DirDialog(self.parent)

        if dlg.ShowModal():
            self.textbox.SetValue(dlg.GetPath())

        dlg.Destroy()
