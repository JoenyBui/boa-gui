import wx

__author__ = 'jbui'


class GeneralPanel(wx.Panel):

    def __init__(self, parent=None, **kwargs):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)


        self.SetSizer(sizer)
