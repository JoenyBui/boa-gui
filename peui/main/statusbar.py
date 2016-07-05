import wx

__author__ = 'jbui'


class CustomStatusBar(wx.StatusBar):
    """

    """
    def __init__(self, parent):
        """

        :param parent:
        :return:
        """
        wx.StatusBar.__init__(self, parent, -1)
