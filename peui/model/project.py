import json

__author__ = 'jbui'


class Project(object):
    """
    Project of the model.
    """
    def __init__(self, *args, **kwargs):
        self.keys = kwargs.get('keys', {})

        self.controller = None

        self.name = kwargs.get('name', '')

    def save(self, path):
        """

        :param path:
        """
        data = {
            'keys': self.keys
        }

        json.dump(data, open(path, "wb"))

    def load(self, path):
        """
        Load json.
        :param path:
        """
        data = json.load(open(path, "rb"))

        self.keys = data['keys']

    @property
    def name(self):
        """
        Name of the file.
        :return:
        """
        return self.keys.get('name')

    @name.setter
    def name(self, value):
        self.keys['name'] = value

    @property
    def project_folder(self):
        """
        Specify the Project Folder
        :return:
        """
        return self.keys.get('project_folder')

    @project_folder.setter
    def project_folder(self, value):
        self.keys['project_folder'] = value
