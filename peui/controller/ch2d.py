import wx

from ..chart.dlg import FigureSettingDialog, FigureSetting
from ..form.file import SaveXYDialog

from . import ChildController

__author__ = 'jbui'


class Chart2dController(ChildController):

    def __init__(self, parent, view, figure_setting=None):
        ChildController.__init__(self, parent, view)

        if figure_setting:
            self.figure_setting = figure_setting
        else:
            self.figure_setting = FigureSetting()

    def do_layout(self):
        data = self.parent.project.data

        self.view.axes.plot(data[0], data[1])

        self.bind_toolbar_figure()

        self.update_text()

    def update_text(self):
        self.view.axes.set_title(self.figure_setting.title)
        self.view.axes.set_ylabel(self.figure_setting.y_title)
        self.view.axes.set_xlabel(self.figure_setting.x_title)

    def bind_toolbar_figure(self):
        tb = self.view.toolbar

        tb.Bind(wx.EVT_TOOL, self.on_custom_figure_setting, None, tb.ON_CUSTOM_FIGURE_SETTING)
        tb.Bind(wx.EVT_TOOL, self.on_click_save_xy_data, None, tb.ON_CUSTOM_DPLOT)

    def update_layout(self):
        pass

    def refresh(self):
        pass

    def sync_data(self):
        pass

    def on_custom_figure_setting(self, event):
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
