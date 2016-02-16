import wx

__author__ = 'jbui'


class GeneralDialog(wx.Dialog):
    """

    Flags
        wx.OK               Creates an OK button
        wx.CANCEL           Creates a Cancel button
        wx.YES              Creates a Yes button
        wx.NO               Creates a No button
        wx.HELP             Creates a Help button
        wx.NO_DEFAULT       Sets the No button as the default
    """
    def __init__(self, parent, controller=None, local=None, btn_flags=wx.OK | wx.CANCEL):
        wx.Dialog.__init__(self, parent)

        self.controller = controller
        self.local = local

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)

        btnsizer = self.CreateButtonSizer(btn_flags)

        vsizer.Add(self.do_layout())
        vsizer.AddSpacer(10)
        vsizer.Add(btnsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(vsizer)
        self.SetInitialSize()
        self.CenterOnParent()

    def do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)


        return vsizer