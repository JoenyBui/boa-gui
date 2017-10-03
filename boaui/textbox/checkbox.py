import wx
import os

from .smart import SmartCheckBox, SmartInputLayout

__author__ = 'Joeny'


class CheckboxInputLayout(SmartInputLayout):
    """
    Checkbox Input Layout

    """
    def __init__(self, parent, checkbox=None, layout=None, *args, **kwargs):
        label = None
        if checkbox:
            label = checkbox
        else:
            label = SmartCheckBox(parent)

        SmartInputLayout.__init__(self, parent, layout=layout, label=label, *args, **kwargs)

        self.do_layout()

    def set_value(self, value):
        # type: (object) -> object
        self.label.SetValue(bool(value))

    def get_value(self):
        return self.label.Value
