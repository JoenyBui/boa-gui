from abc import ABCMeta, abstractmethod

__author__ = 'jbui'


class ChildController(object):
    __metaclass__ = ABCMeta

    def __init__(self, parent, view):
        self.parent = parent
        self.view = view

    @abstractmethod
    def do_layout(self):
        pass

    @abstractmethod
    def update_layout(self):
        pass

    @abstractmethod
    def refresh(self):
        pass


