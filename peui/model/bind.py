import wx
from wx.lib.pubsub import pub

__author__ = 'jbui'


class BindOjbect(object):
    """
    Bind Object Model

    """
    def __init__(self, model, view, key, *args, **kwargs):
        """

        :param model:
        :param view:
        :param key:
        :param args:
        :param kwargs:
        :return:
        """
        self.id = wx.ID_ANY

        self.model = model
        self.view = view
        self.key = key

        # Sync Data
        self.view.set_value(self.model[self.key])

        # Subscribe to model-to-view.
        pub.subscribe(self.model_to_view, self.M2V)

        self.view.Bind(wx.EVT_TEXT, self.view_to_model)

    @property
    def M2V(self):
        """

        :return:
        """
        return 'M2V-%d'%self.id

    @property
    def V2M(self):
        """

        :return:
        """
        return 'V2M-%d'%self.id

    def model_to_view(self, event):
        """

        :param event:
        :return:
        """
        self.view.set_value(self.model)

    def view_to_model(self, event):
        """

        :param event:
        :return:
        """
        self.model[self.key] = self.view.get_value()
