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

import wx
import wx.aui

DEBUG = True

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
    app = wx.App(False)

    # Check if the a file path is passed with the executable.
    project = Project()
    controller = MainController(project, master_key=MASTER_KEY, setting=setting)

    frame = MainWindow(parent=None, controller=controller, title='Sample Editor')

    # Set Components.
    controller.set_key(MENU_BAR_KEY)

    # Tree Panel.
    # controller.windows['tree'] = ProjectTree(frame, controller, project)
    # frame.add_pane(controller.windows['tree'], wx.LEFT, 'Project Tree')
    controller.add_pane(
        ProjectTree(frame, controller, project),
        'tree',
        wx.LEFT,
        'Project Tree'
    )
    # General Panel
    # controller.windows['general'] = GeneralPanel(parent=frame)
    # frame.add_pane(controller.windows['general'], wx.CENTER, 'View')

    # controller.windows['chart_2d'] = Chart2d(parent=frame)
    # frame.add_pane(controller.windows['chart_2d'], wx.CENTER, 'Chart 2d')
    # controller.windows['chart_2d'].plot()
    #
    # controller.windows['prop grid'] =
    # frame.add_pane(controller.windows['prop grid'], wx.BOTTOM, 'Prop Grid')
    controller.add_pane(
        PropGrid(frame, controller, style=wx.propgrid.PG_SPLITTER_AUTO_CENTER),
        'prop grid',
        wx.BOTTOM,
        'Property'
    )

    # Load Model
    frame.Show(True)
    app.SetTopWindow(frame=frame)
    controller.refresh()
    app.MainLoop()
