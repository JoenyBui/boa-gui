import wx
import wx.richtext

from lxml import html

__author__ = 'Joeny'


class SmartRichText(wx.richtext.RichTextCtrl):
    """
    Smarter Rich Text box.

    """
    def __init__(self, parent, id=-1, value=wx.EmptyString, style=wx.richtext.RE_MULTILINE,
                 validator=wx.DefaultValidator, background_colour=wx.NullColour, *args, **kwargs):

        wx.richtext.RichTextCtrl.__init__(
            self, parent, id=id, value=value, style=style, validator=validator, *args, **kwargs
        )

        # Set the background colour.
        self.SetBackgroundColour(background_colour)

    def add_new_line(self):
        self.Newline()

    def clear(self):
        self.Clear()

    def write(self, text):
        """
        Write text

        :param text:
        :return:
        """
        self.WriteText(text)

        self.add_new_line()

        pass
        self.BeginSuppressUndo()
        self.BeginParagraphSpacing(0, 20)
        self.BeginAlignment(wx.TEXT_ALIGNMENT_CENTRE)
        self.BeginBold()
        self.BeginFontSize(14)
        self.EndFontSize()
        self.BeginItalic()
        self.EndItalic()
        self.EndAlignment()
        self.EndBold()
        self.BeginSymbolBullet('*', 100, 60)
        self.EndSymbolBullet()
