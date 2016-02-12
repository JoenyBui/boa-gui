import random

import numpy as np

import wx

# comment out the following to use wx rather than wxagg
import matplotlib

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

from matplotlib.backends.backend_wx import NavigationToolbar2Wx

import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg

__author__ = 'jbui'


class Chart2d(wx.Panel):
    """
    Chart 2d Panel.
    """
    def __init__(self, parent, *args, **kwargs):
        """

        :param parent:
        :return:
        """
        wx.Panel.__init__(self, parent)

        self.figure = plt.Figure()
        # self.axes = self.figure.add_subplot(111)
        self.axes = self.figure.add_subplot(*args, **kwargs)

        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)

        self.axes.plot(t, s)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.toolbar = None

        self.add_toolbar()

    def add_toolbar(self):
        """
        Add toolbar into the chart.
        :return:
        """
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()

        # By adding toolbar in sizer, we are able to put it at the bottom
        # of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)

        # update the axes menu on the toolbar
        self.toolbar.update()

