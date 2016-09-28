from wx import propgrid

from . import PaneController

__author__ = 'jbui'


class PropertyGridController(PaneController):
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
        PaneController.__init__(self, parent, view, *args, **kwargs)

        self.cells = dict()

    def do_layout(self):
        """
        Demo.

        :return:
        """
        # self.view.Append(propgrid.LongStringProperty("MultipleButtons"))
        # self.view.SetPropertyEditor("MultipleButtons", "MultiButtonEditor")
        #
        # item = self.view.add_multi_choice('MultiChoice', 'mc', ['wxWidget', 'QT', 'GTK'])

        item = self.view.add_category_property('General Information')

        self.cells['name'] = self.view.add_string_property('File Name', 'name', self.parent.project.name, 'Project File Name.')
        self.cells['author'] = self.view.add_string_property('Author Name', 'author', self.parent.project.author, 'Author Name')
        self.cells['project_folder'] = self.view.add_file_property('Project Path', 'project_folder', self.parent.project.project_folder, 'Project Folder')

    def refresh(self):
        """

        :return:
        """
        self.cells['name'].m_value = self.parent.project.name
        self.cells['author'].m_value = self.parent.project.author
        self.cells['project_folder'].m_value = self.parent.project.project_folder

    def sync_data(self):
        """

        :return:
        """
        pass

    def clear_control(self):
        pass
