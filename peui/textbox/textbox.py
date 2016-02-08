import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class TextSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)


class TextInputLayout(SmartInputLayout):

    def __init__(self, parent, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        self.label = kwargs.get('label', 'Textbox Label:')
        self.textbox = kwargs.get('textbox', TextSmartBox(parent))

        if kwargs.get('postbox'):
            self.postbox = kwargs.get('postbox')

        self.do_layout()
