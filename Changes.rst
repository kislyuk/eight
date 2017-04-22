

Version 0.3.4 (???)
--------------------------
- Fix redirecting module loader to allow eight.__name__ and return correct error for invalid attribute

Version 0.3.3 (2015-11-06)
--------------------------
- Bump python-future dependency

Version 0.3.2 (2015-05-08)
--------------------------
- Import order fix for 0.3.1

Version 0.3.1 (2015-05-08)
--------------------------
- Do not shim the winreg module unless on NT. This avoids incompatibilities with packages such as CherryPy, which try to load all modules seen by the interpreter.
- Do not wrap os.getenv, os.putenv multiple times.

Version 0.3.0 (2014-04-21)
--------------------------
- Add new utility functions to wrap input and output of command-line arguments and environment variables on Python 2.

Version 0.2.0 (2014-04-21)
--------------------------
- Support more renamed packages.
- Eliminate bugs resulting from raw_input ceasing to flush buffers and bind readline when stdio streams are overridden.
- RedirectingLoader now acts as a lazy self-replacing loader when no moves are declared.

Version 0.1.2 (2014-04-04)
--------------------------
- Fix installation of dependencies.

Version 0.1.1 (2014-04-03)
--------------------------
- Add redirecting module loader to allow statements like "from eight.collections import UserDict".

Version 0.1.0 (2014-03-31)
--------------------------
- Begin tracking changes in changelog.
- Depend on the future module for module renames and reorgs.
