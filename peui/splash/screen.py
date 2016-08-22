
import wx
import wx.lib.agw.advancedsplash as AS


class SplashScreen(AS.AdvancedSplash):
    """

    """
    def __init__(self, imagePath='PEC.png'):
        """

        :param imagePath:
        :return:
        """
        frame = wx.Frame(None, -1, "AdvancedSplash Test")

        bitmap = wx.Bitmap(imagePath, wx.BITMAP_TYPE_PNG)
        shadow = wx.WHITE

        AS.AdvancedSplash.__init__(
            self, frame, bitmap=bitmap, timeout=5000,
            agwStyle=AS.AS_TIMEOUT | AS.AS_CENTER_ON_PARENT | AS.AS_SHADOW_BITMAP, shadowcolour=shadow
        )

        # Attributes
        self.gauge = wx.Gauge(self, size=(-1, 16))

        # Setup
        rect = self.GetClientRect()
        new_size = (rect.width, 16)
        self.gauge.SetSize(new_size)
        self.SetSizer((rect.width, rect.height + 16))
        self.gauge.SetPosition((0, rect.height))

    def set_progress(self, percent):
        """
        Set the indicator gauges progress.

        :param percent:
        :return:
        """
        self.gauge.SetValue(percent)

    def get_progress(self):
        """

        :return:
        """
        return self.gauge.GetValue()

