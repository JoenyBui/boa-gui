from unittest import TestCase

import wx

from boaui.units import KEY_IMPERIAL

from boaui.textbox.combobox import SmartComboBox
from boaui.textbox.intbox import IntInputLayout, IntSmartBox

__author__ = 'Joeny'


class TestIntInputLayout(TestCase):

    def setUp(self):
        app = wx.App()
        frame = wx.Frame(None, -1, 'simple')

        self.tl = IntInputLayout(frame,
                                 value=18,
                                 unit='in',
                                 unit_system=KEY_IMPERIAL,
                                 type='length',
                                 textbox=IntSmartBox(frame),
                                 postbox=SmartComboBox(frame))

    def test_get_value_length(self):
        self.assertNotEqual(self.tl.get_value('ft'), 1.5)
        self.assertEqual(self.tl.get_value('ft'), 1)

    def test_validator_zero(self):
        self.tl.textbox.set_value('00')

        self.assertEqual(self.tl.textbox.get_value(), 0)
