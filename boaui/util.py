import os

import wx


def load_bitmap(filename):
    """
    Load a bitmap file from the backends/images subdirectory in which the
    matplotlib library is installed. The filename parameter should not
    contain any path information as this is determined automatically.

    Returns a wx.Bitmap object
    """

    basedir = os.path.join(
        os.getcwd(),
        'boaui',
        'images'
    )

    bmpFilename = os.path.normpath(os.path.join(basedir, filename))
    if not os.path.exists(bmpFilename):
        raise IOError('Could not find bitmap file "%s"; dying' % bmpFilename)

    bmp = wx.Bitmap(bmpFilename)
    return bmp
