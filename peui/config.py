import wx

__author__ = 'jbui'

# There are method keys that corresponds to a specific controller action from the project.
METHOD_OPEN_PROJECT = 1
METHOD_SAVE_PROJECT = 2
METHOD_SAVE_AS_PROJECT = 3
METHOD_CLOSE_PROJECT = 4

MASTER_KEY = dict(
    open_project=dict(id=METHOD_OPEN_PROJECT, menuitem='Open Project', )
)

MENU_BAR_KEY = dict(
    file=dict(id=None)
)

CONTEXT_MENU_KEY = dict(

)
