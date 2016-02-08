import wx

from .smart import SmartTextBox

__author__ = 'jbui'


class IntSmartBox(SmartTextBox):

    def __init__(self, parent, *args, **kwargs):
        SmartTextBox.__init__(self, parent, *args, **kwargs)

