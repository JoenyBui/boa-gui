import wx

__author__ = 'Joeny'


class AboutDialog(wx.AboutDialogInfo):
    """
    About Dialog Info
    """
    licence = """This software is proprietary and cannot be redistributed and/or modified without the
    expressed and written permission of the Joeny.

    Copyright (C) 2016, Joeny, All Rights Reserved.
    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        wx.AboutDialogInfo.__init__(self)

        if kwargs.get('name'):
            self.SetName(kwargs.get('name'))

        if kwargs.get('version'):
            self.SetVersion(kwargs.get('version'))

        if kwargs.get('description'):
            self.SetDescription(kwargs.get('description'))

        if kwargs.get('copyright'):
            self.SetCopyright(kwargs['copyright'])
        else:
            self.SetCopyright('(C) 2016 Joeny')

        if kwargs.get('website'):
            self.SetWebSite(kwargs.get('website'))
        else:
            self.SetWebSite('http://www.google.com/')

        if kwargs.get('license'):
            self.licence = kwargs.get('license')

        self.SetLicence(self.licence)

        if kwargs.get('developer'):
            self.AddDeveloper(kwargs.get('developer'))

        if kwargs.get('writer'):
            self.AddDocWriter(kwargs.get('writer'))

    def show(self):
        """
        Show the about dialog on top.

        :return:
        """
        wx.AboutBox(self)
