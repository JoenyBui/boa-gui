import wx
from wx import propgrid

from ..controller.property import PropertyGridController

__author__ = 'jbui'


class PropGrid(propgrid.PropertyGrid):
    """
    Property Grid.

    """
    def __init__(self, parent, controller, local, size=(100, 50), *args, **kwargs):
        """
        Property grid view.

        :param parent: main frame
        :param controller:
        :param local: pass in the local controller for this view
        :param size:
        :param args:
        :param kwargs:
        :return:
        """
        # if not kwargs.get('size'):
        #     kwargs['size'] = (200, 150)

        propgrid.PropertyGrid.__init__(self, parent, size=size, *args, **kwargs)

        if local:
            self.controller = local
        else:
            self.controller = PropertyGridController(controller, self)

        if not local:
            self.controller.do_layout()

    def add_category_property(self, name, enabled=True, **kwargs):
        """
        Add category property.

        :param name:
        :param enabled:
        :param kwargs:
        :return:
        """

        return self.Append(propgrid.PropertyCategory(name))

    def add_file_property(self, name, key, value, status, enabled=True, **kwargs):
        """
        Add file property.

        :param name:
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.FileProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_int_property(self, name, key, value, status, enabled=True, **kwargs):
        """
        Add integer property.

        :param name:
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.IntProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_string_property(self, name, key, value, status, enabled=True, **kwargs):
        """
        Add string property.

        :param name:
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.StringProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_float_property(self, name, key, value, status, enabled=True, **kwargs):
        """
        Add float property.

        :param name: title
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.FloatProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_bool_property(self, name, key, value, status, enabled=True, **kwargs):
        """
        Add boolean property.

        :param name:
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.BoolProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyAttribute(key, "UseCheckbox", True)
        self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_enum_property(self, name, key, value, status, enabled=True, **kwargs):
        """
        Add enumerator property.

        :param name:
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
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

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_multi_button(self, enabled=True, **kwargs):
        """
        Add multi-button.

        :param enabled:
        :param kwargs:
        :return:
        """
        buttons = propgrid.PGMultiButton(self, wx.Size(10, 10))
        buttons.Add('...')
        buttons.Add('A')

        buttons.Finalize(self, wx.Point(1, 1))

        self.Append(buttons)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return buttons

    def delete_item(self, key):
        """
        Delete Item Property.

        :param key:
        """
        self.DeleteProperty(key)
