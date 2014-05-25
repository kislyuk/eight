#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import os, sys, unittest, collections, copy, re, io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import eight
from eight import *

class TestEight(unittest.TestCase):
    def test_basic_eight_statements(self):
        from eight import queue, builtins, reprlib
        from eight.configparser import ConfigParser
        from eight import collections
        from eight.collections import UserList, deque
        q = collections.UserList()
        self.assertEqual(type(map(str, range(5))), map)
        self.assertEqual(open, io.open)

    def test_long_int(self):
        pass

    def test_stdio_wrappers(self):
        eight.wrap_stdio()
        self.assertTrue(hasattr(sys.stdin, 'buffer'))
        sys.stdout.write(u'test')
        sys.stderr.write(u'test')
        sys.stdout.buffer.write(b'test')
        sys.stderr.buffer.write(b'test')
        if eight.USING_PYTHON2:
            sys.stdin = sys.stdin.detach()
            sys.stdout = sys.stdout.detach()
            sys.stderr = sys.stderr.detach()

    def test_unicode_str(self):
        if eight.USING_PYTHON2:
            exec("s = b'конструкция'")
        else:
            s = bytes("конструкция", encoding="utf-8")
        self.assertEqual(str(s, encoding="utf-8"), u"конструкция")

    def test_os_environ_io_wrappers(self):
        eight.wrap_os_environ_io()
        os.environ["переменная"] = "значение"
        self.assertEqual(os.environ["переменная"], "значение")

    def test_decode_command_line_args(self):
        pass

if __name__ == '__main__':
    unittest.main()
