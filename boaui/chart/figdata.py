from matplotlib.pyplot import FuncFormatter

from boautil.threads import threaded
from boautil.general import check_empty

from .dlg import FigureSetting
from ..chart.ch2d import log_10_product

AXIS_X_MAIN = 1
AXIS_X_TWIN = 2
AXIS_Y_MAIN = 3
AXIS_Y_TWIN = 4


class Figure(object):
    """
    Figure Setup

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.plots = []

        # Row-Column set.
        self.plot_layout = kwargs.get('plot_layout', None)
        self.nrows = None
        self.ncols = None

    def refresh(self, settings):
        """
        Refresh plots.

        :return:
        """
        for plt in self.plots:
            plt.refresh(settings)

    def preset(self):
        """

        :return:
        """
        self.calculate_row_col()

    def calculate_row_col(self):
        """
        Calculate Row/Column.

        :return:
        """
        pl = self.get_plot_layout()

        nrows = 1
        ncols = 1
        for key, item in pl.items():
            nrows = max(nrows, item[0])
            ncols = max(ncols, item[1])

        self.nrows = nrows
        self.ncols = ncols

    def get_plot_layout(self):
        """
        Get plot layout.

        :return:
        """
        if self.plot_layout:
            return self.plot_layout
        else:
            plot_layout = {}
            for i in range(0, len(self.plots), 1):
                # (Row, Column)
                plot_layout[i] = (i + 1, 1)

            self.plot_layout = plot_layout

        return plot_layout

    def add_plot(self, *args, **kwargs):
        """
        Add plot

        :param args:
        :param kwargs:
        :return:
        """
        if kwargs.get('plot'):
            self.plots.append(kwargs.get('plot'))

        elif kwargs.get('data_set'):
            data_set = []
            for item in kwargs.get('data_set'):
                if isinstance(item, DataSet):
                    data_set.append(item)
                elif callable(item):
                    data_set.append(item)
                else:
                    data_set.append(
                        DataSet(
                            x=item[0],
                            y=item[1]
                        )
                    )
            self.plots.append(Plot(
                data_set=data_set
            ))

        else:
            for item in args:
                self.plots.append(item)

    def set_layout(self):
        """
        Set the layout.

        :return:
        """
        # Set the the grid.
        # gs = gridspec.GridSpec(self.nrows, self.ncols)
        pass

    def plot_data(self):
        """

        :return:
        """
        for index, data in enumerate(self.plots):
            pass


class Plot(object):
    """
    Plot setup

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
            :x_scale: {'linear', 'log', 'symlog', 'logit'}
            :y_scale: {'linear', 'log', 'symlog', 'logit'}
        """
        self.data_set = kwargs.get('data_set', [])
        self.axes = kwargs.get('axes')  # This is the main axis.
        self.twinx = kwargs.get('twinx', {})  # This is the twin x.

        self.settings = FigureSetting()
        self.settings.title = kwargs.get('title', 'Title')
        self.settings.x_label = kwargs.get('x_label', 'X Label')
        self.settings.x_scale = kwargs.get('x_scale', 'linear')
        self.settings.y_label = kwargs.get('y_label', 'Y Label')
        self.settings.y_scale = kwargs.get('y_scale', 'linear')
        self.settings.grid = kwargs.get('grid', True)
        self.settings.grid_minor = kwargs.get('grid_minor', False)
        self.settings.show_origin_axis = kwargs.get('show_origin_axis', True)
        self.settings.margin = 0.1
        self.settings.x_min = kwargs.get('x_min')
        self.settings.x_max = kwargs.get('x_max')
        self.settings.y_min = kwargs.get('y_min')
        self.settings.y_max = kwargs.get('y_max')

    def set_x_limits(self, min_x, max_x):
        """
        Set x limits range.

        :param min_x: minimum x value
        :param max_x: maximum x value
        """
        diff = (max_x - min_x) * self.settings.margin

        self.axes.set_xlim(
            left=min_x - diff / 2.0,
            right=max_x + diff / 2.0
        )

    def set_y_limits(self, min_y, max_y):
        """
        Set y limits range.

        :param min_y: minimum y value
        :param max_y: maximum y value
        """
        diff = (max_y - min_y) * self.settings.margin

        self.axes.set_ylim(
            bottom=min_y - diff / 2.0,
            top=max_y + diff / 2.0
        )

    def add_data_set(self, data_set):
        """

        :param data_set:
        :return:
        """
        if isinstance(data_set, DataSet):
            if data_set.twinx != 0:
                if data_set.twinx not in self.twinx:
                    if self.axes:
                        self.twinx[data_set.twinx] = self.axes.twinx()
                    else:
                        self.twinx[data_set.twinx] = None

            self.data_set.append(
                data_set
            )
        else:
            # Passed in (x, y) tuple.
            obj = DataSet()
            obj.x = data_set[0]
            obj.y = data_set[1]

            self.data_set.append(
                obj
            )

    @threaded
    def plot_data(self, *args, **kwargs):
        """

        :return:
        """
        for data in self.data_set:
            if callable(data):
                pass
            else:
                if data.twinx != 0:
                    data.plot(self.twinx[data.twinx])
                else:
                    data.plot(self.axes)

    def refresh(self, settings):
        """
        Refresh axes and it's data.

        :param settings: Figure Settings
        :return:
        """
        formatter = FuncFormatter(log_10_product)

        # Add title, x label, and y label.
        self.axes.set_title(self.settings.title)
        self.axes.set_xlabel(self.settings.x_label)
        self.axes.set_ylabel(self.settings.y_label)

        legend = {0: []}
        lines = []
        has_label = None

        color_set = settings.get('color_set')

        for index, data in enumerate(self.data_set):
            # If data_set is a function, we call it to operate on it.
            if callable(data):
                data = data()

            if data.twinx != 0:
                # data.plot(self.twinx[data.twinx], settings)
                # Plot alternative scale and return line.
                lines += data.plot(self.twinx[data.twinx], settings, color=color_set[index])

                if data.twinx not in legend:
                    legend[data.twinx] = []

                if data.label:
                    has_label = True
                    legend[data.twinx].append(data.label)
            else:
                # data.plot(self.axes, settings)
                # Plot data and return line.
                lines += data.plot(self.axes, settings, color=color_set[index])

                # Add data label.
                if data.label:
                    has_label = True
                    legend[0].append(data.label)

                    # if self.min_x > data.get_min_x():
                    #     self.min_x = data.get_min_x()
                    #
                    # if self.max_x < data.get_max_x():
                    #     self.max_x = data.get_max_x()
                    #
                    # if self.min_y > data.get_min_y():
                    #     self.min_y = data.get_min_y()
                    #
                    # if self.max_y < data.get_max_y():
                    #     self.max_y = data.get_max_y()

        # Add a legend if any dataset is labeled.
        if has_label:
            labels = [l.get_label() for l in lines]
            self.axes.legend(lines, labels, loc=0)

        # for key, ld in legend.items():
        #     if key != 0:
        #         if ld:
        #             self.twinx[key].legend()
        #     else:
        #         if ld:
        #             self.axes.legend()

        # for key, ld in legend.items():
        #     if key != 0:
        #         if ld:
        #             # self.twinx[key].legend(ld, loc=0)
        #             pass
        #     else:
        #         if ld:
        #             self.axes.legend(ld, loc=0)

        # TODO: Add autoscale
        self.axes.autoscale_view(False, True, True)

        if self.settings.x_min:
            self.axes.set_xlim(left=self.settings.x_min)

        if self.settings.x_max:
            self.axes.set_xlim(right=self.settings.x_max)

        if self.settings.y_min:
            self.axes.set_ylim(bottom=self.settings.y_min)

        if self.settings.y_max:
            self.axes.set_ylim(top=self.settings.y_max)

        # X Scale Log
        if self.settings.x_scale == 'log':
            # self.axes.set_xlim(left=self.min_x, right=self.max_x)
            self.axes.set_xscale(self.settings.x_scale, nonposx='clip')
            self.axes.xaxis.set_major_formatter(formatter)
            # self.axes.set_xlim(1e-5)
        else:
            self.axes.set_xscale(self.settings.x_scale)

        # Y Scale Log
        if self.settings.y_scale == 'log':
            # self.axes.set_ylim(bottom=self.min_y, top=self.max_y)
            self.axes.set_yscale(self.settings.y_scale, nonposy='clip')
            self.axes.yaxis.set_major_formatter(formatter)
        else:
            self.axes.set_yscale(self.settings.y_scale)

        # Grid
        if self.settings.grid:
            self.axes.grid(b=True, which='major')

        if self.settings.grid_minor:
            self.axes.grid(b=True, which='minor')

        if self.settings.show_origin_axis:
            self.axes.axhline(0, color='black', linewidth=1)
            self.axes.axvline(0, color='black', linewidth=1)


class DataSet(object):
    """
    Data Set

    """

    def __init__(self, *args, **kwargs):
        """
        Initialize

        :param args:
        :param kwargs:
        """
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')

        self.min_x = 0.0
        self.max_x = 0.0
        self.min_y = 0.0
        self.max_y = 0.0

        self.label = kwargs.get('label', None)
        self.twinx = kwargs.get('twinx', 0)

        if self.twinx == 0:
            self.axis_location = (AXIS_X_MAIN, AXIS_Y_MAIN)
        else:
            self.axis_location = (AXIS_X_TWIN, AXIS_Y_TWIN)

    @threaded
    def plot(self, axes, settings, *args, **kwargs):
        """
        Plot data.

        :param axes:
        :return:
        """
        # TODO: Threading is becoming an issue, where a race condition occured where legend is not plotting in time.
        return axes.plot(
            self.x,
            self.y,
            label=self.label,
            linewidth=settings.get('linewidth'),
            color=kwargs.get('color')
        )

    def get_min_x(self):
        return min(self.x)

    def get_max_x(self):
        return max(self.x)

    def get_min_y(self):
        return min(self.y)

    def get_max_y(self):
        return max(self.y)


# class ChartFigure(object):
#     """
#
#     """
#     def __init__(self, *args, **kwargs):
#         self.data = None
#
#         self.axes = []
#
#         self.title = None
#         self.xlabel = None
#         self.ylabel = None
#
#
# class ChartData(object):
#     """
#
#     """
#     def __init__(self, *args, **kwargs):
#         self.x = kwargs.get('x')
#         self.y = kwargs.get('y')
#
#         self.min_x = 0.0
#         self.max_x = 0.0
#         self.min_y = 0.0
#         self.max_y = 0.0
#
#         # Pointer
#         self.axes = kwargs.get('axes')
