import wx
from wx import propgrid

from ..controller.property import PropertyGridController

__author__ = 'jbui'


class PropGrid(propgrid.PropertyGrid):
    """

    """
    def __init__(self, parent, controller, local, *args, **kwargs):
        """
        Property grid view.
        :param parent: main frame
        :param controller:
        :param local: pass in the local controller for this view
        :param args:
        :param kwargs:
        :return:
        """
        if not kwargs.get('size'):
            kwargs['size'] = (200, 150)

        propgrid.PropertyGrid.__init__(self, parent, *args, **kwargs)

        if local:
            self.controller = local
        else:
            self.controller = PropertyGridController(controller, self)

        if not local:
            self.controller.do_layout()

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

    def add_enum_property(self, name, key, value, status, **kwargs):
        if isinstance(value, tuple):
            arr_label = []
            arr_values = []
            
            for lb, val in value:
                arr_label.append(lb)
                arr_values.append(val)

        else:
            arr_label = value
            arr_values = value

        if kwargs.get('edit'):
            item = propgrid.EditEnumProperty(name, key, arr_label, arr_values)
        else:
            item = propgrid.EnumProperty(name, key, arr_label, arr_values)

        self.Append(item)
        self.SetPropertyHelpString(key, status)
        return item
