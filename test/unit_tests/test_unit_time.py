from unittest import TestCase
from peui.units import time

__author__ = 'jbui'


class TestTime(TestCase):

    def setUp(self):
        pass

    def test_ms(self):
        self.assertEqual(round(time.get_time_conversion_factor('ms', 's'), 5), 0.001)
