# PostGet

**Warning:** This project is still early in development.

## About PostGet

PostGet is a Python library for building web API wrappers which developers can
import as PostGet submodules.

### With PostGet

```python
import requests
from lib import libplug
from plugins import example

plug = example.Plugin()
plug.post_keyval({"key": "val"})
```

### Without PostGet

```python
import requests

def post_keyval(dict):
    request.get("https://example.org" + "/post", dict)

post_keyval({"key": "val"})
```

<!-- TODO # Building and installing PostGet -->

<!-- TODO ## Installing PostGet on Unix/Linux -->

<!-- TODO ## Installing PostGet on macOS -->

<!-- TODO ## Installing PostGet on Windows -->

<!-- TODO # Using PostGet -->

<!-- TODO See
[USER-MANUAL.md](https://github.com/PostGet/blob/master/USER-MANUAL.rst) for
information on using PostGet. -->

<!-- TODO ## Logging and statistics -->

<!-- TODO ## PostGet interfaces -->

<!-- TODO ### Graphical user interface (GUI) -->

<!-- TODO ### Command-line interface (CLI) -->

<!-- TODO ### Application programming interface (API) -->

<!-- TODO ### Preferences (GUI/CLI/API) -->

# Development and maintenance of PostGet

See
[CONTRIBUTING.md](https://github.com/gmarmstrong/postget/blob/master/CONTRIBUTING.md)
for information on PostGet development.
