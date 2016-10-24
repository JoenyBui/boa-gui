import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class TextSmartBox(SmartTextBox):
    """
    Text Smart Box.
    """
    def __init__(self, parent, key_up=None, message=None, *args, **kwargs):
        """

        :param parent:
        :param key_up:
        :param message:
        :param args:
        :param kwargs:
        """
        SmartTextBox.__init__(self, parent, key_up=key_up, message=message, *args, **kwargs)



class TextInputLayout(SmartInputLayout):
    """
    Text Input Layout

    """
    def __init__(self, parent, textbox=None, value=None, layout=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param textbox:
        :param value:
        :param layout:
        :param args:
        :param kwargs:
        :return:
        """
        SmartInputLayout.__init__(self, parent, layout=layout, *args, **kwargs)

        if textbox:
            self.textbox = textbox
        else:
            self.textbox = TextSmartBox(parent)

        # self.textbox.SetSize(self.layout.get_size(self.INDEX_TEXTBOX))

        if value:
            self.textbox.Value = str(value)

        self.do_layout()

    def set_value(self, value):
        """
        Set the value

        :param value:
        :return:
        """
        self.textbox.set_value(value)

    def get_value(self):
        """
        Get the value

        :return:
        """
        return self.textbox.get_value()
