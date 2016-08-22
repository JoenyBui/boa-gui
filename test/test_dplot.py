import unittest

import os

from peui.chart.dplot import Dplot


__author__ = 'jbui'


class TestDPLOT(unittest.TestCase):

    def setUp(self):
        self.test_folder = os.path.dirname(__file__)
        self.project_folder = os.path.split(self.test_folder)[0]

        self.dp = Dplot()

        self.setup_file()

        self.dp.title = 'Deflection vs. Time'

    def setup_file(self):
        pass

    def test_write(self):
        file_path = os.path.join(self.test_folder, 'data', 'test.grf')

        self.dp.write_dplot(file_path)

        self.assertTrue(os.path.isfile(file_path))

