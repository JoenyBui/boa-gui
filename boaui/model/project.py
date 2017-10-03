import os
import json

__author__ = 'Joeny'


class Project(object):
    """
    Project of the model.

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        self.keys = kwargs.get('keys', {})

        # Overall setting
        self.setting = kwargs.get('setting', None)

        self.controller = None

        if self.setting:
            self.name = self.setting.project_name
            self.author = self.setting.author
            self.project_folder = self.setting.path

        else:
            self.name = kwargs.get('name', 'NA Project')
            self.author = kwargs.get('author', 'Anonymous')
            self.project_folder = kwargs.get('project_folder', os.getcwd())

    def save(self, path):
        """
        Save project model.

        :param path:
        """
        data = self.get_json()

        json.dump(data, open(path, "wb"), sort_keys=True, indent=4)

    def load(self, path):
        """
        Load project json data.

        :param path: file path
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
        """

        :param value:
        :return:
        """
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
        """

        :param value:
        :return:
        """
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
        """

        :param value:
        :return:
        """
        self.keys['project_folder'] = value

    def get_json(self):
        """

        :return:
        """
        return {
            'name': self.name,
            'author': self.author,
        }

    def load_json(self, data):
        """

        :param data:
        :return:
        """
        self.name = data.get('name')
        self.author = data.get('author')
