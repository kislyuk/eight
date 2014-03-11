from __future__ import print_function

import sys

# Reminder: Don't put any globals here. They will become unusable once we perform the loader trick below.

class Loader(object):
    def __init__(self):
        self._sys = sys
        self.__package__ = __package__
        self.__path__ = __path__
        self.USING_PYTHON2 = True if sys.version_info < (3, 0) else False
        if self.USING_PYTHON2:
            self._map = dict(str=unicode,
                             bytes=str,
                             input=raw_input,
                             int=long)
            self._manifest = list(self._map.keys())
            self._moves = {'queue': 'Queue',
                           'reprlib': 'repr'}
        else:
            self._map = dict()
            self._manifest = list(self._map.keys())

    def __getattr__(self, attr):
        if attr == '__all__':
            return list(self._map.keys())
        elif attr == '__package__':
            return self.__package__
        elif attr == '__path__':
            return self.__path__
        elif attr == '__loader__':
            return None
        elif attr in self._manifest:
            return self._map[attr]
        else:
            if self.USING_PYTHON2:
                attr = self._moves[attr]
            __import__(attr)
            return self._sys.modules[attr]

loader = Loader()
sys.modules[__name__] = loader
