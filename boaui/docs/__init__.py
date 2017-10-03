import os

from pecdoc.document import DocFile

__author__ = 'Joeny'


class PecDocument(DocFile):
    """
    PEC Document Example

    """
    def __init__(self, template=None, *args, **kwargs):
        """
        PEC Document

        :param template:
        :param args:
        :param kwargs:
        :return:
        """
        if template is None:
            template = os.path.join(os.path.dirname(__file__), 'tpl.docx')

        DocFile.__init__(self, template=template)

    def save(self, file_path):
        """
        Save document to the file path

        :param file_path: word file path
        :return:
        """
        self.write_docx(file_path)


