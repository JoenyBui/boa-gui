import wx

__author__ = 'jbui'


class LayoutDimensions(object):
    """

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

        :param kwargs:
        :return:
        """
        self.top = kwargs.get('top', 1)
        self.bottom = kwargs.get('bottom', 1)
        self.left = kwargs.get('left', 1)
        self.right = kwargs.get('right', 1)
        self.interior = kwargs.get('interior', 1)

        self.overall_width = kwargs.get('overall_width', 200)
        self.overall_height = kwargs.get('overall_height', 30)

        self.columns = kwargs.get('columns', 2)
        self.widths = kwargs.get('widths', (150, 100, ))
        self.height = kwargs.get('height', 25)

        self.absolute = kwargs.get('absolute', True)

        self.make_stretchable = kwargs.get('make_stretchable', 1)
        self.border_width = kwargs.get('border_width', 0)
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

        :return:
        """
        pass
