import wx
import os

from .smart import SmartButton, SmartInputLayout

__author__ = 'Joeny'


class ButtonInputLayout(SmartInputLayout):
    """
    Button Input Layout

    """
    def __init__(self, parent, button=None, layout=None, *args, **kwargs):
        SmartInputLayout.__init__(self, parent=parent, layout=layout, *args, **kwargs)

        if button:
            self.button = button
        else:
            self.button = SmartButton(parent=parent)

        self.do_layout()

    @property
    def button(self):
        return self.combobox[self.INDEX_BUTTON]

    @button.setter
    def button(self, value):
        if value is None:
            return

        self.INDEX_BUTTON = self.next_id
        self.components.append(value)
