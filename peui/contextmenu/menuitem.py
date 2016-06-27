import wx

__author__ = 'jbui'


class MenuItem(wx.MenuItem):
    """

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        wx.MenuItem.__init__(self, *args, **kwargs)

        self.keys = {}

    @property
    def uuid(self):
        """

        :return:
        """
        return self.keys.get('uuid')

    @uuid.setter
    def uuid(self, value):
        """

        :param value:
        :return:
        """
        self.keys['uuid'] = value

