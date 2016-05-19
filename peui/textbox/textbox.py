import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class TextSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)


class TextInputLayout(SmartInputLayout):
    """

    """
    def __init__(self, parent, textbox=None, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)
        #
        # self.label = wx.StaticText(self.parent, label=label, size=(150, -1))

        if textbox:
            self.textbox = textbox
        else:
            self.textbox = TextSmartBox(parent)

        # if kwargs.get('postbox'):
        #     self.postbox = kwargs.get('postbox')

        self.do_layout()

