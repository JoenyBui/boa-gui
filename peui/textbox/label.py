import os
import sys

import wx

__author__ = 'jbui'


class SmartLabel(wx.StaticText):
    """
    PEC-GUI Label with tooltip.

    """
    def __init__(self, parent=None, label="", message=None, font=None, wrap=None, alignment=None, *args, **kwargs):
        wx.StaticText.__init__(self, parent=parent, label=label, *args, **kwargs)

        self.tooltip = None
        if message:
            self.tooltip = wx.ToolTip(message)
            self.SetToolTip(self.tooltip)

        if font:
            self.SetFont(font)

        if wrap:
            self.Wrap(wrap)

        if alignment:
            if alignment == 'left':
                self.SetWindowStyle(wx.ALIGN_LEFT)
            elif alignment == 'right':
                self.SetWindowStyle(wx.ALIGN_RIGHT)
            elif alignment == 'center':
                self.SetWindowStyle(wx.ALIGN_CENTER)

    def set_value(self, value):
        # type: (object) -> object
        """
        Set text value

        :param value:
        :return:
        """
        self.Label = value

    def get_value(self):
        """
        Get text value

        :return:
        """
        return self.Label
