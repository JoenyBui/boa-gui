import sys
import wx


__author__ = 'jbui'


class Console(wx.Panel):

    def __init__(self, parent, controller):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        # Add a panel so it looks the correct on all platforms
        style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
        log = wx.TextCtrl(self, wx.ID_ANY, size=(800, 300), style=style)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(sizer)

        log.BackgroundColour = wx.BLACK
        log.ForegroundColour = wx.WHITE

        # redirect text here
        sys.stdout = log
