from unittest import TestCase

import wx

from peui.units import KEY_IMPERIAL

from peui.textbox.combobox import SmartComboBox
from peui.textbox.intbox import IntInputLayout, IntSmartBox

__author__ = 'jbui'


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
