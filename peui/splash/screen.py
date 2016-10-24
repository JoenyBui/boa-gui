import os

import wx
import wx.lib.agw.advancedsplash as AS


class SplashScreen(AS.AdvancedSplash):
    """
    Splash Screen

    """
    def __init__(self,
                 image_path=None,
                 bitmap=None,
                 title='Title',
                 agwStyle=AS.AS_TIMEOUT | AS.AS_CENTER_ON_PARENT,
                 shadowcolour=wx.NullColour,
                 timeout=5000,
                 *args,
                 **kwargs):
        """
        Constructor

        :param image_path:
        :param bitmap:
        :param agwStyle:
        :param shadowcolour:
        :param timeout:
        :param args:
        :param kwargs:
        :return:
        """
        self.frame = wx.Frame(None, -1, title=title)

        if image_path:
            file_name, file_ext = os.path.splitext(image_path)

            if file_ext.lower() == '.jpg':
                bitmap = wx.Bitmap(image_path, wx.BITMAP_TYPE_JPEG)
            elif file_ext.lower() == '.png':
                bitmap = wx.Bitmap(image_path, wx.BITMAP_TYPE_PNG)
            elif file_ext.lower() == '.bmp':
                bitmap = wx.Bitmap(image_path, wx.BITMAP_TYPE_BMP)

        AS.AdvancedSplash.__init__(
            self,
            self.frame,
            bitmap=bitmap,
            timeout=timeout,
            agwStyle=agwStyle,
            shadowcolour=shadowcolour
        )

        # Attributes
        self.gauge = wx.Gauge(self, size=(-1, 16))

        # Setup
        rect = self.GetClientRect()
        new_size = (rect.width, 16)
        self.gauge.SetSize(new_size)
        self.SetSize(wx.Size(rect.width, rect.height + 16))

        self.gauge.SetPosition((0, rect.height))

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.AddStretchSpacer(1)
        vsizer.Add(self.gauge, 0, wx.EXPAND | wx.ALL, 5)

        self.frame.SetSizer(vsizer)

        wx.Yield()

    def set_progress(self, percent):
        """
        Set the indicator gauges progress.

        :param percent:
        :return:
        """
        self.gauge.SetValue(percent)

    def get_progress(self):
        """
        Get progress value

        :return:
        """
        return self.gauge.GetValue()

