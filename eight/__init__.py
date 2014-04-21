from __future__ import print_function

import sys

# Reminder: Don't put any globals here. They will become unusable once we perform the loader trick below.

class Loader(object):
    _map = dict(str=str,
                bytes=bytes,
                input=input,
                int=int,
                chr=chr,
                range=range,
                filter=filter,
                hex=hex,
                map=map,
                oct=oct,
                zip=zip,
                open=open,
                round=round,
                super=super)

    def __init__(self):
        self._name = __name__
        self._sys = sys
        self.__package__ = __package__
        self.__path__ = __path__
        self.USING_PYTHON2 = True if sys.version_info < (3, 0) else False
        if self.USING_PYTHON2:
            import io, future_builtins
            from future.builtins.newround import newround
            from future.builtins.newsuper import newsuper
            from .utils import python2_input
            self._map = dict(str=unicode,
                             bytes=str,
                             input=python2_input,
                             int=long,
                             chr=unichr,
                             range=xrange,
                             ascii=future_builtins.ascii,
                             filter=future_builtins.filter,
                             hex=future_builtins.hex,
                             map=future_builtins.map,
                             oct=future_builtins.oct,
                             zip=future_builtins.zip,
                             open=io.open,
                             round=newround,
                             super=newsuper)
        else:
            self._map['ascii'] = ascii

        self._map.update(dict(USING_PYTHON2=self.USING_PYTHON2,
                              PY2=self.USING_PYTHON2,
                              PY3=not self.USING_PYTHON2))
        self._manifest = list(self._map)
        self._stdio_wrapped = False

    def __getattr__(self, attr):
        if attr == '__all__':
            if self.USING_PYTHON2:
                return list(self._map)
            else:
                return []
        elif attr == '__package__':
            return self.__package__
        elif attr == '__path__':
            return self.__path__
        elif attr == '__loader__':
            return None
        elif attr in self._manifest:
            return self._map[attr]
        else:
            return self._sys.modules[self._name + '.' + attr]

    def __dir__(self):
        return list(self._map)

    def wrap_stdio(self):
        if self.USING_PYTHON2 and not self._stdio_wrapped:
            import sys, io
            from io import TextIOWrapper
            class StderrTextIOWrapper(TextIOWrapper):
                def write(self, s):
                    if type(s) is unicode:
                        TextIOWrapper.write(self, s)
                    else:
                        TextIOWrapper.write(self, unicode(s, self.encoding))

            original_stdin, original_stdout, original_stderr = sys.stdin, sys.stdout, sys.stderr
            sys.stdin = io.open(sys.stdin.fileno(), encoding=sys.stdin.encoding)
            sys.stdin._original_stream = original_stdin
            sys.stdout = StderrTextIOWrapper(io.FileIO(sys.stdout.fileno(), mode='w'), encoding=sys.stdout.encoding,
                                             line_buffering=True if sys.stdout.isatty() else False)
            sys.stdout._original_stream = original_stdout
            sys.stderr = StderrTextIOWrapper(io.FileIO(sys.stderr.fileno(), mode='w'), encoding=sys.stderr.encoding,
                                             line_buffering=True if sys.stderr.isatty() else False)
            sys.stderr._original_stream = original_stderr
            self._stdio_wrapped = True

from .utils import RedirectingLoader, Move

USING_PYTHON2 = True if sys.version_info < (3, 0) else False

MOVES = {'collections': [Move(new_name='UserList', old_module='UserList', old_name='UserList'),
                         Move(new_name='UserDict', old_module='UserDict', old_name='UserDict'),
                        Move(new_name='UserString', old_module='UserString', old_name='UserString')],
         'itertools': [Move(new_name='filterfalse', old_module='itertools', old_name='ifilterfalse'),
                       Move(new_name='zip_longest', old_module='itertools', old_name='izip_longest')],
         'sys': [Move(new_name='intern', old_module='__builtin__', old_name='intern')]}

RENAMES = {'__builtin__': 'builtins',
           'copy_reg': 'copyreg',
           'Queue': 'queue',
           'ConfigParser': 'configparser',
           'repr': 'reprlib',
           '_winreg': 'winreg',
           'thread': '_thread',
           'dummy_thread': '_dummy_thread'}

for new_module, moves in MOVES.items():
    name = __name__ + '.' + new_module
    sys.modules[name] = RedirectingLoader(new_module)
    for move in moves:
        sys.modules[name]._add_redirect(move)

for old_name, new_name in RENAMES.items():
    sys.modules[__name__ + '.' + new_name] = RedirectingLoader(old_name if USING_PYTHON2 else new_name,
                                                               parent_name=__name__)

loader = Loader()
sys.modules[__name__] = loader
