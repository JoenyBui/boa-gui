import os
import json
import getpass

__author__ = 'jbui'


class Setting(object):
    """
    Settings file is stored in the user local settings folder.

    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.keys = {}

        self.folder = kwargs.get('folder', '.peui')
        self.file = self.get_temp_folder(self.folder)

        if os.path.isfile(self.file):
            self.load(self.file)
        else:
            self.template()
            self.save(self.file)

    def template(self):
        """

        :return:
        """
        keys = dict(
            author=self.author,
            project_name=self.project_name,
            company=self.company,
            path=self.get_home_folder(),
            esignature=self.esignature,
            ekey=self.ekey,
            efile=self.efile
        )

        self.keys = keys

    @property
    def author(self):
        """

        :return:
        """
        return self.keys.get('author', getpass.getuser())

    @author.setter
    def author(self, value):
        """

        :param value:
        :return:
        """
        self.keys['author'] = value

    @property
    def company(self):
        """
        Get the company

        """
        return self.keys.get('company', '')

    @company.setter
    def company(self, value):
        """
        Set the company

        """
        self.keys['company'] = value

    @property
    def project_name(self):
        """
        Get the project name

        :return:
        """
        return self.keys.get('project_name', 'Project')

    @project_name.setter
    def project_name(self, value):
        """
        Set the project name

        :param value:
        :return:
        """
        self.keys['project_name'] = value

    @property
    def path(self):
        """

        :return:
        """
        return self.keys.get('path', self.get_home_folder())

    @path.setter
    def path(self, value):
        """

        :param value:
        :return:
        """
        self.keys['path'] = value

    @property
    def efile(self):
        """
        Get electronic file

        :return:
        """
        return self.keys.get('efile', 'FILE')

    @efile.setter
    def efile(self, value):
        """
        Set electronic file

        :param value:
        :return:
        """
        self.keys['efile'] = value

    @property
    def ekey(self):
        """
        Get electronic key

        :return:
        """
        return self.keys.get('ekey', 'KEY')

    @ekey.setter
    def ekey(self, value):
        """
        Set electronic key

        :param value:
        :return:
        """
        self.keys['ekey'] = value

    @property
    def esignature(self):
        """
        Get electronic signature

        :return:
        """
        return self.keys.get('esignature', 'SIGNATURE')

    @esignature.setter
    def esignature(self, value):
        """
        Set electronic signature

        :param value:
        :return:
        """
        self.keys['esignature'] = value

    @staticmethod
    def get_home_folder():
        """
        Get the home folder.

        :return:
        """
        temp_folder = os.path.expanduser('~')

        if os.name == 'nt':
            # In window we store in user temporary folder
            temp_folder = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']

        return temp_folder

    def get_temp_folder(self, folder):
        """
        Get temporary folder.

        :return:
        """
        temp_folder = self.get_home_folder()

        path = os.path.join(temp_folder, folder)
        if not os.path.isdir(path):
            os.mkdir(path)

        return os.path.join(path, 'settings.json')

    def load(self, file_path):
        """
        Load file

        :param file_path:
        :return:
        """
        with open(file_path) as data_file:
            self.keys = json.load(data_file)

    def save_to_settings(self):
        """
        Save to settings

        :return:
        """
        self.save(self.file)

    def save(self, file_path):
        """

        :param file_path:
        :return:
        """
        with open(file_path, 'w') as outfile:
            json.dump(self.keys, outfile, sort_keys=True, indent=4)
