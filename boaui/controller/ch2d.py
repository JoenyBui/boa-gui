import os
import wx

import matplotlib.gridspec as gridspec

import numpy as np

import palettable

from boautil.threads import threaded
from boautil.general import check_empty

from ..chart.dlg import FigureSettingDialog, FigureSetting
from ..form.file import SaveXYDialog, PlotChooseAxisDialog
from ..chart.dplot import Dplot, DplotCurve

from . import TabPageController
from ..config import STATE_CLOSE_PROJECT

AXIS_X_MAIN = 1
AXIS_X_TWIN = 2
AXIS_Y_MAIN = 3
AXIS_Y_TWIN = 4

__author__ = 'Joeny'


class Chart2dController(TabPageController):
    """
    Chart 2d controller.

    """
    def __init__(self, parent, view, *args, **kwargs):
        """
        Constructor

        :param parent: parent controller
        :param view: local view
        :param *args:
        :param **kwargs:
        :return:
        """
        TabPageController.__init__(self, parent, view, *args, **kwargs)

        self.data = None
        self.data_loc = []

        self.twinx = []

        self.color_set = palettable.colorbrewer.qualitative.Dark2_7.mpl_colors
        self.figure_settings = []

        self.show_origin_axis = kwargs.get('show_origin_axis', True)
        self.margin = 0.1

    def set_data_axis(self):
        """
        Set original data axis.

        :return:
        """
        if self.data:

            # Loop through data.
            for i1, data in enumerate(self.data):
                data_axis = []

                for i2, (x, y) in enumerate(data):
                    data_axis.append((AXIS_X_MAIN, AXIS_Y_MAIN))

                self.data_loc.append(data_axis)

    def do_layout(self):
        """
        Draw the chart 2d data.

        :return:
        """
        # Set the data axis.
        self.set_data_axis()

        self.view.axes = []

        self.view.axes.append(self.view.figure.add_subplot(111))

        # Grab project data.
        data = self.parent.project.data

        legend = []
        # Loop through the data set to have multiple plots.
        for i, (x, y) in enumerate(data):
            self.view.axes[0].plot(x, y)

            legend.append('Curve %d' % i)

        self.view.axes[0].set_title('Title')
        self.view.axes[0].set_ylabel('Y Title')
        self.view.axes[0].set_xlabel('X Title')

        # Add legend
        self.view.axes[0].legend(legend)
        # self.view.axes.set_prop_cycle(self.color_set)

        # Call the binding for custom toolbar figure.
        self.bind_toolbar_figure()

        # Update figure text.
        # self.update_text()

    def update_figure_setting(self, settings):
        """
        Update figure setting text

        :param settings: update the title axes
        :return:
        """

        for index, setting in enumerate(settings):
            self.view.axes[index].set_title(setting.title)
            self.view.axes[index].set_ylabel(setting.y_title)
            self.view.axes[index].set_xlabel(setting.x_title)

            self.view.axes[index].set_xlim(left=setting.x_min, right=setting.x_max)
            self.view.axes[index].set_ylim(bottom=setting.y_min, top=setting.y_max)

        self.view.figure.canvas.draw()

    def bind_toolbar_figure(self):
        """
        Bind Toolbar Figure

        :return:
        """
        tb = self.view.toolbar

        tb.Bind(wx.EVT_TOOL, self.on_custom_figure_setting, None, tb.ON_CUSTOM_FIGURE_SETTING)
        tb.Bind(wx.EVT_TOOL, self.on_click_save_xy_data, None, tb.ON_CUSTOM_DPLOT)

    def update_layout(self, state):
        """
        Update the layout given the state.

        :param state:
        :return:
        """
        if self.state == state:
            self.clear_control()

            self.view.figure.canvas.draw()

        elif state < self.state:
            self.delete_control()

        else:
            TabPageController.update_layout(self, state)

    def refresh(self):
        """
        Refresh

        :return:
        """
        pass

    def sync_data(self):
        """
        Sync data

        :return:
        """
        pass

    def clear_control(self):
        """
        Clear the axis control.

        """
        for axes in self.view.axes:
            axes.cla()

    # def delete_control(self):
    #     """
    #     Delete Control
    #
    #     """
    #
    #     # Remove from the dictionary
    #     if self.parent.windows:
    #         ctrl, idx = self.parent.notebook.FindTab(self.view)
    #
    #         self.parent.delete_page(idx)
    #
    #         del self.parent.windows[self.key]

    def get_figure_settings(self):
        """
        Get the figure setting array for each plot.

        :return:
        """
        fs_array = []

        for axes in self.view.axes:
            fs = FigureSetting()

            fs.title = axes.get_title()
            fs.x_title = axes.get_xlabel()
            fs.y_title = axes.get_ylabel()

            xlim = axes.get_xlim()
            ylim = axes.get_ylim()

            fs.x_min = xlim[0]
            fs.x_max = xlim[1]
            fs.y_min = ylim[0]
            fs.y_max = ylim[1]

            fs_array.append(fs)

        return fs_array

    def on_custom_figure_setting(self, event):
        """

        :param event:
        :return:
        """
        dlg = FigureSettingDialog(self.view, self, setting=self.get_figure_settings())

        if dlg.ShowModal() == wx.ID_OK:
            self.update_figure_setting(dlg.local.settings)

    def update_figure_settings(self):
        """
        Update figure settings

        :param fs:
        :return:
        """
        self.update_figure_setting(self.figure_settings)

    def on_click_save_xy_data(self, event):
        """
        On click save xy data.

        :param event:
        :return:
        """
        if len(self.view.axes) == 1:
            dlg = SaveXYDialog(self.view)
        else:
            dlg = PlotChooseAxisDialog(self.view)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

            axis_index = dlg.get_axis_index()
            filename = dlg.GetFilename()

            file, ext = os.path.splitext(filename)

            if ext == '.csv':
                self.save_xy_data(path, axis_index)
            elif ext == '.grf':
                self.save_dplot_data(path, axis_index)

        dlg.Destroy()

    def get_data_block(self, index):
        """
        Get data in numpy matrix block.

        :param index:
        :return:
        """
        data = []

        for line in self.view.axes[index].lines:
            x = line.get_xdata()
            y = line.get_ydata()

            data.append(x)
            data.append(y)

        return np.array(data)

    def get_data_list(self, axis_index):
        """
        Get the data in list of tuple.

        :param axis_index:
        :return:
        """
        data = []

        # for axes in self.view.axes[axis_index]:
        axes = self.view.axes[axis_index]

        if self.show_origin_axis:
            for line in axes.lines[:-2]:
                data.append((line.get_xdata(), line.get_ydata()))

        else:
            for line in axes.lines:
                data.append((line.get_xdata(), line.get_ydata()))

        return data

    def save_xy_data(self, pathname, axis_index):
        """
        Save data file to csv x, y.

        :param pathname: file path name
        :param axis_index:
        :return:
        """
        data = self.get_data_block(axis_index)

        try:
            np.savetxt(pathname, data.transpose(), delimiter=',')
        except TypeError as e:
            print(e)

            wx.MessageBox('TypeError: Data is not aligned and cannot be saved as csv.')

    def save_dplot_data(self, pathname, axis_index):
        """
        Save dplot data

        :param pathname:
        :param axis_index:
        :return:
        """

        try:
            dp = Dplot()

            data = self.get_data_list(axis_index)

            # Title
            dp.title_1 = self.view.axes[axis_index].get_title()

            # X-Title
            x_axis = self.view.axes[axis_index].get_xaxis()
            dp.x_axis = x_axis.get_label().get_text()

            # Y-Title
            y_axis = self.view.axes[axis_index].get_yaxis()
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
            legend = self.view.axes[axis_index].get_legend()

            if legend:
                texts = legend.get_texts()
                for index in range(0, len(texts)):
                    text = texts[index]

                    dp.data[index].legend_title = text.get_text()

            dp.write_dplot(pathname)

        except IOError as e:

            print(str(e))

    def add_figure_setting(self, *args, **kwargs):
        """
        Add figure setting.

        :param args: arguments
        :param kwargs: keyword arguments
        """
        setting = FigureSetting(*args, **kwargs)
        self.figure_settings.append(setting)

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

    # @threaded
    def plot_data(self):
        """
        Plot data.

        :return:
        """
        if self.data:
            for i1, data in enumerate(self.data):
                if self.data_loc != []:
                    data_loc = self.data_loc[i1]
                else:
                    data_loc = None

                # Axes
                if len(self.view.axes) > i1:

                    self.plot_figure(self.view.axes[i1],
                                     data,
                                     linewidth=self.figure_settings[i1].linewidth,
                                     data_loc=data_loc)

                    # Set the legend.
                    if self.figure_settings[i1].legend:
                        # if isinstance(self.figure_settings[i1].legend, list):

                        for i2, legend in enumerate(self.figure_settings[i1].legend):
                            if i2 == 0:
                                self.view.axes[i1].legend(legend)
                            else:
                                if self.twinx:
                                    if self.twinx[i1]:
                                        self.twinx[i1][i2].legend(legend, loc='upper center')
                        # else:
                        #     self.view.axes[i1].legend(self.figure_settings[i1].legend)

                    # if self.figure_settings[i1].legend:
                    #     self.view.axes[i1].legend(self.figure_settings[i1].legend)
                    #
                    # if i1 == 1:
                    #     #TODO: Need to completely redo the way we plot.
                    #     self.twinx[1][1].legend(['Dynamic Axial Load'], loc='upper center')

                    self.plot_axis(self.view.axes[i1])
                else:
                    print('No axes in chart2d.')


            self.view.figure.canvas.draw()

    def plot_figure(self, ax1, data, *args, **kwargs):
        """
        Plot figure w/ data.

        :param ax1:
        :param data:
        :param *args:
        :param **kwargs:
        :return:
        """
        # Minimum and maximum x, y limits.
        min_x = max_x = min_y = max_y = 0.0

        # Use twin axis.
        use_twinx = False
        min_x_twin = max_x_twin = min_y_twin = max_y_twin = 0.0

        # Grab line width.
        linewidth = kwargs.get('linewidth', 1.0)

        data_loc = kwargs.get('data_loc')

        # Loop through the data.
        if data:
            for i2, (x, y) in enumerate(data):
                # Colorset
                colorset = self.color_set[i2]

                if data_loc is None or data_loc[i2][0] == AXIS_X_MAIN:
                    # Set the main axis.
                    ax1.plot(x, y, linewidth=linewidth, color=colorset)

                    if check_empty(x):
                        if min_x > min(x):
                            min_x = min(x)

                        if max_x < max(x):
                            max_x = max(x)

                    if check_empty(y):
                        if min_y > min(y):
                            min_y = min(y)

                        if max_y < max(y):
                            max_y = max(y)
                else:
                    # Run through the twinx axis.
                    use_twinx = True

                    ax2 = self.twinx[1][1]

                    ax2.plot(x, y, linewidth=linewidth, color=colorset)

                    if check_empty(x):
                        if min_x_twin > min(x):
                            min_x_twin = min(x)

                        if max_x_twin < max(x):
                            max_x_twin = max(x)

                    if check_empty(y):
                        if min_y_twin > min(y):
                            min_y_twin = min(y)

                        if max_y_twin < max(y):
                            max_y_twin = max(y)

        # Set the minimum and maximum for main axis.
        if use_twinx:
            self.set_xlimits(ax1, min_x, max_x)

            # Remove teh align axis.

            # Set the minimum and maximum for twin axis.
            #TODO: This is bad.  Need to remove it and create a class for ChartFigure and ChartData.

            if False:

                ax2 = self.twinx[1][1]

                # self.set_xlimits(ax2, min_x_twin, max_x_twin)
                # self.set_ylimits(ax2, min_y_twin, max_y_twin)
                self.align_both_set(ax1, ax2, max_y, min_y, min_y_twin, max_y_twin)

                # Align the two axes at 0.0
                self.align_yaxis(ax1, 0, ax2, 0)
            else:
                self.set_ylimits(ax2, min_y_twin, max_y_twin)
        else:
            self.set_xlimits(ax1, min_x, max_x)
            self.set_ylimits(ax1, min_y, max_y)

    def align_both_set(self, ax1, ax2, max_y1, min_y1, max_y2, min_y2):
        """
        Align both set of data with each other.

        :param ax1: axes 1
        :param ax2: axes 2
        :param max_y1:
        :param min_y1:
        :param max_y2:
        :param min_y2:
        :return:
        """
        total_y1 = abs(max_y1)  + abs(min_y1)
        total_y2 = abs(max_y2) + abs(min_y2)

        if total_y1 == 0 or total_y2 == 0:
            return

        top1 = abs(max_y1)/total_y1
        bot1 = abs(min_y1)/total_y1

        top2 = abs(max_y2)/total_y2
        bot2 = abs(min_y2)/total_y2

        adj_top = max(top1, top2)
        adj_bot = max(bot1, bot2)

        # Left
        _bot1 = (-1.0*adj_bot)*total_y1
        _top1 = (adj_top)*total_y1
        ax1.set_ylim(bottom=_bot1, top=_top1)

        #Right
        _bot2 = (-1.0*adj_bot)*total_y2
        _top2 = (adj_top)*total_y2
        ax2.set_ylim(bottom=_bot2, top=_top2)

    def align_yaxis(self, ax1, v1, ax2, v2):
        """
        Adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1

        :param ax1:
        :param v1:
        :param ax2:
        :param v2:
        :return:
        """
        _, y1 = ax1.transData.transform((0, v1))
        _, y2 = ax2.transData.transform((0, v2))
        inv = ax2.transData.inverted()
        _, dy = inv.transform((0, 0)) - inv.transform((0, y1 - y2))
        miny, maxy = ax2.get_ylim()
        ax2.set_ylim(miny + dy, maxy + dy)

    @threaded
    def update_data(self):
        """
        Update data

        """

        if self.data:

            # Clear Control
            for i1, data in enumerate(self.data):
                axes = self.view.axes[i1]

                # Initialize min/max
                min_x = max_x = min_y = max_y = 0.0

                lines = axes.get_lines()
                for i2, (x, y) in enumerate(data):

                    line = lines[i2]
                    line.set_data(x, y)

                    if check_empty(x):
                        if min_x > min(x):
                            min_x = min(x)

                        if max_x < max(x):
                            max_x = max(x)

                    if check_empty(y):
                        if min_y > min(y):
                            min_y = min(y)

                        if max_y < max(y):
                            max_y = max(y)

                self.set_xlimits(axes, min_x, max_x)
                self.set_ylimits(axes, min_y, max_y)

                if self.figure_settings[i1].legend:
                    self.view.axes[i1].legend(self.figure_settings[i1].legend)

            self.view.figure.canvas.draw()

    def plot_axis(self, axes):
        """
        Plot horizontal and vertical axis.

        :param axes: Axes2d
        """
        # axes.spines['right'].set_position('zero')
        # axes.spines['right'].set_smart_bounds(True)

        # axes.spines['left'].set_position('center')
        # axes.spines['right'].set_color('none')
        # axes.spines['bottom'].set_position('center')
        # axes.spines['top'].set_position('zero')
        # axes.spines['top'].set_smart_bounds(True)

        # axes.spines['left'].set_smart_bounds(True)
        # axes.spines['bottom'].set_smart_bounds(True)
        # axes.xaxis.set_ticks_position('bottom')
        # axes.yaxis.set_ticks_position('left')
        # pass
        if self.show_origin_axis:
            axes.axhline(0, color='black', linewidth=1)
            axes.axvline(0, color='black', linewidth=1)

    def set_xlimits(self, axes, min_x, max_x):
        """
        Set x limits range.

        :param axes: Axes2d
        :param min_x: minimum x value
        :param max_x: maximum x value
        """
        diff = (max_x - min_x)*self.margin

        axes.set_xlim(left=min_x - diff/2.0, right=max_x + diff/2.0)

    def set_ylimits(self, axes, min_y, max_y):
        """
        Set y limits range.

        :param axes: Axes2d
        :param min_y: minimum y value
        :param max_y: maximum y value
        """
        diff = (max_y - min_y)*self.margin

        axes.set_ylim(bottom=min_y - diff/2.0, top=max_y + diff/2.0)


class MultiChart2dController(Chart2dController):
    """
    Multi Graph Chart 2D

    """
    def __init__(self, parent, view, data=None, figure_setting=None, *args, **kwargs):
        """
        Constructor

        :param parent: parent controller
        :param view: local view
        :param data:
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
        self.set_data_axis()

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
