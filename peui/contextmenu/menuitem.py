import wx

__author__ = 'jbui'


class MenuItem(wx.MenuItem):

    def __init__(self, *args, **kwargs):
        wx.MenuItem.__init__(self, *args, **kwargs)

        self.keys = {}

    @property
    def uuid(self):
        return self.keys.get('uuid')

    @uuid.setter
    def uuid(self, value):
        self.keys['uuid'] = value

