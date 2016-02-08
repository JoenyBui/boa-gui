import random

import wx

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg

__author__ = 'jbui'


class Chart2d(wx.Panel):
    """
    Chart 2d Panel.
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.sp = wx.SplitterWindow(self)
        self.p1 = Graph2D(self.sp)
        self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.sp.SplitHorizontally(self.p1, self.p2, 470)

        # Custom Toolbar
        self.plotbut = wx.Button(self.p2, -1, "plot", size=(40, 20), pos=(160, 10))
        self.plotbut.Bind(wx.EVT_BUTTON,self.plot)

        self.sibut = wx.Button(self.p2,-1,"Zoom", size=(40, 20), pos=(60, 10))
        self.sibut.Bind(wx.EVT_BUTTON, self.zoom)

        self.hmbut = wx.Button(self.p2,-1,"Home", size=(40,20), pos=(110, 10))
        self.hmbut.Bind(wx.EVT_BUTTON, self.home)

        self.hibut = wx.Button(self.p2, -1, "Pan", size=(40, 20), pos=(10, 10))
        self.hibut.Bind(wx.EVT_BUTTON, self.pan)

        # self.SetSizer(self.sp)

    def zoom(self, event):
        self.p1.toolbar.zoom()

    def home(self, event):
        self.p1.toolbar.home()

    def pan(self, event):
        self.p1.toolbar.pan()

    def plot(self,event):
        self.p1.plot()


class Graph2D(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)

        self.toolbar = NavigationToolbar2WxAgg(self.canvas)
        self.toolbar.Hide()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.hold(False)
        ax.plot(data, '*-')
        self.canvas.draw()
