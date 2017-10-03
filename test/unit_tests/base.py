import unittest

__author__ = 'Joeny'


class BaseUnitTest(unittest.TestCase):

    def assertTolerance(self, value1, value2, percent=0.01):
        ratio = None

        if value1 is None:
            # self.assertRaises(Exception)
            raise Exception('None value')

        if isinstance(value1, list):
            for x, y in zip(value1, value2):
                if isinstance(x, str) or isinstance(y, str):
                    break

                try:
                    self.assertLess(abs(x-y)/abs(y), percent)
                except ZeroDivisionError as e:
                    self.assertLess(self.difference(x, y), percent)

        else:
            try:
                ratio = abs(value1 - value2)/abs(value2)
                self.assertLess(ratio, percent)

            except ZeroDivisionError as e:
                self.assertLess(self.difference(value1, value2), percent)

    def difference(self, value1, value2):
        return abs(value1 - value2)
