import wx

__author__ = 'Joeny'


class CustomStatusBar(wx.StatusBar):
    """

    """
    def __init__(self, parent):
        """

        :param parent:
        :return:
        """
        wx.StatusBar.__init__(self, parent, -1)
