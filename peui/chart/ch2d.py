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


class Chart2d(wx.ScrolledWindow):
    """
    Chart 2D Panel

    """
    def __init__(self, parent, controller, local, figsize=None, dpi=None, facecolor=None, edgecolor=None,
                 linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None, *args, **kwargs):
        """
        Constructor.

        :param parent: parent view
        :param controller: parent controller
        :param local: local controller
        :param figsize: width, height tuples in inches
        :param dpi: Dots per inch
        :param facecolor: The figure patch facecolor; defaults to rc figure.facecolor
        :param edgecolor: The figure patch edge color; defaults to rc figure.edgecolor
        :param linewidth: The figure patch edge linewidth; the default linewidth of the frame
        :param frameon: If False, suppress drawing the figure frame
        :param subplotpars: A SubplotParams instance, defaults to rc
        :param tight_layout: If False use subplotpars; if True adjust subplot parameters using tight_layout() with
            default padding. When providing a dict containing the keys pad, w_pad, h_pad and rect, the default
            tight_layout() paddings will be overridden. Defaults to rc figure.autolayout.
        :param args:
            nrows - number of rows
            ncols - number of columns
            plot_number - plot number
        :param kwargs:

        :return:
        """
        wx.ScrolledWindow.__init__(self, parent=parent, size=wx.Size(200, 200), id=wx.ID_ANY, style=wx.VSCROLL)

        self.figure = plt.Figure(figsize=figsize, dpi=dpi, facecolor=facecolor, edgecolor=edgecolor,
                                 linewidth=linewidth, frameon=frameon, subplotpars=subplotpars,
                                 tight_layout=tight_layout)

        self.SetScrollRate(5, 5)

        if local:
            self.controller = local
            self.controller.view = self
        else:
            self.controller = Chart2dController(controller, self, **kwargs)

        self.axes = []
        # self.axes = self.figure.add_subplot(*args, **kwargs)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.toolbar = None

        # Add custom toolbar
        self.add_toolbar()

        # if not local:
        if hasattr(self.controller, 'do_layout'):
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

