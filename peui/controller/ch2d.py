import wx

from ..chart.dlg import FigureSettingDialog, FigureSetting
from ..form.file import SaveXYDialog

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

            self.view.save_xy_data(path)

        dlg.Destroy()
