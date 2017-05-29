import wx

from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.backends.backend_wx import _load_bitmap

from ..config import ICONS
from ..util import load_bitmap

__author__ = 'jbui'


class MatplotlibCustomToolbar(NavigationToolbar):
    """
    Matplotlib Custom Toolbar

    """
    ON_CUSTOM_LEFT = wx.NewId()
    ON_CUSTOM_RIGHT = wx.NewId()
    ON_CUSTOM_UP = wx.NewId()
    ON_CUSTOM_DOWN = wx.NewId()
    ON_CUSTOM_FIGURE_SETTING = wx.NewId()
    ON_CUSTOM_DPLOT = wx.NewId()

    def __init__(self, canvas, chart, pan_tool=True, pan_percentage=0.5):
        """
        Constructor

        :param canvas:
        :param chart:
        :param pan_tool:
        :param pan_percentage:
        :return:
        """
        NavigationToolbar.__init__(self, canvas)

        self.chart = chart

        self.pan_percentage = pan_percentage

        # add new toolbar buttons
        self.AddSimpleTool(self.ON_CUSTOM_DPLOT,
                           _load_bitmap('qt4_editor_options.png'),
                           'Save XY',
                           'Save XY to csv.')

        self.AddSimpleTool(self.ON_CUSTOM_FIGURE_SETTING,
                           load_bitmap('hand.xpm'),
                           'Open figure setting',
                           'Open figure setting.')
        # wx.EVT_TOOL(self, self.ON_CUSTOM_FIGURE_SETTING, self._on_custom_figure_setting)


        # self.AddSimpleTool(self.ON_CUSTOM_DPLOT,
        #                    wx.Bitmap(ICONS['dplot']),
        #                    'DPLOT',
        #                    'DPLOT')

        self.AddSeparator()
        self.AddStretchableSpace()

        if pan_tool:
            self.AddSimpleTool(self.ON_CUSTOM_LEFT, load_bitmap('stock_left.xpm'),
                               'Pan to the left', 'Pan graph to the left')
            self.Bind(wx.EVT_TOOL, self._on_custom_pan_left, None, self.ON_CUSTOM_LEFT)

            self.AddSimpleTool(self.ON_CUSTOM_RIGHT, load_bitmap('stock_right.xpm'),
                               'Pan to the right', 'Pan graph to the right')
            self.Bind(wx.EVT_TOOL, self._on_custom_pan_right, None, self.ON_CUSTOM_RIGHT)

            self.AddSimpleTool(self.ON_CUSTOM_UP, load_bitmap('stock_up.xpm'),
                               'Pan to the top', 'Pan graph to the top')
            self.Bind(wx.EVT_TOOL, self._on_custom_pan_up, None, self.ON_CUSTOM_UP)

            self.AddSimpleTool(self.ON_CUSTOM_DOWN, load_bitmap('stock_down.xpm'),
                               'Pan to the bottom', 'Pan graph to the bottom')
            self.Bind(wx.EVT_TOOL, self._on_custom_pan_down, None, self.ON_CUSTOM_DOWN)

    def _on_custom_pan_left(self, evt):
        """
        Pan the graph to the left.

        :param evt:
        :return:
        """
        for axes in self.canvas.figure.axes:
            x1, x2 = axes.get_xlim()

            ONE_SCREEN = x2 - x1

            axes.set_xlim(x1 - self.pan_percentage*ONE_SCREEN,
                          x2 - self.pan_percentage*ONE_SCREEN)

        self.canvas.draw()

    def _on_custom_pan_right(self, evt):
        """
        Pan the graph to the right.

        :param evt:
        :return:
        """
        for axes in self.canvas.figure.axes:
            x1, x2 = axes.get_xlim()

            ONE_SCREEN = x2 - x1

            axes.set_xlim(x1 + self.pan_percentage*ONE_SCREEN,
                          x2 + self.pan_percentage*ONE_SCREEN)
        self.canvas.draw()

    def _on_custom_pan_up(self, evt):
        """
        Pan the graph to the up.

        :param evt:
        :return:
        """
        for axes in self.canvas.figure.axes:
            y1, y2 = axes.get_ylim()

            ONE_SCREEN = y2 - y1

            axes.set_ylim(y1 + self.pan_percentage*ONE_SCREEN,
                          y2 + self.pan_percentage*ONE_SCREEN)
        self.canvas.draw()

    def _on_custom_pan_down(self, evt):
        """
        Pan the graph to the down.

        :param evt:
        :return:
        """
        for axes in self.canvas.figure.axes:
            y1, y2 = axes.get_ylim()

            ONE_SCREEN = y2 - y1

            axes.set_ylim(y1 - self.pan_percentage*ONE_SCREEN,
                          y2 - self.pan_percentage*ONE_SCREEN)
        self.canvas.draw()

    def update(self):
        """
        Update toolbar

        :return:
        """
        NavigationToolbar.update(self)
