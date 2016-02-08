import re

import wx

__author__ = 'jbui'


class SmartTextBox(wx.TextCtrl):
    """
    Create a smartter text box that could capture keys and process them
    to see if the format is correct.
    """
    def __init__(self, parent, *args, **kwargs):
        wx.TextCtrl.__init__(self, *args, **kwargs)

        self.parent = parent
