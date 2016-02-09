from collections import OrderedDict

import wx

__author__ = 'jbui'

# There are method keys that corresponds to a specific controller action from the project.
METHOD_NEW_PROJECT = wx.ID_NEW
METHOD_OPEN_PROJECT = wx.ID_OPEN
METHOD_SAVE_PROJECT = wx.ID_SAVE
METHOD_SAVE_AS_PROJECT = wx.ID_SAVEAS
METHOD_CLOSE_ALL = wx.ID_CLOSE_ALL
METHOD_EXIT_PROJECT = wx.ID_EXIT
METHOD_FILE = wx.ID_FILE

METHOD_VIEW = wx.NewId()
METHOD_WINDOW = wx.NewId()
METHOD_WINDOW_TREE = wx.NewId()
METHOD_WINDOW_CONSOLE = wx.NewId()
METHOD_WINDOW_PROP_GRID = wx.NewId()

METHOD_HELP = wx.ID_HELP
METHOD_ABOUT = wx.ID_ABOUT

MASTER_KEY = {
    METHOD_NEW_PROJECT:     dict(name='New Project'),
    METHOD_OPEN_PROJECT:    dict(name='Open Project'),
    METHOD_SAVE_PROJECT:    dict(name='Save Project'),
    METHOD_SAVE_AS_PROJECT: dict(name='Save Project As'),
    METHOD_CLOSE_ALL:       dict(name='Close All Projects'),
    METHOD_EXIT_PROJECT:    dict(name='Exit'),

    METHOD_WINDOW_TREE:     dict(name='Window Tree'),
    METHOD_WINDOW_CONSOLE:  dict(name='Window Console'),
    METHOD_WINDOW_PROP_GRID:dict(name='Window Property'),
    METHOD_HELP:            dict(name='&Help'),
    METHOD_ABOUT:           dict(name='&About')
}

MENU_BAR_KEY = [
    OrderedDict(
        name='&File',
        id=METHOD_FILE,
        keys=[
            OrderedDict(
                id=METHOD_NEW_PROJECT,
                name='&New Project'
            ),
            OrderedDict(
                id=METHOD_OPEN_PROJECT,
                name='&Open Project'
            ),
            OrderedDict(
                id=METHOD_SAVE_PROJECT,
                name='Save Project'
            ),
            OrderedDict(
                id=METHOD_SAVE_AS_PROJECT,
                name='Save As Project'
            ),
            OrderedDict(
                id=METHOD_EXIT_PROJECT,
                name='E&xit'
            )
        ]
    ),
    OrderedDict(
        name='View',
        id=METHOD_VIEW,
        keys=[
            OrderedDict(
                id=METHOD_WINDOW,
                name='Window',
                keys=[
                    OrderedDict(
                        id=METHOD_WINDOW_TREE,
                        name='Project Tree'
                    ),
                    OrderedDict(
                        id=METHOD_WINDOW_PROP_GRID,
                        name='Property'
                    ),
                    OrderedDict(
                        id=METHOD_WINDOW_CONSOLE,
                        name='Console'
                    ),
                ]
            ),
        ]
    ),
    OrderedDict(
        name='Help',
        id=METHOD_HELP,
        keys=[
            OrderedDict(
                id=METHOD_ABOUT,
                name='About',
            ),
        ]
    )
]

CONTEXT_MENU_KEY = dict(

)
