eight: Python 2 to the power of 3
=================================
Eight is a Python module that provides a minimalist compatibility layer between Python 3 and 2. Eight lets you write
code for Python 3.3+ while providing limited compatibility with Python 2.7 with no code changes.  Eight is inspired by
`six <https://pythonhosted.org/six/>`_, `nine <https://github.com/nandoflorestan/nine>`_, and `python-future
<https://github.com/PythonCharmers/python-future>`_, but provides better internationalization (i18n) support, is more
lightweight, easier to use, and unambiguously biased toward Python 3 code: if you remove eight from your code, it will
continue to function exactly as it did with eight on Python 3.

To write code for Python 3 that is portable to Python 2, you may also want to read Armin Ronacher's excellent `Python 3
porting guide <http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/>`_, as well as the official
`porting guide <http://docs.python.org/3/howto/pyporting.html>`_.

Writing ``from eight import *`` in your code is a no-op in Python 3. In Python 2, it binds a bunch of Python 3 names to
their Python 2 equivalents. Also, if you need to import a module or module member that was renamed in Python 3, writing
``from eight import <module>`` will do the right thing (equivalent to ``import <module>`` on Python 3 and ``import
<old_name> as <module>`` on Python 2). Finally, eight can optionally wrap your standard streams and environment variable
I/O to use text, not bytes (see below).

Installation
------------
::

    pip install eight

Synopsis
--------

.. code-block:: python

    from eight import *
    from eight import queue
    from eight.collections import UserList, deque

If you use ``print``, division, non-ASCII literals, or relative imports, you should also add this `future import
<http://docs.python.org/3/library/__future__.html>`_ at the top of each source file:

.. code-block:: python

    from __future__ import (print_function, division, unicode_literals, absolute_import)

Wrapping stdio
--------------
Eight provides wrappers for ``sys.stdin``, ``sys.stdout``, and ``sys.stderr`` to make them (and methods that use them)
behave like they do on Python 3. Specifically, in Python 3 these streams accept text data, and their ``.buffer`` attributes
refer to the underlying streams that accept bytes. Eight uses the `io <http://docs.python.org/2/library/io.html>`_ module
to do the same for you, but subclasses the TextIOWrapper class for ``sys.stdout`` and ``sys.stderr`` to coerce non-unicode
input to unicode on Python 2 (otherwise, because of the Python 2 semantics, things like exception printing cease to work).

To enable stdio wrapping, use the following:

.. code-block:: python

    import eight
    eight.wrap_stdio()

To revert the effects of this on any of the streams, use the detach method, e.g. ``sys.stdin = sys.stdin.detach()`` (but
remember to condition this on ``eight.USING_PYTHON2``). See the `io module documentation
<http://docs.python.org/2/library/io.html>`_ for more information.

Decoding command-line arguments
-------------------------------
Eight provides a utility function to decode the contents of ``sys.argv`` on Python 2 (as Python 3 does). It uses
``sys.stdin.encoding`` as the encoding to do so:

.. code-block:: python

    import eight
    eight.decode_command_line_args()

The call to ``decode_command_line_args()`` replaces ``sys.argv`` with its decoded contents and returns the new contents.
On Python 3, the call is a no-op (it returns ``sys.argv`` and leaves it intact).

Wrapping environment variable getters and setters
-------------------------------------------------
Eight provides utility wrappers to help bring Python 2 environment variable access and assignment in line with Python
3: encode the input to ``os.putenv`` (which is used for statements like ``os.environ[x] = y``) and decode the output of
``os.getenv`` (used for ``x = os.environ[y]``). Use ``wrap_os_environ_io()`` to monkey-patch these wrappers into the
``os`` module:

.. code-block:: python

    import eight
    eight.wrap_os_environ_io()

On Python 3, the call is a no-op.

Selecting from the buffet
-------------------------
You can see what ``from eight import *`` will do by running `IPython <https://github.com/ipython/ipython>`_ and typing
``import eight``, then ``eight.<TAB>``. Here is a full list of what's available:

* ``ascii``
* ``bytes``
* ``chr``
* ``filter``
* ``hex``
* ``input``
* ``int``
* ``map``
* ``oct``
* ``open``
* ``range``
* ``round``
* ``str``
* ``super``
* ``zip``

You can import these symbols by listing them explicitly. If for any reason you see an issue with importing them all (which
is recommended), you can of course import a subset.

In addition to names imported by ``from eight import *``, the following modules are available and should be imported by
name using ``from eight import <name>`` when needed:

* ``queue`` (old name: ``Queue``)
* ``builtins`` (old name: ``__builtin__``)
* ``copyreg`` (old name: ``copy_reg``)
* ``configparser`` (old name: ``ConfigParser``)
* ``reprlib`` (old name: ``repr``)
* ``winreg`` (old name: ``_winreg``)
* ``_thread`` (old name: ``thread``)
* ``_dummy_thread`` (old name: ``dummy_thread``)

The following modules have attributes which resided elsewhere in Python 2: TODO

Acknowledgments
---------------
`Python-future <https://github.com/PythonCharmers/python-future>`_ for doing a bunch of heavy lifting on backports of
Python 3 features.

Links
-----
* `Project home page (GitHub) <https://github.com/kislyuk/eight>`_
* `Documentation (Read the Docs) <https://eight.readthedocs.io/en/latest/>`_
* `Package distribution (PyPI) <https://pypi.python.org/pypi/eight>`_

Bugs
~~~~
Please report bugs, issues, feature requests, etc. on `GitHub <https://github.com/kislyuk/eight/issues>`_.

License
-------
Licensed under the terms of the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.

.. image:: https://img.shields.io/travis/kislyuk/eight.svg
        :target: https://travis-ci.org/kislyuk/eight
.. image:: https://codecov.io/github/kislyuk/eight/coverage.svg?branch=master
        :target: https://codecov.io/github/kislyuk/eight?branch=master
.. image:: https://img.shields.io/pypi/v/eight.svg
        :target: https://pypi.python.org/pypi/eight
.. image:: https://img.shields.io/pypi/l/eight.svg
        :target: https://pypi.python.org/pypi/eight
.. image:: https://readthedocs.org/projects/eight/badge/?version=latest
        :target: https://eight.readthedocs.io/
