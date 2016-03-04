from . import ChildController

__author__ = 'jbui'


class XlsxController(ChildController):

    def __init__(self, parent, view):
        ChildController.__init__(self, parent, view)

    def do_layout(self):
        pass

    def update_layout(self):
        pass

    def refresh(self):
        pass

    def sync_data(self):
        pass
