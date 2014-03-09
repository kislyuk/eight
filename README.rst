eight: Python 2 to the power of 3
=================================
Eight is a Python module that provides a minimalist compatibility layer between Python 3 and 2. Eight lets you write
code for Python 3.3+ while providing limited compatibility with Python 2.7 with no code changes.  Eight is inspired by
`six <https://pythonhosted.org/six/>`_ and `nine <https://github.com/nandoflorestan/nine>`_, but is more lightweight,
easier to use, and unambiguously biased toward Python 3 code: if you remove eight from your code, it will continue to
function exactly as it did with eight on Python 3.

To write code for Python 3 that is portable to Python 2, you may also want to read Armin Ronacher's excellent `Python 3
porting guide <http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/>`_.

Writing ``from eight import *`` in your code is a no-op in Python 3. In Python 2, it binds a bunch of Python 3 names to
their Python 2 equivalents. Also, if you need to import a module that was renamed in Python 3, writing ``from eight
import <module>`` will do the right thing (equivalent to ``import <module>`` on Python 3 and ``import <old_name> as
<module>`` on Python 2.

Installation
------------
::

    pip install eight

Synopsis
--------

.. code-block:: python

    from eight import *
    from eight import queue

Links
-----
* `Project home page (GitHub) <https://github.com/kislyuk/eight>`_
* `Documentation (Read the Docs) <https://eight.readthedocs.org/en/latest/>`_
* `Package distribution (New PyPI) <https://preview-pypi.python.org/project/eight/>`_ `(Old PyPI) <http://pypi.python.org/pypi/eight>`_

Bugs
~~~~
Please report bugs, issues, feature requests, etc. on `GitHub <https://github.com/kislyuk/eight/issues>`_.

License
-------
Licensed under the terms of the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.

.. image:: https://travis-ci.org/kislyuk/eight.png
        :target: https://travis-ci.org/kislyuk/eight
.. image:: https://coveralls.io/repos/kislyuk/eight/badge.png?branch=master
        :target: https://coveralls.io/r/kislyuk/eight?branch=master
.. image:: https://pypip.in/v/eight/badge.png
        :target: https://crate.io/packages/eight
.. image:: https://pypip.in/d/eight/badge.png
        :target: https://crate.io/packages/eight
