import re

import wx

__author__ = 'jbui'


class SmartTextBox(wx.TextCtrl):
    """
    Create a smarter text box that could capture keys and process them
    to see if the format is correct.
    """
    def __init__(self, parent, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, *args, **kwargs)

        self.parent = parent


class SmartInputLayout(wx.BoxSizer):
    """
    Create the horizontal layout of smart textbox.


    * --------------------------------------------*
    * |     |                      |              |
    * |     |                      |              |
    * --------------------------------------------*

    """
    def __init__(self, parent, *args, **kwargs):
        wx.BoxSizer.__init__(self, parent, *args, **kwargs)

        self.label = None
        self.textbox = None
        self.postbox = None     # Additional placeholder that is significant (unit box, path button, etc.)

        # Call do_layout after you have populate the label, textbox, and/or postbox

    def do_layout(self):
        if self.label:
            self.AddSpacer(10)
            self.Add(self.label)

        if self.textbox:
            self.AddSpacer(5)
            self.Add(self.textbox)

        if self.postbox:
            self.AddSpacer(5)
            self.Add(self.postbox)
