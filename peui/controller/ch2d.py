import wx

from ..chart.dlg import FigureSettingDialog, FigureSetting

from . import ChildController

__author__ = 'jbui'


class Chart2dController(ChildController):

    def __init__(self, parent, view):
        ChildController.__init__(self, parent, view)

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

