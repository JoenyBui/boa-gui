import pecutil.folder

__author__ = 'jbui'


class TreeController(object):
    """
    Tree Controller

    """
    def __init__(self, parent, view, *args, **kwargs):

        self.parent = parent
        self.project = parent.project
        self.view = view

    def do_layout(self):
        """

        :return:
        """
        directory = pecutil.folder.get_directory_structure(self.project.project_folder)

        # if self.view.IsEmpty():
        self.view.DeleteAllItems()

        self.view.add_root(directory)

    def refresh(self):
        """
        Refresh model.
        :return:
        """
        self.do_layout()
