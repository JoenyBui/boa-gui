from . import Unit, UNIT_IMPULSE_KEY

FACTOR_IMPULSE_PASCAL_MS = 1.0
FACTOR_IMPULSE_KPA_MS = 1.0/1000.0
FACTOR_IMPULSE_PSI_MS = 1.0/6894.75728

IMPULSE_KEY = {
    'Pa': FACTOR_IMPULSE_PASCAL_MS,
    'psi-ms': FACTOR_IMPULSE_PSI_MS,
    'kPa-ms': FACTOR_IMPULSE_KPA_MS
}


DEFAULT_IMPERIAL_LIST = [
    'psi-ms'
]

DEFAULT_METRIC_LIST = [
    'Pa',
    'kPa-ms',
]


class ImpulseUnit(Unit):
    """
    **TNT Unit**

    """
    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)

        self.key = UNIT_IMPULSE_KEY
        self.table = IMPULSE_KEY

        self.imperial_list = DEFAULT_IMPERIAL_LIST
        self.metric_list = DEFAULT_METRIC_LIST
