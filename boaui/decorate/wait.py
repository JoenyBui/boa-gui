import wx

__author__ = 'Joeny'


def wait_dlg(parent, function, msg='Please wait while we process your request..', *args, **kwargs):
    """
    Wait dialog

    :param parent: parent controller
    :param function: passed the function
    :param msg: message
    :param args:
    :param kwargs:
    :return:
    """
    try:
        dlg = wx.BusyInfo(msg, parent)
        ret = function(*args, **kwargs)
        del dlg

    except Exception as e:
        if dlg:
            del dlg