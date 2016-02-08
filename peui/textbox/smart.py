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

        wx.BoxSizer.__init__(self, wx.HORIZONTAL)

        self.parent = parent

        self.label = None
        self.textbox = None
        self.postbox = None     # Additional placeholder that is significant (unit box, path button, etc.)

        # Call do_layout after you have populate the label, textbox, and/or postbox

    def do_layout(self):
        """

        :return:
        """
        if self.label:
            self.Add(wx.StaticText(self.parent, label=self.label), 0,
                     wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        if self.textbox:
            self.Add(self.textbox, 1, wx.EXPAND)

        if self.postbox:
            self.Add(self.postbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT)
