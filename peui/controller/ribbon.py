from . import BaseController

__author__ = 'jbui'


class RibbonController(BaseController):

    def __init__(self, parent):
        BaseController.__init__(self)

        self.parent = parent

    def sync_data(self):
        pass