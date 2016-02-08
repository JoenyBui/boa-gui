import wx

from .smart import SmartTextBox

__author__ = 'jbui'


class FloatSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)
