import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class TextSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)


class TextInputLayout(SmartInputLayout):

    def __init__(self, parent, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        # if kwargs.get('label'):
        #     self.label = kwargs.get('label')
        # else:
        #     self.label = wx.StaticText(self.parent, label="TextBox Label:", size=(150, -1))

        if kwargs.get('textbox'):
            self.textbox = kwargs.get('textbox')
        else:
            self.textbox = TextSmartBox(parent)

        # if kwargs.get('postbox'):
        #     self.postbox = kwargs.get('postbox')

        self.do_layout()

