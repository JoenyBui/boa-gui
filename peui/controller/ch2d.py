import os
import wx

import matplotlib.gridspec as gridspec

import numpy as np

import palettable

from ..chart.dlg import FigureSettingDialog, FigureSetting
from ..form.file import SaveXYDialog
from ..chart.dplot import Dplot, DplotCurve

from . import ChildController

__author__ = 'jbui'


class Chart2dController(ChildController):
    """
    Chart 2d controller.

    """
    def __init__(self, parent, view, figure_setting=None, *args, **kwargs):
        """
        Constructor

        :param parent: parent controller
        :param view: local view
        :param figure_setting:
        :return:
        """
        ChildController.__init__(self, parent, view, *args, **kwargs)

        self.color_set = palettable.cubehelix.classic_16.mpl_colors

        if figure_setting:
            self.figure_setting = figure_setting
        else:
            self.figure_setting = FigureSetting()

    def do_layout(self):
        """
        Draw the chart 2d data.

        :return:
        """
        self.view.axes = self.view.figure.add_subplot(111)

        # Grab project data.
        data = self.parent.project.data

        legend = []
        # Loop through the data set to have multiple plots.
        for i, (x, y) in enumerate(data):
            self.view.axes.plot(x, y)

            legend.append('Curve %d' % i)

        # Add legend
        self.view.axes.legend(legend)
        # self.view.axes.set_prop_cycle(self.color_set)

        # Call the binding for custom toolbar figure.
        self.bind_toolbar_figure()

        # Update figure text.
        self.update_text()

    def update_text(self):
        """

        :return:
        """
        self.view.axes.set_title(self.figure_setting.title)
        self.view.axes.set_ylabel(self.figure_setting.y_title)
        self.view.axes.set_xlabel(self.figure_setting.x_title)
        self.view.figure.canvas.draw()

    def bind_toolbar_figure(self):
        """

        :return:
        """
        tb = self.view.toolbar

        tb.Bind(wx.EVT_TOOL, self.on_custom_figure_setting, None, tb.ON_CUSTOM_FIGURE_SETTING)
        tb.Bind(wx.EVT_TOOL, self.on_click_save_xy_data, None, tb.ON_CUSTOM_DPLOT)

    def update_layout(self):
        """

        :return:
        """
        pass

    def refresh(self):
        """

        :return:
        """
        pass

    def sync_data(self):
        """

        :return:
        """
        pass

    def clear_control(self):
        """
        Clear the control.

        """
        pass

    def on_custom_figure_setting(self, event):
        """

        :param event:
        :return:
        """
        dlg = FigureSettingDialog(self.view, self, setting=self.figure_setting)

        if dlg.ShowModal() == wx.ID_OK:
            self.figure_setting = dlg.local.setting

            self.update_text()

    def on_click_save_xy_data(self, event):
        """
        On click save xy data.

        :param event:
        :return:
        """
        dlg = SaveXYDialog(self.view)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

            filename = dlg.GetFilename()

            file, ext = os.path.splitext(filename)

            if ext == '.csv':
                self.save_xy_data(path)
            elif ext == '.grf':
                self.save_dplot_data(path)

        dlg.Destroy()

    def get_data_block(self):
        """
        Get data in numpy matrix block.

        :return:
        """
        data = []

        for line in self.view.axes.lines:
            x = line.get_xdata()
            y = line.get_ydata()

            data.append(x)
            data.append(y)

        return np.array(data)

    def get_data_list(self):
        """
        Get the data in list of tuple.

        :return:
        """
        data = []

        for line in self.view.axes.lines:
            data.append((line.get_xdata(), line.get_ydata()))

        return data

    def save_xy_data(self, pathname):
        """
        Save data file to csv x, y.

        :param pathname: file path name
        :return:
        """
        data = self.get_data_block()

        # df = pd.DataFrame(np.array(data).transpose())
        # df.to_csv(pathname)
        try:
            np.savetxt(pathname, data.transpose(), delimiter=',')
        except TypeError as e:
            print(e)

            wx.MessageBox('TypeError: Data is not aligned and cannot be saved as csv.')

    def save_dplot_data(self, pathname):
        """
        Save dplot data

        :param pathname:
        :return:
        """

        try:
            dp = Dplot()

            data = self.get_data_list()

            # Title
            dp.title_1 = self.view.axes.get_title()

            # X-Title
            x_axis = self.view.axes.get_xaxis()
            dp.x_axis = x_axis.get_label().get_text()

            # Y-Title
            y_axis = self.view.axes.get_yaxis()
            dp.y_axis = y_axis.get_label().get_text()

            xscale = x_axis.get_scale()
            yscale = y_axis.get_scale()

            if xscale == 'linear' and yscale == 'linear':
                dp.scale_mode = dp.scaling_list['A'][1]
            elif xscale == 'linear' and yscale == 'log':
                dp.scale_mode = dp.scaling_list['D'][1]
            elif xscale == 'log' and yscale == 'linear':
                dp.scale_mode = dp.scaling_list['B'][1]
            elif xscale == 'log' and yscale == 'log':
                dp.scale_mode = dp.scaling_list['E'][1]

            for x, y in data:
                dp.add_curve(
                    DplotCurve(
                        list(x), list(y)
                    )
                )

            # Draw Legend
            legend = self.view.axes.get_legend()

            if legend:
                texts = legend.get_texts()
                for index in range(0, len(texts)):
                    text = texts[index]

                    dp.data[index].legend_title = text.get_text()

            dp.write_dplot(pathname)

        except IOError as e:

            print(str(e))

    def plot(self,
             index,
             xdata,
             ydata,
             linewidth=None,
             linestyle=None,
             color=None,
             marker=None,
             markersize=None,
             markeredgewidth=None,
             markeredgecolor=None,
             markerfacecolor=None,
             markerfacecoloralt='none',
             fillstyle=None,
             antialiased=None,
             dash_capstyle=None,
             solid_capstyle=None,
             dash_joinstyle=None,
             solid_joinstyle=None,
             pickradius=5,
             drawstyle=None,
             markevery=None,):
        """
        =================== =======================================================================================================================
        Property            Description
        =================== =======================================================================================================================
        agg_filter	        unknown
        alpha	            float (0.0 transparent through 1.0 opaque)
        animated	        [True | False]
        antialiased or aa	[True | False]
        axes	            an Axes instance
        clip_box	        a matplotlib.transforms.Bbox instance
        clip_on	            [True | False]
        clip_path	        [ (Path, Transform) | Patch | None ]
        color or c	        any matplotlib color
        contains	        a callable function
        dash_capstyle	    ['butt' | 'round' | 'projecting']
        dash_joinstyle	    ['miter' | 'round' | 'bevel']
        dashes	            sequence of on/off ink in points
        drawstyle	        ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post']
        figure	            a matplotlib.figure.Figure instance
        fillstyle	        ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none']
        gid	                an id string
        label	            string or anything printable with '%s' conversion.
        linestyle or ls	    ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
        linewidth or lw	    float value in points
        marker	            A valid marker style
        markeredgecolor     any matplotlib color
        markeredgewidth     float value in points
        markerfacecolor     any matplotlib color
        markerfacecoloralt  any matplotlib color
        markersize          float
        markevery	        [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
        path_effects	    unknown
        picker	            float distance in points or callable pick function fn(artist, event)
        pickradius	        float distance in points
        rasterized	        [True | False | None]
        sketch_params	    unknown
        snap	unknown
        solid_capstyle	    ['butt' | 'round' | 'projecting']
        solid_joinstyle	    ['miter' | 'round' | 'bevel']
        transform	        a matplotlib.transforms.Transform instance
        url	                a url string
        visible	            [True | False]
        xdata	            1D array
        ydata	            1D array
        zorder	            any number
        =================== =======================================================================================================================
        """

        pass


class MultiChart2dController(Chart2dController):
    """
    Multi Graph Chart 2D

    """
    def __init__(self, parent, view, data, figure_setting=None, *args, **kwargs):
        """
        Constructor

        :param parent: parent controller
        :param view: local view
        :param figure_setting:
        :return:
        """
        Chart2dController.__init__(self, parent, view, figure_setting=figure_setting, *args, **kwargs)

        self.data = data

    def do_layout(self):
        """
        Draw the chart 2d data.

        :return:
        """
        # Loop through the data set to have multiple plots.
        self.view.axes = []

        nrows = len(self.data)
        ncols = 1
        gs = gridspec.GridSpec(nrows, ncols)

        for i, (x, y) in enumerate(self.data):
            plot_number = i+1

            axes = self.view.figure.add_subplot(gs[i, :])

            axes.plot(x, y)

            legend = ['Curve %d' % (plot_number,)]

            # Add legend
            axes.legend(legend)
            axes.set_title('title')
            axes.set_xlabel('x label')
            axes.set_ylabel('y label')

            self.view.axes.append(axes)

        # Call the binding for custom toolbar figure.
        self.bind_toolbar_figure()

        # Make the grid nice.
        self.view.figure.tight_layout()
        self.view.figure.subplots_adjust(left=0.125, right=0.9)

        # Update figure text.
        # self.update_text()
