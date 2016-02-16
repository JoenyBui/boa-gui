from . import ChildController

__author__ = 'jbui'


class Chart2dController(ChildController):

    def __init__(self, parent, view):
        ChildController.__init__(self, parent, view)

    def do_layout(self):
        data = self.parent.project.data

        self.view.axes.plot(data[0], data[1])

    def update_layout(self):
        pass

    def refresh(self):
        pass
