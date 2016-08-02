import wx, os

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
        """

        :param event:
        """
        pass


class PathInputLayout(SmartInputLayout):
    """
    Path Input Layout.

    """
    def __init__(self, parent, textbox=None, postbox=None, max=None, min=None, layout=None, is_file=False, *args, **kwargs):
        """

        :param parent:
        :param textbox:
        :param postbox:
        :param layout:
        :param args:
        :param kwargs:
        :return:
        """
        SmartInputLayout.__init__(self, parent, max=max, min=min, layout=layout, *args, **kwargs)

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
            if is_file:
                self.postbox.Bind(wx.EVT_BUTTON, self.pick_file_path)
                self.postbox.SetToolTip(wx.ToolTip("Choose File"))
            else:
                self.postbox.Bind(wx.EVT_BUTTON, self.pick_folder_path)
                self.postbox.SetToolTip(wx.ToolTip("Choose Path"))

        self.do_layout()

    def pick_folder_path(self, event):
        """
        Pick the folder path using a Directory Dialog.

        :param event:
        :return:
        """
        path = self.textbox.Value

        if os.path.isdir(path):
            dlg = wx.DirDialog(self.parent, defaultPath=path)
        else:
            dlg = wx.DirDialog(self.parent)

        if dlg.ShowModal() == wx.ID_OK:
            # Change the path string..
            self.textbox.SetValue(dlg.GetPath())

        dlg.Destroy()

    def pick_file_path(self, event):
        """

        :param event:
        :return:
        """
        path = self.textbox.Value

        if os.path.isfile(path):
            dlg = wx.FileDialog(self.parent, defaultFile=path)
        else:
            dlg = wx.FileDialog(self.parent)

        if dlg.ShowModal() == wx.ID_OK:
            # Change the path string..
            self.textbox.SetValue(dlg.GetPath())

        dlg.Destroy()

    def enable(self):
        """
        Enable textbox and/or postbox.

        :return:
        """
        if self.textbox:
            self.textbox.Enable(True)

        if self.postbox:
            self.postbox.Enable(True)

    def disable(self):
        """
        Disable textbox and/or postbox.

        :return:
        """
        if self.textbox:
            self.textbox.Disable()

        if self.postbox:
            self.postbox.Disable()

    def set_value(self, value):
        self.postbox.Value = value

    def get_value(self):
        return self.postbox.Value
git