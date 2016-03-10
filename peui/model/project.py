import os
import json

__author__ = 'jbui'


class Project(object):
    """
    Project of the model.
    """
    def __init__(self, *args, **kwargs):
        self.keys = kwargs.get('keys', {})

        self.controller = None

        self.name = kwargs.get('name', 'NA Project')
        self.author = kwargs.get('author', 'Anonymous')
        self.project_folder = kwargs.get('project_folder', os.getcwd())

    def save(self, path):
        """

        :param path:
        """
        data = self.get_json()

        json.dump(data, open(path, "wb"), sort_keys=True, indent=4)

    def load(self, path):
        """
        Load json.
        :param path:
        """
        data = json.load(open(path, "rb"))

        self.load_json(data)

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
    def author(self):
        """
        Author of the model.
        :return:
        """
        return self.keys.get('author')

    @author.setter
    def author(self, value):
        self.keys['author'] = value

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

    def get_json(self):
        return {
            'name': self.name,
            'author': self.author,
        }

    def load_json(self, data):
        self.name = data.get('name')
        self.author = data.get('author')
