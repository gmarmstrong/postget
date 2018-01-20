# routeshout

from postget.libplug import MetaPlugin
import requests

api_key = ""

class Plugin(MetaPlugin):
    def __init__(self):
        MetaPlugin.__init__(self, "http://api.routeshout.com/v1")

    def list_agencies(self):
        self.config_urlopts("/rs.agencies.getList")
        self.urlopts.payload_add("key", api_key)
        return requests.get(self.url)
