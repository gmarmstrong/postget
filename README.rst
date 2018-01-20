=======
PostGet
=======

About PostGet
=============

PostGet is a Python library and plugin repository for interfacing with web APIs. By placing HTTP request methods behind a layer of abstraction, PostGet plugins allow the developer to directly interface with web API functions with little-to-no added overhead.

With PostGet
------------
.. code-block:: python

    import requests
    from lib import libplug
    from plugins import example

    plug = example.Plugin()
    plug.post_keyval({"key": "val"})

Without PostGet
---------------
.. code-block:: python

    import requests

    def post_keyval():
        request.get("https://example.org" + "/post", {"key": "val"})

    post_keyval()

.. TODO Building and installing PostGet
..      ===============================
.. TODO Installing PostGet on Unix/Linux
..      --------------------------------
.. TODO Installing PostGet on macOS
..      ---------------------------
.. TODO Installing PostGet on Windows
..      -----------------------------

.. TODO Using PostGet
..      =============
.. TODO See `USER-MANUAL.rst`_ for information on using PostGet.
..
.. TODO .. _`USER-MANUAL.rst`: https://github.com/PostGet/blob/master/USER-MANUAL.rst
..
.. TODO Logging and statistics
..      ----------------------
..
.. TODO PostGet interfaces
..      ------------------
.. TODO Graphical user interface (GUI)
..      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. TODO Command-line interface (CLI)
..      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. TODO Application programming interface (API)
..      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. TODO Preferences (GUI/CLI/API)
..      ~~~~~~~~~~~~~~~~~~~~~~~~~

Development and maintenance of PostGet
======================================
See `CONTRIBUTING.rst`_ for information on PostGet development.

.. _`CONTRIBUTING.rst`: https://github.com/gmarmstrong/PostGet/blob/master/CONTRIBUTING.rst
