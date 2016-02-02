import wx

__author__ = 'jbui'


class ProjectTree(wx.TreeCtrl):
    """
    Project Tree Structure
    """

    def __init__(self, parent, id, project):
        wx.TreeCtrl.__init__(self, parent, id)

        self.project = project
