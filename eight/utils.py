from __future__ import print_function

import sys
from collections import namedtuple

USING_PYTHON2 = True if sys.version_info < (3, 0) else False

def python2_input(prompt=None):
    try:
        cur_stdin, cur_stdout = sys.stdin, sys.stdout
        if hasattr(sys.stdin, '_original_stream'):
            sys.stdin = sys.stdin._original_stream
        if hasattr(sys.stdout, '_original_stream'):
            sys.stdout = sys.stdout._original_stream
        encoded_prompt = prompt.encode(getattr(sys.stdout, 'encoding', 'utf-8'))
        return raw_input(encoded_prompt).decode(getattr(sys.stdin, 'encoding', 'utf-8')) # noqa
    finally:
        sys.stdin, sys.stdout = cur_stdin, cur_stdout

Move = namedtuple('Move', ('new_name', 'old_module', 'old_name'))

class RedirectingLoader(object):
    def __init__(self, name, parent_name='eight'):
        self._name = name
        self._parent_name = parent_name
        self._moves = {}
        self._old_module = None
        self._module = None

    def _add_redirect(self, move):
        self._moves[move.new_name] = move

    def __getattr__(self, attr):
        if USING_PYTHON2 and attr in self._moves:
            move = self._moves[attr]
            if self._old_module is None:
                self._old_module = __import__(move.old_module)
            return getattr(self._old_module, move.old_name)
        else:
            if self._module is None:
                self._module = __import__(self._name)
            if len(self._moves) == 0:
                sys.modules[self._parent_name + '.' + self._name] = sys.modules[self._name]
            return getattr(self._module, attr)
