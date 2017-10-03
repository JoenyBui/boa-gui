import os

import wx
from wx.lib.colourchooser.canvas import Canvas


class ImageCanvas(wx.Panel):
    """
    Image Panel

    """
    def __init__(self, parent, image_path=None, *args, **kwargs):
        """
        Constructor

        :param parent:
        """
        wx.Panel.__init__(self, parent=parent, *args, **kwargs)

        self.image_path = image_path
        if self.image_path:
            bmp = wx.Bitmap(self.image_path)

            padding = 10
            self.SetMinClientSize((bmp.GetWidth() + padding,
                                   bmp.GetHeight() + padding))

        self.glyphs = []

        # self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent

        # img = wx.EmptyImage(240, 240)

        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_sizer.Add((1, 1), 0, wx.EXPAND, 75)
        # self.main_sizer.Add(img, 0, wx.EXPAND)
        self.main_sizer.Add((1,1), 0, wx.ALL, 75)


        self.SetSizer(self.main_sizer)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase_background)
        self.Bind(wx.EVT_SIZE, self.on_size)

    def set_sizer(self):
        """

        :param sizer:
        :return:
        """
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        for num in range(4):
            label = "Button %s" % num
            btn = wx.Button(self, label=label)
            sizer.Add(btn, 0, wx.ALL, 5)

        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 0, wx.ALL, 75)

        self.SetSizer(hSizer)

    def on_size(self, event):
        """

        :param event:
        """

        event.Skip()
        self.Refresh()

    def scale_image(self, image, max_width=None, max_height=None):
        """

        :param image:
        :param max_width:
        :param max_height:
        :return:
        """
        width = image.GetWidth()
        height = image.GetHeight()
        ratio = min(max_width / width, max_height / height)
        image = image.Scale(ratio * width, ratio * height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)

        return result

    def on_erase_background(self, event):
        """
        Add a picture to the background

        :param event:
        """

        # self.Freeze()

        dc = event.GetDC()
        w, h = self.GetClientSize()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()

        if self.image_path:
            bmp = wx.Bitmap(self.image_path)
            # bmp = self.scale_image(bmp, 100, 200)
            size = bmp.GetSize()

            x = int(w/2.0 - size.x/2.0)
            y = int(h/2.0 - size.y/2.0)

            dc.DrawBitmap(bmp, x, y)

        self.draw_model(dc)

        # self.Thaw()

    def draw_model(self, dc):
        """
        Draw glyps

        :param dc:
        :return:
        """
        for glyph in self.glyphs:
            glyph.draw(dc)


class Glyph(object):
    def __init__(self, *args, **kwargs):
        self.pen_color = kwargs.get('pen_color', wx.BLACK)
        self.pen_width = kwargs.get('pen_width', 5)

        self.coordinates = kwargs.get('coordinates', [])

    def set_pen(self, dc):
        dc.SetPen(self.pen_color, self.pen_width)

    def pre_draw(self, dc):
        self.set_pen()

    def post_draw(self, dc):
        pass

    def _draw_(self, dc):
        pass

    def draw(self, dc):
        self.pre_draw(dc)
        self._draw_(dc)
        self.post_draw(dc)

class Arc(Glyph):
    """

    """
    def _draw_(self, dc):
        pass

class Line(Glyph):
    """

    """
    def _draw_(self, dc):
        xy1 = self.coordinates[0]
        xy2 = self.coordinates[1]

        dc.DrawLine(xy1[0], xy1[1], xy2[0], xy2[1])

class Circle(Glyph):
    """

    """
    def _draw_(self, dc):
        xy = self.coordinates[0]

        dc.DrawCircle(xy[0], xy[1], 100)

class Rectangle(Glyph):
    """

    """
    def _draw_(self, dc):
        pass
