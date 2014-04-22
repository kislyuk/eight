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
