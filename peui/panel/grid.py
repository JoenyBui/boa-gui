import wx
from wx import propgrid

from ..controller.property import PropertyGridController

__author__ = 'jbui'


class PropGrid(propgrid.PropertyGrid):
    """
    Property Grid.

        * PropertyCategory
            pg.Append( wxpg.PropertyCategory("1 - Basic Properties") )

        * StringProperty
            pg.Append( wxpg.StringProperty("String",value="Some Text") )

        * IntProperty
            pg.Append( wxpg.IntProperty("Int",value=100) )

            pg.Append( wxpg.IntProperty("IntWithSpin",value=256) )
            pg.SetPropertyEditor("IntWithSpin","SpinCtrl")

        * UIntProperty
            pg.Append( wxpg.UIntProperty("UInt",value=100) )

        * FloatProperty
            pg.Append( wxpg.FloatProperty("Float",value=100.0) )

        * BoolProperty
            pg.Append( wxpg.BoolProperty("Bool",value=True) )
            pg.Append( wxpg.BoolProperty("Bool_with_Checkbox",value=True) )
            pg.SetPropertyAttribute("Bool_with_Checkbox", "UseCheckbox", True)

        * EnumProperty
            pg.Append( wxpg.EnumProperty("Enum","Enum", ['wxPython Rules', 'wxPython Rocks', 'wxPython Is The Best'], [10,11,12], 0) )

        * EditEnumProperty
            pg.Append( wxpg.EditEnumProperty("EditEnum","EditEnumProperty", ['A','B','C'], [0,1,2], "Text Not in List") )

        * FlagsProperty

        * LongStringProperty
            pg.Append( wxpg.LongStringProperty("LongString", value="This is a\\nmulti-line string\\nwith\\ttabs\\nmixed\\tin."))

        * FileProperty
            pg.Append( wxpg.FileProperty("File",value="C:\\Windows\\system.ini") )

        * DirProperty
            pg.Append( wxpg.DirProperty("Dir",value="C:\\Windows") )

        * ArrayStringProperty
            pg.Append( wxpg.ArrayStringProperty("ArrayString",value=['A','B','C']) )

        * FontProperty
            pg.Append( wxpg.FontProperty("Font",value=panel.GetFont()) )

        * SystemColourProperty
            pg.Append( wxpg.SystemColourProperty("SystemColour") )

        * ColourProperty
            pg.Append( wxpg.ColourProperty("Colour", value=panel.GetBackgroundColour()) )

        * CursorProperty

        * ImageFileProperty
            pg.Append( wxpg.ImageFileProperty("ImageFile") )

        * MultiChoiceProperty
            pg.Append( wxpg.MultiChoiceProperty("MultiChoice", choices=['wxWidgets','QT','GTK+']) )

        * DateProperty
            pg.Append( wxpg.DateProperty("Date",value=wx.DateTime_Now()) )

            pg.SetPropertyAttribute( "Date", wxpg.PG_DATE_PICKER_STYLE, wx.DP_DROPDOWN|wx.DP_SHOWCENTURY )


    PGCell
        * GetData
        * HasText
        * SetEmptyData
        * MergeFrom
        * SetText
        * SetBitmap
        * SetFgCol
        * SetFont
        * SetBgCol
        * GetText
        * GetBitmap
        * GetFgCol
        * GetFont
        * GetBgCol
        * IsInvalid

    """
    def __init__(self, parent, controller, local, size=(100, 50), column=None, *args, **kwargs):
        """
        Property grid view.

        :param parent: parent main frame
        :param controller: parent controller
        :param local: pass in the local controller for this view
        :param size: set the initial size of the panel
        :param column: set the number of column
        :param args: arguments
        :param kwargs: additional keywords
        :return:
        """
        propgrid.PropertyGrid.__init__(self, parent, size=size, *args, **kwargs)

        # Add the number of column.
        if column:
            self.SetColumnCount(column)

            # Change Selection Setting.
            self.SetMarginColour(wx.LIGHT_GREY)
            self.SetSelectionBackgroundColour(wx.WHITE)
            self.SetSelectionTextColour(wx.BLACK)
            self.SetCaptionTextColour(wx.BLACK)

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

        # if enabled:
        #     self.EnableProperty(key)
        # else:
        #     self.DisableProperty(key)

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

    def add_multi_button(self, name, key, value, enabled=True, **kwargs):
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

    def get_item(self, key):
        """
        Return the PGProperty item.

        :param key: name of key
        :return:
        """
        return self.GetPropertyByName(key)

    def get_cell(self, key, column):
        """
        Return the cell inside the property item.

        :param key: name of property key
        :param column: column of item (0 index)
        :return:
        """
        cell = self.get_item(key)

        return cell.GetCell(column)

    def set_text(self, key, column, value):
        """
        Set the cell value for the property item.

        :param key: name of property key
        :param column: column of item (0 index)
        :param value: item name
        :return:
        """

        cell = self.get_cell(key, column)

        cell.SetText(str(value))

    def get_text(self, key, column):
        """
        Return the cell value for the property item column.

        :param key: name of property key
        :param column: column of item (0 index)
        """
        cell = self.get_cell(key, column)

        return cell.GetText()

    def get_data(self, key, column):
        """
        Return the cell value for the property item column.

        :param key: name of property key
        :param column: column of item (0 index)
        """
        cell = self.get_cell(key, column)

        return cell.GetData()

    def delete_item(self, key):
        """
        Delete the PGProperty Item.

        :param key: name of key
        """
        self.DeleteProperty(key)

