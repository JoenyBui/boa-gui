from . import BaseController

__author__ = 'jbui'


class PropertyGridController(BaseController):
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
        BaseController.__init__(self)

        self.parent = parent
        self.view = view
        self.cells = dict()

    def do_layout(self):
        """

        :return:
        """
        item = self.view.add_category_property('General Information')

        self.cells['name'] = self.view.add_string_property('File Name', 'name', self.parent.project.name, 'Project File Name.')
        self.cells['author'] = self.view.add_string_property('Author Name', 'author', self.parent.project.author, 'Author Name')
        self.cells['project_folder'] = self.view.add_file_property('Project Path', 'project_folder', self.parent.project.project_folder, 'Project Folder')

    def update_layout(self):
        """

        :return:
        """
        self.cells['name'].m_value = self.parent.project.name
        self.cells['author'].m_value = self.parent.project.author
        self.cells['project_folder'].m_value = self.parent.project.project_folder

    def refresh(self):
        """

        :return:
        """
        self.update_layout()

    def sync_data(self):
        """

        :return:
        """
        pass

    def clear_control(self):
        pass

