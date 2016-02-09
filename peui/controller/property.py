__author__ = 'jbui'


class PropertyGridController(object):
    """
    Property Grid Controller

    """
    def __init__(self, parent, view, *args, **kwargs):
        """

        :param parent: Main Controller.
        :param view: Property Grid View.
        :param args:
        :param kwargs:
        :return:
        """
        self.parent = parent
        self.project = parent.project
        self.view = view

    def do_layout(self):
        self.view.add_category_property('General Information')
        self.view.add_string_property('File Name', 'name', self.project.name, 'Project File Name.')
        self.view.add_string_property('Author Name', 'author', self.project.author, 'Author Name')
        self.view.add_file_property('Project Path', 'path', self.project.project_folder, 'Project Folder')

    def refresh(self):
        self.do_layout()
