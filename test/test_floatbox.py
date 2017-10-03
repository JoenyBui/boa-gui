from unittest import TestCase

import wx

from boaui.units import KEY_IMPERIAL, KEY_METRIC

from boaui.textbox.combobox import SmartComboBox
from boaui.textbox.floatbox import FloatInputLayout, FloatSmartBox
from boaui.textbox.intbox import IntInputLayout


class TestFloatInputLayout(TestCase):

    def setUp(self):
        app = wx.App()
        frame = wx.Frame(None, -1, 'simple')

        self.tl = FloatInputLayout(frame,
                                   value=18.0,
                                   unit='in',
                                   unit_system=KEY_IMPERIAL,
                                   type='length',
                                   textbox=FloatSmartBox(frame),
                                   postbox=SmartComboBox(frame))

    def test_get_value_length(self):
        self.assertEqual(self.tl.get_value('ft'), 1.5)
        self.assertEqual(self.tl.get_value('yd'), 0.5)
        self.assertEqual(self.tl.get_value('m'), 0.4572)
        self.assertEqual(self.tl.get_value('cm'), 45.72)
        self.assertEqual(self.tl.get_value('mm'), 457.2)
        self.assertAlmostEqual(self.tl.get_value('km'), 0.0004572, 6)


