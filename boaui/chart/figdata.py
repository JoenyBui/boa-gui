

class ChartFigure(object):
    """

    """
    def __init__(self, *args, **kwargs):
        self.data = None

        self.axes = []

        self.title = None
        self.xlabel = None
        self.ylabel = None


class ChartData(object):
    """

    """
    def __init__(self, *args, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')

        self.min_x = 0.0
        self.max_x = 0.0
        self.min_y = 0.0
        self.max_y = 0.0

        # Pointer
        self.axes = kwargs.get('axes')
