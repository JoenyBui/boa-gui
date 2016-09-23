from abc import ABCMeta, abstractmethod
from ..config import EVT_CHANGE_STATE

import wx
from wx.lib.pubsub import pub

__author__ = 'jbui'


class BaseController(object):
    """
    Base Controller

    """
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', '')

        self.bind_objects = {}
        self.state = None

    @abstractmethod
    def sync_data(self):
        """
        Sync data with the view

        """
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
    Child Controller

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
        BaseController.__init__(self, *args, **kwargs)

        self.parent = parent
        self.view = view
        self.key = None

        pub.subscribe(self.update_layout, EVT_CHANGE_STATE)

    @abstractmethod
    def do_layout(self):
        """
        Draw the layout

        :return:
        """
        pass

    @abstractmethod
    def update_layout(self, state):
        """
        Update layout based off of change state.

        :return:
        """
        pass

    @abstractmethod
    def refresh(self):
        """

        :return:
        """
        pass

    def delete_control(self):
        """
        Remove the pane, delete the pointer in parent windows, and than remove self from child.

        """
        if self.parent.windows:
            self.parent.delete_pane(self.key)

            del self.parent.windows[self.key]
