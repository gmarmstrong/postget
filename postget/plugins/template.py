#!/usr/bin/env python3

# plugins/template.py

from postget.libplug import MetaPlugin
import requests

class Plugin(MetaPlugin):
    def __init__(self):
        MetaPlugin.__init__(self, "https://example.org")

    def my_function(self):
        self.config_urlopts("/endpoint")
        return requests.get(self.url)

