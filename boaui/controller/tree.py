import boautil.folder

from . import PaneController

__author__ = 'Joeny'


class TreeController(PaneController):
    """
    Tree Controller

    """
    def __init__(self, parent, view, *args, **kwargs):
        """
        Constructor

        :param parent:
        :param view:
        :param args:
        :param kwargs:
        :return:
        """
        PaneController.__init__(self, parent, view, *args, **kwargs)

    def do_layout(self):
        """
        Draw layout
        
        :return:
        """
        directory = boautil.folder.get_directory_structure(self.parent.project.project_folder)

        # if self.view.IsEmpty():
        self.view.DeleteAllItems()

        self.view.add_root(directory)

    def refresh(self):
        """
        Refresh model.
        :return:
        """
        pass

    def sync_data(self):
        """

        :return:
        """
        pass
