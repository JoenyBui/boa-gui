import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class IntSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)


class IntInputLayout(SmartInputLayout):

    def __init__(self, parent, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        self.label = kwargs.get('label', 'Input Label:')
        self.textbox = kwargs.get('textbox', IntSmartBox(parent))

        if kwargs.get('postbox'):
            self.postbox = kwargs.get('postbox')

        self.do_layout()
