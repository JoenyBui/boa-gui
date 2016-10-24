import os

import numpy as np

__author__ = 'jbui'


class Dplot(object):
    """
    DPlot Data

    """
    def __init__(self, *args, **kwargs):
        """
        Constructor

        :param args:
        :param kwargs:
        :return:
        """
        self.heading = 'DPLOT/W v1.2'

        self.title_1 = kwargs.get('title_1', '')
        self.title_2 = kwargs.get('title_2', '')
        self.title_3 = kwargs.get('title_3', '')
        self.x_axis = kwargs.get('x_axis', '')
        self.y_axis = kwargs.get('y_axis', '')

        self.legend_title = kwargs.get('legend_title', '')
        self.legend_coordinate = kwargs.get('legend_coordinate', (0.0, 0.0))
        self.legend_max_num_row = kwargs.get('legend_max_num_row', 20)
        self.legend_frame = kwargs.get('legend_frame', True)
        self.legend_line_width = kwargs.get('legend_line_width', 1.5)
        self.legend_transparent = kwargs.get('legend_transparent', False)

        self.column_heading = None

        self.dense_grid = kwargs.get('dense_grid', None)
        self.grid_type = kwargs.get('grid_type', 1)
        self.grid_list = {
            0: 'Axes Only',
            1: 'Grid Lines',
            2: 'Box Around Curves'
        }

        self.data = []
        self.data_attr = []

        self.line_type_list = {
            0: 'None',
            1: 'Full',
            2: 'Long-Dash',
            3: 'Short-Dash',
            4: 'Alternate-1-Dash',
            5: 'Alternate-2-Dash',
            6: 'Alternate-3-Dash'
        }

        self.scale_mode = 1

        self.scaling_list = dict(
            A=('Linear X - Linear Y', 1),
            B=('Linear X - Logarithmic Y', 2),
            C=('Linear X - Probability Y', 1),
            D=('Logarithmic X - Linear Y', 3),
            E=('Logarithmic X - Logarithmic Y', 4),
            F=('Logarithmic X - Probability Y', 1),
            G=('Probability X - Linear Y', 11),
            H=('Probability X - Logarithmic Y', 12),
            I=('Probability X - Probability Y',),
            J=('Tripartite Grid', 5),
            K=('Grain Size Distribution',),
            L=('Polar Coordinates', 8),
            M=('Bar Chart', 9)
        )

        self.symbol_type_list = dict(A=(0, 256),
                                     B=(1, 257),
                                     C=(2, 258),
                                     D=(3, 259),
                                     E=(4, 260),
                                     F=(5, 261),
                                     G=(6, 262),
                                     H=(7, 263),
                                     I=(8, 264),
                                     J=(9, 265),
                                     K=(10, 267),
                                     L=(11, 268),
                                     M=(12, 269))

        self.font_size = dict(
            numbers=10,
            first_title=12,
            second_title=12,
            x_axis=12,
            y_axis=12,
            legend=10,
            note=10
        )

    def add_curve(self, data):
        """
        Add curve data

        :param data:
        :return:
        """
        self.data.append(data)

    def write_dplot(self, filepath):
        """
        Write DPLOT file.

        :param filepath:
        :return:
        """
        with open(filepath, 'w') as data_file:
            def write(line):
                data_file.write(line + '\n')

            write(self.heading)

            write('data')

            # Number of Curves
            write('%d' % len(self.data))

            for curve in self.data:
                curve.write_data(write)

            # Write Title 1 and 2, 'x' and 'y' axis
            write(self.title_1)
            write(self.title_2)
            write(self.x_axis)
            write(self.y_axis)
            write(' %d' % self.scale_mode)
            write('%f, %f' % (self.legend_coordinate[0], self.legend_coordinate[1]))

            # Grid
            if self.dense_grid:
                write('DenseGrid')

            write('Grid Type')
            write('0%d' % self.grid_type)

            write('LineWidths')
            line_width = ''
            for item in self.data:
                line_width += ' %d' % item.line_width
            write(line_width)

            # Legend Title
            if self.legend_title is not '':
                write('Lname')
                write(self.legend_title)

            if self.legend_frame is False:
                write('NoLegendFrame')

            write('Legend Line Width')
            write(' %f' % self.legend_line_width)

            write('PointSizes')
            write('7')
            write(' %d %d %d %d %d %d %d' %
                  (self.font_size['numbers'],
                   self.font_size['first_title'],
                   self.font_size['second_title'],
                   self.font_size['x_axis'],
                   self.font_size['y_axis'],
                   self.font_size['legend'],
                   self.font_size['note']))

            # Symbol Size
            write('SymbolSizes')
            symbol_size = ''
            for item in self.data:
                symbol_size += ' %d' % item.symbol_size
            write(symbol_size)

            if self.legend_transparent:
                write('TransparentLegend')

            if self.title_3 is not '':
                # Write Title 3
                write('Title3')
                write(self.title_3)

            # End
            write('Stop')


class DplotCurve(object):
    """
    DPlot Curve data and attributes

    """
    def __init__(self, x, y, *args, **kwargs):
        """
        Initialize Curve

        :param x:
        :param y:
        :param args:
        :param kwargs:
        :return:
        """
        self.x = x
        self.y = y

        self.line_type = kwargs.get('line_type', 1)
        self.symbol_type = kwargs.get('symbol_type', 0)
        self.line_width = kwargs.get('line_width', 30)
        self.symbol_size = kwargs.get('symbol_size', 0)

        self.legend_title = kwargs.get('title', '')
        self.curve_title = kwargs.get('curve_title', '')

    def write_data(self, write):
        """
        Write curve data

        :param write: function
        :return:
        """
        # Write Number of Points
        write('%d' % len(self.y))

        # Write plot
        for x, y in zip(self.x, self.y):
            # write('%f, %f' % (x, y))
            write(str(x) + ', ' + str(y))

        # Line Type and Symbol Type
        write(' %d %d' % (self.line_type, self.symbol_type))

        write(self.legend_title)       # Legend Title
        write(self.curve_title)       # Curve Label

    def write_dx(self, write):
        """
        Write data in equal increment

            75
            1,0.992115,0.968583,0.929776,0.876307
            0.809017,0.728969,0.637424,0.535827,0.425779
            0.309017,0.187381,0.062791,-0.062791,-0.187381
            -0.309017,-0.425779,-0.535827,-0.637424,-0.728969
            -0.809017,-0.876307,-0.929776,-0.968583,-0.992115
            -1,-0.992115,-0.968583,-0.929776,-0.876307
            -0.809017,-0.728969,-0.637424,-0.535827,-0.425779
            -0.309017,-0.187381,-0.062791,0.062791,0.187381
            0.309017,0.425779,0.535827,0.637424,0.728969
            0.809017,0.876307,0.929776,0.968583,0.992115
            1,0.992115,0.968583,0.929776,0.876307
            0.809017,0.728969,0.637424,0.535827,0.425779
            0.309017,0.187381,0.062791,-0.062791,-0.187381
            -0.309017,-0.425779,-0.535827,-0.637424,-0.728969
            -0.809017,-0.876307,-0.929776,-0.968583,-0.992115
            0,1.48
             3  268

        Legend 2
        :param write:
        :return:
        """
        # Write Number of Points
        write('%d' % len(self.y))

        # Write plot
        for index in range(0, len(self.y), 5):
            # TODO: Need to check for uneven increment
            write('%f, %f, %f, %f, %f' % (self.y[index], self.y[index+1], self.y[index+2], self.y[index+3], self.y[index+4]))

        write('%f,%f' % (self.x[0], self.x[-1]))

        # Line Type and Symbol Type
        write(' %d %d' % (self.line_type, self.symbol_type))

        write(self.legend_title)       # Legend Title
        write(self.curve_title)       # Curve Label

