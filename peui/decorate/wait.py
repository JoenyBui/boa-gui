import wx

__author__ = 'jbui'


def wait_dlg(function, *args, **kwargs):
    """

    :param function:
    :param args:
    :param kwargs:
    :return:
    """
    msg = 'Please wait while we process your request..'
    dlg = wx.BusyInfo(msg)
    ret = function(*args, **kwargs)
    dlg = None
