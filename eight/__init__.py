from __future__ import print_function

import sys

USING_PYTHON2 = True if sys.version_info < (3, 0) else False

_moves = {'Queue': 'queue',
          'repr': 'reprlib'}

class Loader(object):
    def __init__(self):
        self._sys = sys
        if USING_PYTHON2:
            self._map = dict(str=unicode,
                             bytes=str,
                             basestring=basestring,
                             input=raw_input,
                             int=long)
            self._manifest = list(self._map.keys())
        else:
            self._map = dict(str=str,
                             bytes=bytes,
                             basestring=(str, bytes),
                             input=input,
                             int=int)
            self._manifest = list(self._map.keys())

    def __getattr__(self, attr):
        print("Get A", attr)
        if attr == '__all__':
            return list(self._map.keys())
        elif attr in self._manifest:
            return self._map[attr]
        else:
            __import__(_moves[attr] if USING_PYTHON2 else attr)
            return self._sys.modules[attr]

loader = Loader()
sys.modules[__name__] = loader
