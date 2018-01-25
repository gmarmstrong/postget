#!/usr/bin/env python3

class MetaPlugin(object):
    """
    Returns a Plugin object.
    """
    def __init__(self, url):
        self.url = url

    def config_urlopts(self, endpoint):
        self.urlopts = self.URLOptions(endpoint)

    class URLOptions(object):
        """
        Returns a ```URLOptions``` object.
        """
        def __init__(self, endpoint):
            self.endpoint = endpoint
            self.payload = {}

        def payload_add(self, key, value):
            self.payload[key] = value

