#!/usr/bin/env python3

# plugins/httpbin.py

from postget.libplug import MetaPlugin
import requests

class Plugin(MetaPlugin):
    """
    Returns an HTTPBin plugin object.
    """
    def __init__(self):
        MetaPlugin.__init__(self, "https://httpbin.org")

    def homepage(self):
        self.config_urlopts("/")
        return requests.get(self.url)

    def ip(self):
        self.config_urlopts("/ip")
        return reqeusts.get(self.url)

    # TODO Optionally allow a dictionary of keys and values
    def get(self, key, val):
        self.config_urlopts("/get")
        self.urlopts.payload_add(key, val)
        return requests.get(self.url)
