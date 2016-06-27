import wx

__author__ = 'jbui'


class AboutDialog(wx.AboutDialogInfo):
    """
    About Dialog Info
    """
    licence = """This software is proprietary; it can not be redistribute
    it and/or modify without the express permission of PEC.

    This software is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE."""

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

        self.SetCopyright('(C) 2016 Protection Engineer Consultants')
        self.SetWebSite('http://www.protection-consultants.com/')
        self.SetLicence(self.licence)

        if kwargs.get('developer'):
            self.AddDeveloper(kwargs.get('developer'))

        if kwargs.get('writer'):
            self.AddDocWriter(kwargs.get('writer'))

    def show(self):
        """

        :return:
        """
        wx.AboutBox(self)
