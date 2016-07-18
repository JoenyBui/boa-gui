from abc import ABCMeta, abstractmethod

import wx
from wx.lib.pubsub import pub

__author__ = 'jbui'


class BaseController(object):
    """

    """
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.title = kwargs.get('title', '')

    @abstractmethod
    def sync_data(self):
        ""

        pass

    def register_two_way_bind(self, view_ctrl, view_message, view_function,
                              model_message, model_function):
        """
        Register two way binding.
        :param view_ctrl:
        :param view_message:
        :param view_function:
        :param model_message:
        :param model_function:
        :return:
        """
        view_ctrl.Bind(view_message, view_function)
        pub.subscribe(model_function, model_message)

    def register_two_way_textbox_bind(self, view_ctrl, view_function, model_message, model_function):
        """

        :param view_ctrl:
        :param view_function:
        :param model_message:
        :param model_function:
        :return:
        """
        view_ctrl.textbox.Bind(wx.EVT_TEXT, view_function)

        if view_ctrl.postbox:
            view_ctrl.postbox.Bind(wx.EVT_TEXT, view_function)

        pub.subscribe(model_function, model_message)


class ChildController(BaseController):
    """

    """
    __metaclass__ = ABCMeta

    def __init__(self, parent, view, *args, **kwargs):
        """

        :param parent:
        :param view:
        :param args:
        :param kwargs:
        :return:
        """
        BaseController.__init__(self)

        self.parent = parent
        self.view = view

    @abstractmethod
    def do_layout(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def update_layout(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def refresh(self):
        """

        :return:
        """
        pass


