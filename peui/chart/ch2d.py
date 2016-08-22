import random

import numpy as np
import pandas as pd

import wx

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg

from ..controller.ch2d import Chart2dController
from .toolbar import MatplotlibCustomToolbar

__author__ = 'jbui'


class Chart2d(wx.Panel):
    """
    Chart 2d Panel.
    """
    def __init__(self, parent, controller, local, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param controller: parent controller
        :param local: local controller
        :param args:
        :param kwargs:
        :return:
        """
        wx.Panel.__init__(self, parent)

        if local:
            self.controller = local
        else:
            self.controller = Chart2dController(controller, self)

        self.figure = plt.Figure()
        self.axes = self.figure.add_subplot(*args, **kwargs)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.toolbar = None

        self.add_toolbar()

        if not local:
            self.controller.do_layout()

    def plot(self, xs, ys, *args, **kwargs):
        """
        Plot x, y data.

        :param xs:
        :param ys:
        :param args:
        :param kwargs:
        :return:
        """
        self.axes.plot(xs, ys, *args, **kwargs)

    def add_toolbar(self):
        """
        Add toolbar into the chart.

        :return:
        """
        self.toolbar = MatplotlibCustomToolbar(self.canvas, self)
        self.toolbar.Realize()

        # By adding toolbar in sizer, we are able to put it at the bottom
        # of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)

        # update the axes menu on the toolbar
        self.toolbar.update()

