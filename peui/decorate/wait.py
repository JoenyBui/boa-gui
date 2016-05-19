import wx

__author__ = 'jbui'


def wait_dlg(function, *args, **kwargs):

    msg = 'Please wait while we process your request..'
    dlg = wx.BusyInfo(msg)
    ret = function(*args, **kwargs)
    dlg = None
