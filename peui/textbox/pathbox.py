import wx, os

from ..textbox import LayoutDimensions
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

    def is_file_exists(self):
        """
        Is file exists.

        :return:
        """
        filepath = self.get_value()

        if filepath:
            if os.path.exists(filepath):
                return os.path.isfile(filepath)

        return False

    def is_dir_exists(self):
        """
        Is path exists.

        :return:
        """
        path = self.get_value()

        if path:
            if os.path.exists(path):
                return os.path.isdir(path)

        return False


class PathInputLayout(SmartInputLayout):
    """
    Path Input Layout.

    """
    def __init__(self,
                 parent,
                 textbox=None,
                 postbox=None,
                 layout=None,
                 is_file=False,
                 is_save=False,
                 message=wx.FileSelectorPromptStr,
                 defaultDir=wx.EmptyString,
                 defaultFile=wx.EmptyString,
                 wildcard=wx.FileSelectorDefaultWildcardStr,
                 style=wx.FD_DEFAULT_STYLE,
                 *args,
                 **kwargs):
        """
        Constructor

        :param parent:
        :param textbox:
        :param postbox:
        :param layout:
        :param is_file:
        :param is_save:
        :param message:
        :param defaultDir:
        :param defaultFile:
        :param wildcard:
        :param style:
        :param args:
        :param kwargs:
        :return:
        """
        SmartInputLayout.__init__(self, parent, layout=layout, *args, **kwargs)

        if textbox:
            self.textbox = textbox
        else:
            self.textbox = PathSmartBox(parent)

        if postbox:
            self.postbox = postbox
        else:
            self.postbox = wx.Button(parent, id=wx.ID_ANY, size=(24, 24))

        if self.postbox:
            if is_file:
                self.postbox.Bind(wx.EVT_BUTTON, self.pick_file_path)
                self.postbox.SetToolTip(wx.ToolTip("Choose File"))
            else:
                self.postbox.Bind(wx.EVT_BUTTON, self.pick_folder_path)
                self.postbox.SetToolTip(wx.ToolTip("Choose Path"))

        self.is_file = is_file
        self.is_save = is_save

        self.message = message
        self.defaultDir = defaultDir
        self.defaultFile = defaultFile
        self.wildcard = wildcard

        self.style = style
        if is_save and is_file:
            self.style = wx.SAVE | wx.OVERWRITE_PROMPT

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

            ret_val = wx.ID_OK
        else:
            ret_val = wx.ID_CANCEL

        dlg.Destroy()

        return ret_val

    def pick_file_path(self, event):
        """
        Pick file path

        :param event:
        :return:
        """
        path = self.textbox.Value

        if os.path.isfile(path):
            dlg = wx.FileDialog(self.parent,
                                message=self.message,
                                defaultDir=self.defaultDir,
                                defaultFile=path,
                                wildcard=self.wildcard,
                                style=self.style)
        else:
            dlg = wx.FileDialog(self.parent,
                                message=self.message,
                                defaultDir=self.defaultDir,
                                defaultFile=self.defaultFile,
                                wildcard=self.wildcard,
                                style=self.style)

        if dlg.ShowModal() == wx.ID_OK:
            # Change the path string..
            self.textbox.SetValue(dlg.GetPath())

            ret_val = wx.ID_OK
        else:
            ret_val = wx.ID_CANCEL

        dlg.Destroy()

        return ret_val

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
        """
        Set the file path

        """
        self.textbox.set_value(value)

    def get_value(self):
        """
        Return the file path

        """
        return self.textbox.get_value()

    def is_valid_path(self):
        """
        Is valid path

        :return:
        """
        if self.is_file:
            return self.textbox.is_file_exists()
        else:
            return self.textbox.is_dir_exists()


class SmartPathInputLayout(PathInputLayout):
    """
    Smart Path Input Layout

    """
    def __init__(self, parent, name=None, textbox=None, postbox=None, layout=None, *args, **kwargs):
        """
        Constructor

        :param parent:
        :param name:
        :param textbox:
        :param postbox:
        :param layout:
        :param is_file:
        :param args:
        :param kwargs:
        :return:
        """
        if textbox is None:
            textbox = PathSmartBox(parent, disabled_messages=[name])
            textbox.Disable()

        if postbox is None:
            postbox = wx.Button(parent, label='Browse', id=wx.ID_ANY)

        if layout is None:
            layout = LayoutDimensions(left=2, right=2, top=2, bottom=2, interior=2,
                                      widths=(125, 75),
                                      stretch_factor=(1, 0))
            layout.calculate()

        PathInputLayout.__init__(self,
                                 parent,
                                 label=None,
                                 textbox=textbox,
                                 postbox=postbox,
                                 layout=layout,
                                 *args,
                                 **kwargs)

        self.path = None

    def pick_file_path(self, event):
        """
        Pick file path

        :param event:
        :return:
        """
        retval = PathInputLayout.pick_file_path(self, event)

        if retval == wx.ID_CANCEL:
            self.textbox.set_disable_message()

            self.path = None
        else:
            self.path = self.textbox.get_value()

        return retval

    def pick_folder_path(self, event):
        """
        Pick folder path

        :param event:
        :return:
        """
        retval = PathInputLayout.pick_folder_path(self, event)

        if retval == wx.ID_CANCEL:
            self.textbox.set_disable_message()

            self.path = None
        else:
            self.path = self.textbox.get_value()

        return retval

    def enable(self):
        """
        Enable textbox and/or postbox.

        :return:
        """
        if self.postbox:
            self.postbox.Enable(True)

    def disable(self):
        """
        Disable textbox and/or postbox.

        :return:
        """
        if self.postbox:
            self.postbox.Disable()

    def get_value(self):
        """
        Get the value

        :return:
        """
        return self.path
