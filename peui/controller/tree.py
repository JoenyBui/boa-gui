import pecutil.folder

__author__ = 'jbui'


class TreeController(object):
    """
    Tree Controller

    """
    def __init__(self, parent, view, *args, **kwargs):

        self.parent = parent
        self.view = view
        self.do_layout()

    def do_layout(self):
        """

        :return:
        """
        directory = pecutil.folder.get_directory_structure(self.parent.project.project_folder)

        # if self.view.IsEmpty():
        self.view.DeleteAllItems()

        self.view.add_root(directory)

    def update_layout(self):
        pass

    def refresh(self):
        """
        Refresh model.
        :return:
        """

        self.update_layout()