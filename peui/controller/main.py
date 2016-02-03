from ..controller.main import *

__author__ = 'jbui'


class MainController(object):
    """
    Main Controller
    """

    def __init__(self, project):
        self.project = project

        # Add controller to project
        self.project.controller = self

        self.frame = None

        self.binds = dict(
            METHOD_OPEN_PROJECT=self.open_project,
            METHOD_SAVE_PROJECT=self.save_project,
            METHOD_SAVE_AS_PROJECT=self.save_as_project,
            METHOD_CLOSE_PROJECT=self.close_project
        )

    def open_project(self, event):
        pass

    def save_project(self, event):
        pass

    def save_as_project(self, event):
        pass

    def close_project(self, event):
        self.frame.Close(True)
        self.frame.Destroy()
        event.Skip()

    def about(self, event):
        pass
