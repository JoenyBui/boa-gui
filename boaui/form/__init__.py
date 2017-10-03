import math

import wx

__author__ = 'Joeny'


class DpiAwareness(object):
    """
    DPI is the physical measurement of the number of pixels in a linear inch of a display.  For desktop monitors, this
    is typically 96 DPI or lower.  However, newer displays for tablets and laptops may be 96 DPI or lower.  In
    Windows 8.1, DPI values for the desktop are divided into four groups: 96, 120, 144, and 192.

    """
    DPI_96 = 1.0
    DPI_120 = 1.25
    DPI_144 = 1.50
    DPI_192 = 2.0

    def __init__(self, *args, **kwargs):
        self.dpi = wx.ScreenDC().GetPPI()
        self.dpi_scale = 1.0

        if self.dpi[0] >= 192.0:
            self.dpi_scale = self.DPI_192
        elif self.dpi[0] >= 144.0:
            self.dpi_scale = self.DPI_144
        elif self.dpi[0] >= 120.0:
            self.dpi_scale = self.DPI_120
        else:
            self.dpi_scale = self.DPI_96

    def scale(self, value):
        """
        Scale value based off of dpi.

        :param value:
        :return:
        """
        if isinstance(value, tuple) or isinstance(value, list):
            objects = []

            for obj in value:
                objects.append(int(math.ceil(obj*self.dpi_scale)))

            if isinstance(value, tuple):
                return tuple(objects)
            else:
                return objects
        else:
            return int(math.ceil(value*self.dpi_scale))
