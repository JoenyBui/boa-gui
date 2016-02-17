from collections import OrderedDict

import wx

__author__ = 'jbui'

# There are method keys that corresponds to a specific controller action from the project.
METHOD_SEPARATOR = wx.ID_SEPARATOR

METHOD_NEW_PROJECT = wx.ID_NEW
METHOD_OPEN_PROJECT = wx.ID_OPEN
METHOD_SAVE_PROJECT = wx.ID_SAVE
METHOD_SAVE_AS_PROJECT = wx.ID_SAVEAS
METHOD_CLOSE_ALL = wx.ID_CLOSE_ALL
METHOD_EXIT_PROJECT = wx.ID_EXIT
METHOD_FILE = wx.ID_FILE

METHOD_EDIT = wx.ID_EDIT
METHOD_UNDO = wx.ID_UNDO
METHOD_REDO = wx.ID_REDO
METHOD_CUT = wx.ID_CUT
METHOD_COPY = wx.ID_COPY
METHOD_PASTE = wx.ID_PASTE

METHOD_VIEW = wx.NewId()
METHOD_TOOLBAR = wx.NewId()
METHOD_TOOLBAR_STANDARD = wx.NewId()
METHOD_TOOLBAR_MODEL = wx.NewId()

METHOD_WINDOW = wx.NewId()
METHOD_WINDOW_TREE = wx.NewId()
METHOD_WINDOW_CONSOLE = wx.NewId()
METHOD_WINDOW_PROP_GRID = wx.NewId()

METHOD_HELP = wx.ID_HELP
METHOD_ABOUT = wx.ID_ABOUT

MASTER_KEY = {
    METHOD_NEW_PROJECT:         dict(name='New Project'),
    METHOD_OPEN_PROJECT:        dict(name='Open Project'),
    METHOD_SAVE_PROJECT:        dict(name='Save Project'),
    METHOD_SAVE_AS_PROJECT:     dict(name='Save Project As'),
    METHOD_CLOSE_ALL:           dict(name='Close All Projects'),
    METHOD_EXIT_PROJECT:        dict(name='Exit'),

    METHOD_EDIT:                dict(name='Edit'),
    METHOD_UNDO:                dict(name='Undo'),
    METHOD_REDO:                dict(name='Redo'),
    METHOD_CUT:                 dict(name='Cut'),
    METHOD_COPY:                dict(name='Copy'),
    METHOD_PASTE:               dict(name='Paste'),

    METHOD_TOOLBAR_STANDARD:    dict(name='Toolbar Standard'),
    METHOD_TOOLBAR_MODEL:       dict(name='Toolbar Model'),

    METHOD_WINDOW_TREE:         dict(name='Window Tree'),
    METHOD_WINDOW_CONSOLE:      dict(name='Window Console'),
    METHOD_WINDOW_PROP_GRID:    dict(name='Window Property'),
    METHOD_HELP:                dict(name='&Help'),
    METHOD_ABOUT:               dict(name='&About')
}


TOOLBAR_FILE_KEY = [
    OrderedDict(
        id=METHOD_NEW_PROJECT,
        label='New Project',
        bitmap=wx.ART_NEW,
    ),
    OrderedDict(
        id=METHOD_OPEN_PROJECT,
        label='Open Project',
        bitmap=wx.ART_FILE_OPEN
    ),
    OrderedDict(
        id=METHOD_SEPARATOR,
        label='Separate',
    ),
    OrderedDict(
        id=METHOD_SAVE_PROJECT,
        label='Save Project',
        bitmap=wx.ART_FILE_SAVE
    ),
    OrderedDict(
        id=METHOD_SAVE_AS_PROJECT,
        label='Save As Project',
        bitmap=wx.ART_FILE_SAVE_AS
    ),
    OrderedDict(
        id=METHOD_EXIT_PROJECT,
        label='Exit',
        bitmap=wx.ART_CLOSE
    ),
    OrderedDict(
        id=METHOD_SEPARATOR
    ),
    OrderedDict(
        id=METHOD_CUT,
        label='Cut',
        bitmap=wx.ART_CUT
    ),
    OrderedDict(
        id=METHOD_COPY,
        label='Copy',
        bitmap=wx.ART_COPY
    ),
    OrderedDict(
        id=METHOD_PASTE,
        label='Paste',
        bitmap=wx.ART_PASTE
    ),
    OrderedDict(
        id=METHOD_SEPARATOR,
    ),
    OrderedDict(
        id=METHOD_UNDO,
        label='Undo',
        bitmap=wx.ART_UNDO
    ),
    OrderedDict(
        id=METHOD_REDO,
        label='Redo',
        bitmap=wx.ART_REDO
    )
]


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
                id=METHOD_SEPARATOR,
                name='Separator'
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
                id=METHOD_SEPARATOR,
                name='Separator'
            ),
            OrderedDict(
                id=METHOD_EXIT_PROJECT,
                name='E&xit'
            )
        ]
    ),
    OrderedDict(
        name='&Edit',
        id=METHOD_EDIT,
        keys=[
            OrderedDict(
                id=METHOD_UNDO,
                name='&Undo'
            ),
            OrderedDict(
                id=METHOD_REDO,
                name='&Redo',
            ),
            OrderedDict(
                id=METHOD_SEPARATOR,
                name='Separator'
            ),
            OrderedDict(
                id=METHOD_CUT,
                name='Cu&t'
            ),
            OrderedDict(
                id=METHOD_COPY,
                name='&Copy'
            ),
            OrderedDict(
                id=METHOD_PASTE,
                name='&Paste'
            )
        ]
    ),
    OrderedDict(
        name='&View',
        id=METHOD_VIEW,
        keys=[
            OrderedDict(
                id=METHOD_TOOLBAR,
                name='Toolbar',
                keys=[
                    OrderedDict(
                        id=METHOD_TOOLBAR_STANDARD,
                        name='Standard'
                    ),
                    # OrderedDict(
                    #     id=METHOD_TOOLBAR_MODEL,
                    #     name='Model'
                    # )
                ]
            ),
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
