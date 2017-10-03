import wx
import wx.lib.agw.ribbon as RB
import wx.lib.agw.ribbon.art


__author__ = 'Joeny'


class CustomRibbonBar(RB.RibbonBar):
    """

    """
    def __init__(self, parent, controller, **kwargs):
        """

        :param parent:
        :param controller:
        :param kwargs:
        :return:
        """
        RB.RibbonBar.__init__(self, parent)

        self.controller = controller

        self.menus = {}

        self.home = RB.RibbonPage(self, wx.ID_ANY, "Examples")
