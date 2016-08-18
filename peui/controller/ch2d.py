import os
import wx

import numpy as np

from ..chart.dlg import FigureSettingDialog, FigureSetting
from ..form.file import SaveXYDialog
from ..chart.dplot import Dplot, DplotCurve

from . import ChildController

__author__ = 'jbui'


class Chart2dController(ChildController):
    """
    Chart 2d controller.

    """
    def __init__(self, parent, view, figure_setting=None):
        """

        :param parent:
        :param view:
        :param figure_setting:
        :return:
        """
        ChildController.__init__(self, parent, view)

        if figure_setting:
            self.figure_setting = figure_setting
        else:
            self.figure_setting = FigureSetting()

    def do_layout(self):
        """
        Draw the chart 2d data.

        :return:
        """
        # Grab project data.
        data = self.parent.project.data

        # Loop through the data set to have multiple plots.
        for i in range(0, len(data), 2):
            self.view.axes.plot(data[i], data[i+1])

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
            self.figure_setting = dlg.setting

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
            dp.x_axis = self.view.axes.get_xaxis().get_label().get_text()

            # Y-Title
            dp.y_axis = self.view.axes.get_yaxis().get_label().get_text()

            for x, y in data:
                dp.add_curve(
                    DplotCurve(
                        list(x), list(y)
                    )
                )

            dp.write_dplot(pathname)

        except IOError as e:

            print(str(e))
