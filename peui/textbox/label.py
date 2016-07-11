import os
import sys

import wx

__author__ = 'jbui'


class Label(wx.StaticText):
    """
    PEC-GUI Label with tooltip.

    """
    def __init__(self, message=None, *args, **kwargs):
        wx.StaticText.__init__(self, *args, **kwargs)

        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

