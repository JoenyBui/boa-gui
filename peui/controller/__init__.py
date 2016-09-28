from abc import ABCMeta, abstractmethod
from ..config import EVT_CHANGE_STATE

import wx
from wx.lib.pubsub import pub

from ..config import STATE_CLOSE_PROJECT

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

    def update_layout(self, state):
        """
        Update layout based off of change state.

        :return:
        """
        if state == STATE_CLOSE_PROJECT:
            self.delete_control()

    @abstractmethod
    def refresh(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def delete_control(self):
        """
        Remove the pane/page, delete the pointer in parent windows, and than remove self from child.

        """
        pass


class TabPageController(ChildController):
    """
    Tab Page Controller

    """
    def __init__(self, parent, view, *args, **kwargs):
        """

        :param parent:
        :param view:
        :param args:
        :param kwargs:
        :return:
        """
        ChildController.__init__(self, parent, view, *args, **kwargs)

    def delete_control(self):
        """
        Remove the page, delete the pointer in the parent window.

        :return:
        """
        if self.parent.windows:
            # Find tab.
            ctrl, idx = self.parent.notebook.FindTab(self.view)

            # Delete page index.
            self.parent.delete_page(idx)

            # Delete parent windows.
            del self.parent.windows[self.key]

            # Add to trash.
            self.parent.trash.append(self)


class PaneController(ChildController):
    """
    Pane Controller

    """
    def __init__(self, parent, view, *args, **kwargs):
        """

        :param parent:
        :param view:
        :param args:
        :param kwargs:
        :return:
        """
        ChildController.__init__(self, parent, view, *args, **kwargs)

    def delete_control(self):
        """
        Remove the pane, delete the pointer in parent windows, and than remove self from child.

        """
        if self.parent.windows:
            # Delete pane from frame manager.
            self.parent.delete_pane(self.key)

            # Delete parent windows.
            del self.parent.windows[self.key]

            # Add to trash.
            self.parent.trash.append(self)
