"""
 *  PROTECTION ENGINEERING CONSULTANTS CONFIDENTIAL
 *
 *  [2014] - [2015] Protection Engineering Consultants
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Protection Engineering Consultants and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Protection Engineering Consultants
 * and its suppliers and may be covered by U.S. and Foreign Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Protection Engineering Consultants.
"""
import os
import sys

import matplotlib

import wx
import wx.lib.mixins.inspection as WIT
import wx.aui

import wx.lib.agw.aui as aui

DEBUG = True

matplotlib.use('WXAgg')

if __name__ == '__main__' and __package__ is None:
    # Relative Import Hack
    package_name = 'peui'
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(1, parent_dir)
    mod = __import__(package_name)
    sys.modules[package_name] = mod
    __package__ = package_name

    from .main.window import MainWindow
    from .controller.main import MainController
    from .model.project import Project
    from .tree.project import ProjectTree
    from .panel.general import GeneralPanel
    from .panel.grid import PropGrid
    from .chart.ch2d import Chart2d
    from .setting import Setting
    from .view.vtk import VtkViewer
    from .panel.xlsx import SpreadSheet
    from .view.terminal import Console

    from .config import MASTER_KEY, MENU_BAR_KEY

    #TODO: Smart Textbox
    #TODO: Undo-Redo Model
    #TODO: Cut & Paste
    #TODO: Printing Pdf & Docx
    #TODO: Open & Close Project
    #TODO: License Manager
    #TODO: Backup Temp File
    #TODO: Periodic Savings

    setting = Setting()

    # Initialize Application
    if DEBUG:
        # Use Ctrl-Alt-I to open the Widget Inspection Tool
        # http://wiki.wxpython.org/Widget%20Inspection%20Tool
        app = WIT.InspectableApp()

    else:
        app = wx.App(False)

    # Check if the a file path is passed with the executable.
    project = Project()
    controller = MainController(project, master_key=MASTER_KEY, setting=setting)
    frame = MainWindow(parent=None, controller=controller, title='Sample Editor')
    controller.notebook = aui.AuiNotebook(frame)
    controller.add_pane(controller.notebook, 'notebook', wx.CENTER, 'Notebook')

    # Set Components.
    controller.set_key(MENU_BAR_KEY)

    # Tree Panel.
    controller.add_pane(
        ProjectTree(frame, controller, project),
        'tree',
        wx.LEFT,
        'Project Tree'
    )

    # Property Panel
    controller.add_pane(
        PropGrid(frame, controller, style=wx.propgrid.PG_SPLITTER_AUTO_CENTER),
        'prop grid',
        wx.BOTTOM,
        'Property'
    )

    controller.add_pane(
        Console(frame, controller), 'console',
        wx.BOTTOM,
        'Output'
    )

    controller.add_page(GeneralPanel(parent=frame), 'general', 'General')
    controller.add_page(Chart2d(frame, 111), 'chart2d', 'Chart')
    controller.add_page(SpreadSheet(frame, controller), 'xlsx', 'XLSX')

    # Load Model
    frame.Show(True)
    app.SetTopWindow(frame=frame)
    controller.refresh()

    print('App Started')
    app.MainLoop()
