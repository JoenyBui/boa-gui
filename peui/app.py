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

    from .config import MASTER_KEY, MENU_BAR_KEY

    #TODO: Smart Textbox
    #TODO: Undo-Redo Model
    #TODO: Cut & Paste
    #TODO: Printing Pdf & Docx
    #TODO: Open & Close Project
    #TODO: License Manager
    #TODO: Backup Temp File
    #TODO: Periodic Savings

    # Initialize Application
    app = wx.App(False)
    project = Project()
    controller = MainController(project, master_key=MASTER_KEY)

    frame = MainWindow(parent=None, controller=controller, title='Sample Editor')

    # Set Components.
    controller.set_key(MENU_BAR_KEY)

    # Tree Panel.
    pt = ProjectTree(frame, controller, project)
    frame.add_pane(pt, wx.LEFT, 'Project Tree')

    # General Panel
    gp = GeneralPanel(parent=frame)
    frame.add_pane(gp, wx.CENTER, 'View')

    # Load Model
    frame.Show(True)
    app.SetTopWindow(frame=frame)
    app.MainLoop()
