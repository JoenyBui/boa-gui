import sys

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
    def __init__(self, parent, controller, local, size=(100, 50), column=None, editable=None,
                 style=propgrid.PG_SPLITTER_AUTO_CENTER, *args, **kwargs):
        """
        Property grid view.

        :param parent: parent main frame
        :param controller: parent controller
        :param local: pass in the local controller for this view
        :param size: set the initial size of the panel
        :param column: set the number of column
        :param editable: an array of integer index
        :param args: arguments
        :param kwargs: additional keywords
        :return:
        """
        propgrid.PropertyGrid.__init__(self, parent, size=size, style=style, *args, **kwargs)

        # Add the number of column.
        if column:
            self.SetColumnCount(column)

            # Change Selection Setting.
            self.SetMarginColour(wx.LIGHT_GREY)
            self.SetSelectionBackgroundColour(wx.WHITE)
            self.SetSelectionTextColour(wx.BLACK)
            self.SetCaptionTextColour(wx.BLACK)

        if editable:
            for index in editable:
                self.MakeColumnEditable(index)

        self.register()

        if local:
            self.controller = local
        else:
            self.controller = PropertyGridController(controller, self)

        if not local:
            self.controller.do_layout()

    def register(self):
        """
        Register other stuff.

        :return:
        """
        # NOTE: Editor must be registered *before* adding a property that uses it.
        if not getattr(sys, '_PropGridEditorsRegistered', False):
            self.RegisterEditor(MultiButtonEditor)

            # ensure we only do it once
            sys._PropGridEditorsRegistered = True

    def add_category_property(self, name, status=None, enabled=True, *args, **kwargs):
        """
        Add category property.

        :param name:
        :param status: status bar string
        :param enabled:
        :param args:
        :param kwargs:
        :return:
        """

        return self.Append(propgrid.PropertyCategory(name))

    def add_file_property(self, name, key, value, status=None, enabled=True, *args, **kwargs):
        """
        Add file property.

        :param name:
        :param key:
        :param value:
        :param status: status bar string
        :param enabled:
        :param args:
        :param kwargs:
        :return:
        """
        item = propgrid.FileProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyHelpString(key, status)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_int_property(self, name, key, value, status=None, enabled=True, *args, **kwargs):
        """
        Add integer property.

        :param name:
        :param key:
        :param value:
        :param status: status bar string
        :param enabled:
        :param args:
        :param kwargs:
        :return:
        """
        item = propgrid.IntProperty(name, key, value=value)
        self.Append(item)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_string_property(self, name, key, value="", status=None, enabled=True, *args, **kwargs):
        """
        Add string property.

        :param name: label
        :param key: item key
        :param value:
        :param status: status bar string
        :param enabled: boolean value
        :param args:
        :param kwargs:
        :return:
        """
        if isinstance(value, list):
            item = propgrid.StringProperty(name, key)
        else:
            item = propgrid.StringProperty(name, key, value=value)

        self.Append(item)

        if isinstance(value, list):
            # Loop through the values and update.
            for index, cell in enumerate(value):
                if index == 0:
                    item.SetValue(cell)
                else:
                    self.set_text(key, index+1, cell)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_float_property(self, name, key, value, status=None, enabled=True, *args, **kwargs):
        """
        Add float property.

        :param name: title
        :param key:
        :param value:
        :param status: status bar string
        :param enabled:
        :param args:
        :param kwargs:
        :return:
        """
        item = propgrid.FloatProperty(name, key, value=value)
        self.Append(item)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_bool_property(self, name, key, value, status=None, enabled=True, **kwargs):
        """
        Add boolean property.

        :param name:
        :param key:
        :param value:
        :param status: status bar string
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.BoolProperty(name, key, value=value)
        self.Append(item)
        self.SetPropertyAttribute(key, "UseCheckbox", True)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_enum_property(self, name, key, value, status=None, enabled=True, **kwargs):
        """
        Add enumerator property.

        :param name:
        :param key:
        :param value:
        :param status: status bar string
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

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_array_string_property(self, name, key, value, status=None, enabled=True, *args, **kwargs):
        """
        Add array string property.

        :param name:
        :param key:
        :param value:
        :param status: status bar string
        :param enabled:
        :param args:
        :param kwargs:
        :return:
        """
        item = wx.propgrid.ArrayStringProperty(name, key, value=value)

        self.Append(item)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def add_multi_button(self, name, key, value, status=None, enabled=True, **kwargs):
        """
        Add multi-button.

        :param name:
        :param key:
        :param value:
        :param status: status bar string
        :param enabled:
        :param kwargs:
        :return:
        """
        buttons = propgrid.PGMultiButton(self, wx.Size(10, 10))
        buttons.Add('...')
        buttons.Add('A')

        # Finally, move button-subwindow to correct position and make sure
        # returned wxPGWindowList contains our custom button list.
        buttons.Finalize(self, wx.Point(1, 1))

        self.Append(buttons)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return buttons

    def add_multi_choice(self, name, key, value, status=None, enabled=True, **kwargs):
        """
        Add multi-choice values.

        :param name:
        :param key:
        :param value:
        :param status:
        :param enabled:
        :param kwargs:
        :return:
        """
        item = propgrid.MultiChoiceProperty(name,
                                            key,
                                            choices=value)

        self.Append(item)

        if status:
            self.SetPropertyHelpString(key, status)

        if enabled:
            self.EnableProperty(key)
        else:
            self.DisableProperty(key)

        return item

    def get_item(self, key, *args, **kwargs):
        """
        Return the PGProperty item.

        :param key: name of key
        :param args:
        :param kwargs:
        :return:
        """
        return self.GetPropertyByName(key)

    def get_cell(self, key, column, *args, **kwargs):
        """
        Return the cell inside the property item.

        :param key: name of property key
        :param column: column of item (0 index)
        :param args:
        :param kwargs:
        :return:
        """
        cell = self.get_item(key)

        return cell.GetCell(column)

    def set_text(self, key, column, value, fmt=None, *args, **kwargs):
        """
        Set the cell value for the property item.

        :param key: name of property key
        :param column: column of item (0 index)
        :param value: item name
        :param args:
        :param kwargs:
        :return:
        """

        cell = self.get_cell(key, column)

        if column == 1:
            item = self.get_item(key)

            if fmt:
                item.SetValue(fmt%(value))
            else:
                item.SetValue(str(value))
        else:
            if fmt:
                cell.SetText(fmt%(value))
            else:
                cell.SetText(str(value))

        if kwargs.get('fgcol'):
            cell.SetFgCol(kwargs.get('fgcol'))

        if kwargs.get('bgcol'):
            cell.SetBgCol(kwargs.get('bgcol'))

        if kwargs.get('bitmap'):
            cell.SetBitmap(kwargs.get('bitmap'))

        if kwargs.get('font'):
            cell.SetFont(kwargs.get('font'))

    def get_text(self, key, column, *args, **kwargs):
        """
        Return the cell value for the property item column.

        :param key: name of property key
        :param column: column of item (0 index)
        :param args:
        :param kwargs:
        """
        cell = self.get_cell(key, column)

        return cell.GetText()

    def get_data(self, key, column, *args, **kwargs):
        """
        Return the cell value for the property item column.

        :param key: name of property key
        :param column: column of item (0 index)
        :param args:
        :param kwargs:
        """
        cell = self.get_cell(key, column)

        return cell.GetData()

    def delete_item(self, key, *args, **kwargs):
        """
        Delete the PGProperty Item.

        :param key: name of key
        :param args:
        :param kwargs:
        """
        self.DeleteProperty(key)


class MultiButtonEditor(propgrid.PyTextCtrlEditor):
    """
    MultiButton Editor.

    """
    def __init__(self):
        """

        :return:
        """
        propgrid.PyTextCtrlEditor.__init__(self)

    def CreateControls(self, propGrid, property, pos, sz):
        """

        :param propGrid:
        :param property:
        :param pos:
        :param sz:
        :return:
        """
        # Create and populate buttons-subwindow
        buttons = propgrid.PGMultiButton(propGrid, sz)

        # Add two regular buttons
        buttons.AddButton("...")
        buttons.AddButton("A")
        # Add a bitmap button
        buttons.AddBitmapButton(wx.ArtProvider.GetBitmap(wx.ART_FOLDER))

        # Create the 'primary' editor control (textctrl in this case)
        wnd = self.CallSuperMethod("CreateControls",
                                   propGrid,
                                   property,
                                   pos,
                                   buttons.GetPrimarySize())

        # Finally, move buttons-subwindow to correct position and make sure
        # returned wxPGWindowList contains our custom button list.
        buttons.Finalize(propGrid, pos)

        # We must maintain a reference to any editor objects we created
        # ourselves. Otherwise they might be freed prematurely. Also,
        # we need it in OnEvent() below, because in Python we cannot "cast"
        # result of wxPropertyGrid.GetEditorControlSecondary() into
        # PGMultiButton instance.
        self.buttons = buttons

        return (wnd, buttons)

    def OnEvent(self, propGrid, prop, ctrl, event):
        """

        :param propGrid:
        :param prop:
        :param ctrl:
        :param event:
        :return:
        """
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:
            buttons = self.buttons
            evtId = event.GetId()

            if evtId == buttons.GetButtonId(0):
                # Do something when the first button is pressed
                wx.LogDebug("First button pressed")
                return False  # Return false since value did not change
            if evtId == buttons.GetButtonId(1):
                # Do something when the second button is pressed
                wx.MessageBox("Second button pressed")
                return False  # Return false since value did not change
            if evtId == buttons.GetButtonId(2):
                # Do something when the third button is pressed
                wx.MessageBox("Third button pressed")
                return False  # Return false since value did not change

        return self.CallSuperMethod("OnEvent", propGrid, prop, ctrl, event)
