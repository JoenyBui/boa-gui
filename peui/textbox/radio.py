import wx

from .smart import SmartInputLayout


__author__ = 'jbui'


class RadioSmartButton(wx.RadioButton):
    """
    Radio Smart Box
    
    """
    def __init__(self, parent, click_up=None, message=None, data=None, enable=None, *args, **kwargs):
        wx.RadioButton.__init__(self, parent, *args, **kwargs)

        self.keys = kwargs.get('keys', {})
        self.parent = parent
        self.data = data

        self.message = message

        if click_up:
            self.bind_click(click_up)

    def bind_click(self, handle):
        self.Bind(wx.EVT_RADIOBUTTON, handle)

