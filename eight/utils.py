import sys

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
