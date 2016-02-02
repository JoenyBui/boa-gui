
import wx
import wx.lib.agw.advancedsplash as AS


class SplashScreen(AS.AdvancedSplash):
    def __init__(self, imagePath='PEC.png'):
        frame = wx.Frame(None, -1, "AdvancedSplash Test")

        bitmap = wx.Bitmap(imagePath, wx.BITMAP_TYPE_PNG)
        shadow = wx.WHITE

        AS.AdvancedSplash.__init__(
            self, frame, bitmap=bitmap, timeout=5000,
            agwStyle=AS.AS_TIMEOUT | AS.AS_CENTER_ON_PARENT | AS.AS_SHADOW_BITMAP, shadowcolour=shadow
        )
