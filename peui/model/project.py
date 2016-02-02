import json

__author__ = 'jbui'


class Project(object):

    def __init__(self, *args, **kwargs):
        self.keys = kwargs.get('keys', {})

