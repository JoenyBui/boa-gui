import os
import sys

import wx

__author__ = 'jbui'


class SmartLabel(wx.StaticText):
    """
    PEC-GUI Label with tooltip.

    """
    def __init__(self, parent=None, message=None, *args, **kwargs):
        wx.StaticText.__init__(self, parent=parent, *args, **kwargs)

        self.tooltip = None
        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

