import sys
from collections import namedtuple

def input_with_unbuffered_stdout(prompt=None):
    class Unbuffered(object):
        def __init__(self, stream):
            self.stream = stream

        def write(self, data):
            self.stream.write(data)
            self.stream.flush()

        def __getattr__(self, attr):
            return getattr(self.stream, attr)

    orig_stdout = sys.stdout
    try:
        sys.stdout = Unbuffered(sys.stdout)
        result = raw_input(prompt)
    finally:
        sys.stdout = orig_stdout
    return result

Move = namedtuple('Move', ('old_module', 'old_name'))

class RedirectingLoader(object):
    def __init__(self):
        self._moves = {}
        self._old_module = None
        self._module = None

    def add(self, new_module, new_name, old_module, old_name):
        print "Adding", new_module, new_name, old_module, old_name
        self._name = new_module
        self._moves[new_name] = Move(old_module, old_name)

    def __getattr__(self, attr):
        if attr in self._moves:
            move = self._moves[attr]
            if self._old_module is None:
                self._old_module = __import__(move.old_module)
            return getattr(self._old_module, move.old_name)
        else:
            if self._module is None:
                self._module = __import__(self._name)
            return getattr(self._module, attr)
