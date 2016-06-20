__author__ = 'jbui'

length = [

]

import os
import sys
import matplotlib
import pandas as pd
import numpy as np

import wx
import wx.lib.mixins.inspection as WIT
import wx.aui

import wx.lib.agw.aui as aui

from peui.main.window import MainWindow
from peui.controller.main import MainController
from peui.model.project import Project
from peui.tree.project import ProjectTree
from peui.panel.general import GeneralPanel
from peui.panel.grid import PropGrid
from peui.chart.ch2d import Chart2d
from peui.setting import Setting
from peui.view.vtk import VtkViewer
from peui.panel.xlsx import SpreadSheet
from peui.view.terminal import Console

import config as cfg
from peui.config import MASTER_KEY, MENU_BAR_KEY, TOOLBAR_FILE_KEY
from peui.main.toolbar import CustomToolBar

DEBUG = True

# matplotlib.use('WXAgg')

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAt6LRm4kBeWOVYP1Y4kaBsqqtPt38F2QUHHzSRuRcvR50ylTD
zBPG9ZIcFxXSNqsZdCYSemkQua2l84op0aijr6v3uQS+Xe7Pda97eiPfZVOBqM9p
FN2k3m8VSRRdN29XFl15KsNMYkC8T85QMuNO2uOtuSYk6vIh1yrqZpPPdp7Pqp7J
loywfDP8GL8xOXr6Y2hLmJOVJ5WoNZ7ABjWwwDaNQXCwvmzxoUbrGFFK0kqNWM44
2mp19GuuREHTioOzXb1HU/S2Ei/VNqerO+PBo42cOpVR13A2A+VbDx34XtZHhl4I
Ow8RBe4t/OEfJY5tNxmcoH1RodQ+UfajpI+ZGwIDAQABAoIBAFiCncz9yDweB43s
Dr9hhHn9UeuPS0Zq8laYwzFwOFLfLyOmn4jpr2gFuIxX9C5tYaNeBmIB6hHU5Lvx
yB5JzjuKA6il5KuZw1zR7A3+5FoOWdxnvBpWinS7zeKfch6aB7u76f72iwaAdUNy
Ca29afCO9NjczcaAVldDVB+E9uYQ7LGBLitoUijwE+t+1/L9Qfy9vquWvqTWaAz0
M2SToauzPDjf9ZekMR+98fHSaWyJ2L5r2C8aUzoagXdVhM3W2VTYQVEe8FYjAfIm
0Kla9PoOyH+wI+XyPjXxWBXGTx1n5dYCDvrGj0hDM5rf+y2opyGqPEK8H55cN5JL
kSBhvuECgYEA3S5WtgSJqa2siQ5nLGtGj9MnujLnORl+9sCWCdQbxMFR2Y0SatPs
+unDWaR0gkyvzIIjdEO8zAjCjHTyCUQTHlAitN4IisCXlt//Bq6D0Y6m+v6tngkL
o9RqZSiWqZDSIvjEwWhmaZCHkN8sbS61PqsRbA2IezwlMg+rfWBPaAUCgYEA1Itn
wDh0cTkI0fZBTHcngZiV7Xvuu3Z2zbKoTLQJujU//Wu4Lcz8T4Ix5Sf4cQDkyL8H
r/rLmTjdZHHs6oDThttYEQoRX19QBFWdgDYDVbv7Y33FopNgOdBvqbHEHZj0+kPy
g4Be/DUIP3IG20h6B8oZpahhlCX8JzW4+/ZcZp8CgYAlcPCwwzfih0nLsap5dHdv
ZVk2ReOqYMyDTLqZU1SYC/mlECJr/xAAsY2mIRav7/dacTU7OzQ8fcchK7LFKsbp
vLsDTwq3Ij8HBUgQg35A/Rr7Jh2RwQo9Y3nXQfWvIprP3LjB3MBpYlPwjDbjDKMV
xrOeTPQrmFTbkpd/E8ydWQKBgB8Q3TJITiS6bGKb9sFhbSHRFqDmi2dVElpQca78
ZauU2uyEkSAIpRxN8FMJO5PwyH/bBBmhs56KpDlpOXKxL7m3V7Dt4soo2T448VNr
EaO3XTAWkwuHNPpeT+PiusKEt9HYmprD6Z49dh4n4X6tokB/Nq5y5QhNYQSuIoKZ
aLoLAoGAIsj43kGRqJVQYMy7dlJkQxuHNI+8z1g9muagUoF+SiEYANq0d9c2tfrS
6yC8NAS+7XwePJchJT64p8J+fnZqB1Vrjog7LBXUvjkjCbgcm95PLYglOM0MyBIA
nKpfTntxSvu2PSWJE4/wKFGO8qX7VL6FXDevwvzKdyBmxTQkAfk=
-----END RSA PRIVATE KEY-----"""

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8ZLCrF7wWkbF7r2gN6MM
56z8iO4FJZ/DRnJIMHrnMFvB5LR6KpUS7cMTKWM5ZQD+dk7+70hwcwLCC8m1u4G7
VmnSuRR0bhO1weyjfRhj3msS13RnpGpGvtYTsfL0nIep6QRF5MjSw6dVWq9VE46M
PbW6Q24lEpz7vF4Yj+cKwrvUzYM4kfxqCfyXTI3nEVEgwRPrfcpqMAvNzXo29TO4
iypSInHEeKEcaGfK3Aae7k6FgJb/wqVTomBNn7NUmNRhch3OohsE9as0axO0xThY
PlJhR2Gg+UlnGbXRcO9uo134SAy894BZ06oJfpcx5HvowMBgUyeSFfnWbutU4/p7
ywIDAQAB
-----END PUBLIC KEY-----"""

if __name__ == '__main__':

    setting = Setting()

    # Initialize Application
    if DEBUG:
        # Use Ctrl-Alt-I to open the Widget Inspection Tool
        # http://wiki.wxpython.org/Widget%20Inspection%20Tool
        app = WIT.InspectableApp()

    else:
        lm = LicenseClientManager()
        lm.load_private_key(PRIVATE_KEY)
        lm.load_public_key(PUBLIC_KEY)
        lm.open_encrypted_file(setting.efile)
        lm.open_encrypted_key(setting.ekey)
        lm.open_encrypted_signature(setting.esignature)

        if lm.unencrypted_file() is False:
            exit()

        if (lm.check_username() and lm.check_system_name() and lm.check_mac_address() and lm.check_end_date()) is False:
            exit()

        app = wx.App(False)

    # Check if the a file path is passed with the executable.
    project = Project()
    controller = MainController(project, master_key=MASTER_KEY, setting=setting)
    frame = MainWindow(parent=None, controller=controller, title='Sample Editor')
    controller.notebook = aui.AuiNotebook(frame, agwStyle=aui.AUI_NB_CLOSE_ON_ALL_TABS)
    controller.add_pane(controller.notebook, 'notebook', wx.CENTER, 'Notebook')

    # Add test data
    project.data = [np.arange(0.0, 3.0, 0.01), np.sin(2 * np.pi * np.arange(0.0, 3.0, 0.01))]

    # Set Components.
    controller.set_key(MENU_BAR_KEY)

    # Tree Panel.
    controller.add_pane(
        ProjectTree(frame, controller, project),
        cfg.METHOD_WINDOW_TREE,
        wx.LEFT,
        'Project Tree'
    )

    # Property Panel
    controller.add_pane(
        PropGrid(frame, controller, None, style=wx.propgrid.PG_SPLITTER_AUTO_CENTER),
        cfg.METHOD_WINDOW_PROP_GRID,
        wx.BOTTOM,
        'Property'
    )

    controller.add_pane(
        Console(frame, controller),
        cfg.METHOD_WINDOW_CONSOLE,
        wx.BOTTOM,
        'Output'
    )

    controller.add_pane(
        CustomToolBar(frame, controller, TOOLBAR_FILE_KEY, agwStyle=aui.AUI_TB_GRIPPER | aui.AUI_TB_OVERFLOW),
        cfg.METHOD_TOOLBAR_STANDARD,
        aui.AuiPaneInfo().Name('std_tb').Caption('Standard Toolbar').ToolbarPane().Top().Gripper()
    )

    controller.add_page(
        GeneralPanel(parent=frame),
        cfg.METHOD_WINDOW_GENERAL,
        'General',
        False
    )

    controller.add_page(
        Chart2d(frame, controller, None, 111),
        cfg.METHOD_WINDOW_CHART,
        'Chart',
        True
    )

    controller.add_page(
        SpreadSheet(frame, controller),
        cfg.METHOD_WINDOW_XLSX,
        'XLSX',
        True
    )

    # Load Model
    frame.Show(True)
    app.SetTopWindow(frame=frame)
    controller.refresh()

    app.MainLoop()
