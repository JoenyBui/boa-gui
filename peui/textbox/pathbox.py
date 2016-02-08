import wx

from .smart import SmartTextBox, SmartInputLayout

__author__ = 'jbui'


class PathSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)


class PathInputLayout(SmartInputLayout):

    def __init__(self, parent, *args, **kwargs):
        SmartInputLayout.__init__(self, parent, *args, **kwargs)

        self.label = kwargs.get('label', 'Path:')
        self.textbox = kwargs.get('textbox', PathSmartBox(parent))

        if kwargs.get('postbox'):
            self.postbox = kwargs.get('postbox')

        self.do_layout()
