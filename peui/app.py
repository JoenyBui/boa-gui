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

import wx
import wx.aui

from main.window import MainWindow
from controller.main import MainController
from model.project import Project

if __name__ == '__main__':
    #TODO: Smart Textbox
    #TODO: Undo-Redo Model
    #TODO: Cut & Paste
    #TODO: Printing Pdf & Docx
    #TODO: Open & Close Project

    project = Project()
    controller = MainController(project)

    app = wx.App(False)
    frame = MainWindow(parent=None, title='Sample Editor')
    app.SetTopWindow(frame=frame)
    app.MainLoop()
