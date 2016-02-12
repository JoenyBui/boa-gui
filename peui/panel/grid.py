import wx
from wx import propgrid

from ..controller.property import PropertyGridController

__author__ = 'jbui'


class PropGrid(propgrid.PropertyGrid):
    """

    """
    def __init__(self, parent, controller, *args, **kwargs):
        """
        Property grid view.
        :param parent: main frame
        :param controller:
        :param args:
        :param kwargs:
        :return:
        """
        if not kwargs.get('size'):
            kwargs['size'] = (200, 150)

        propgrid.PropertyGrid.__init__(self, parent, *args, **kwargs)

        if kwargs.get('grid_controller'):
            self.controller = kwargs.get('self_controller')
        else:
            self.controller = PropertyGridController(controller, self)

    def add_category_property(self, name, **kwargs):
        self.Append(propgrid.PropertyCategory(name))

    def add_file_property(self, name, key, value, status, **kwargs):
        item = propgrid.FileProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)
        return item

    def add_int_property(self, name, key, value, status, **kwargs):
        item = propgrid.IntProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)
        return item

    def add_string_property(self, name, key, value, status, **kwargs):
        item = propgrid.StringProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)
        return item

    def add_float_property(self, name, key, value, status, **kwargs):
        item = propgrid.FloatProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)
        return item

    def add_bool_property(self, name, key, value, status, **kwargs):
        item = propgrid.BoolProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyAttribute(key, "UseCheckbox", True)
        self.SetPropertyHelpString(key, status)
        return item
