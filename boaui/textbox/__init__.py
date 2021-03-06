import wx
from wx.lib.agw.supertooltip import SuperToolTip

from ..form import DpiAwareness

__author__ = 'Joeny'


class LayoutDimensions(DpiAwareness):
    """
    Styling for layout textbox

    ** note: do not apply DPI scaling, done within class


    /---------------- OVERALL WIDTH ----------------------/
    |                                                     |
    |                                                     |

    *******************************************************     ----/
    *    *     * *                     * *              * *         |
    *******************************************************         |
    *    *     * *                     * *              * *
    *    * (1) * *         (2)         * *     (3)      * *     OVERALL HEIGHT
    *    *     * *                     * *              * *
    *******************************************************         |
    *    *     * *                     * *              * *         |
    *******************************************************     ----/


    """
    def __init__(self, **kwargs):
        """
        Constructor

        :param kwargs:
        :return:
        """
        DpiAwareness.__init__(self)

        self.top = self.scale(kwargs.get('top', 1))
        self.bottom = self.scale(kwargs.get('bottom', 1))
        self.left = self.scale(kwargs.get('left', 1))
        self.right = self.scale(kwargs.get('right', 1))
        self.interior = self.scale(kwargs.get('interior', 1))

        self.overall_width = self.scale(kwargs.get('overall_width', 200))
        self.overall_height = self.scale(kwargs.get('overall_height', 30))

        self.widths = self.scale(kwargs.get('widths', (150, 100, 100, )))
        self.height = self.scale(kwargs.get('height', 24))

        self.absolute = kwargs.get('absolute', True)

        # A stretch factor: If a sizer contains more than one child and it is offered more space than its children and
        # their borders need, the question arises how to distribute the surplus space among the children. For this
        # purpose, a stretch factor may be assigned to each child, where the default value of 0 indicates that the
        # child will not get more space than its requested minimum size. A value of more than zero is interpreted in
        # relation to the sum of all stretch factors in the children of the respective sizer, i.e. if two children get
        # a stretch factor of 1, they will get half the extra space each independent of whether one control has a
        # minimal sizer inferior to the other or not. The following sample shows a dialog with three buttons, the first
        # one has a stretch factor of 1 and thus gets stretched, whereas the other two buttons have a stretch factor of
        # zero and keep their initial width:
        self.stretch_factor = kwargs.get('stretch_factor', [])

        self.border_width = kwargs.get('border_width', [])
        self.flags = kwargs.get('flags', (wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, wx.ALIGN_CENTER))

    def get_size(self, component_index):
        """
        Get the size.

        :param component_index:
        :return:
        """
        return wx.Size(self.widths[component_index], self.height)

    def calculate(self):
        """
        Calculate the overall width and height:
            * if absolute calculate overall width and height
            * if percentage than specify the widths and heights

        :return:
        """
        if self.absolute:
            self.overall_height = self.top + self.bottom + self.height
            self.overall_width = self.left + self.right
            for width in self.widths:
                self.overall_width += width

        else:
            # TODO: Update percentage calculations.
            pass

        # Check if stretch factor and border widths are specified.
        NO_STRETCHING = 0
        BORDER_WIDTH_NONE = 0
        for id in range(0, len(self.widths)):
            if id >= len(self.stretch_factor):
                self.stretch_factor.append(NO_STRETCHING)

            if id >= len(self.border_width):
                self.border_width.append(BORDER_WIDTH_NONE)


class SmartToolTip(SuperToolTip):
    """
    Smarter Tooltip

    """
    def __init__(self, message, target,
                 bodyImage=wx.NullBitmap, header=" ", headerBmp=wx.NullBitmap,
                 footer="", footerBmp=wx.NullBitmap):

        SuperToolTip.__init__(self, message=message, bodyImage=bodyImage, header=header, headerBmp=headerBmp,
                              footer=footer, footerBmp=footerBmp)

        if target:
            self.SetTarget(target)

        self.SetDrawHeaderLine(True)
        self.ApplyStyle("Office 2007 Blue")
        self.SetDropShadow(True)

        self.Show(True)

    def enable(self):
        self.Show(True)

    def disable(self):
        self.Show(False)


class SmartHelpButton(wx.ContextHelpButton):
    """
    Smart Help Button

    """
    def __init__(self, parent, helptext=None, minsize=wx.Size(24, 24), evt_click=None, *args, **kwargs):
        wx.ContextHelpButton.__init__(self, parent, *args, **kwargs)

        if helptext:
            self.SetHelpText(helptext)

        if minsize:
            self.SetMinSize(minsize)

        if evt_click:
            self.Bind(wx.EVT_BUTTON, evt_click)
