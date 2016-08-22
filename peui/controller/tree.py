import pecutil.folder

from . import ChildController

__author__ = 'jbui'


class TreeController(ChildController):
    """
    Tree Controller

    """
    def __init__(self, parent, view, *args, **kwargs):
        ChildController.__init__(self, parent, view)

    def do_layout(self):
        """

        :return:
        """
        directory = pecutil.folder.get_directory_structure(self.parent.project.project_folder)

        # if self.view.IsEmpty():
        self.view.DeleteAllItems()

        self.view.add_root(directory)

    def update_layout(self):
        """

        :return:
        """
        pass

    def refresh(self):
        """
        Refresh model.
        :return:
        """

        self.update_layout()

    def sync_data(self):
        """

        :return:
        """
        pass
