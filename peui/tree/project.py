import wx

__author__ = 'jbui'


class ProjectTree(wx.TreeCtrl):
    """
    Project Tree Structure
    """

    def __init__(self, parent, controller, project, **kwargs):
        id = kwargs.get('id', -1)
        wx.TreeCtrl.__init__(self, parent, id=id)

        self.project = project
        self.controller = controller
