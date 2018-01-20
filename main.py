#!/usr/bin/env python3

# main.py

import requests
from postget import libplug
from postget.plugins import httpbin

plug = httpbin.Plugin()
plug.homepage()

