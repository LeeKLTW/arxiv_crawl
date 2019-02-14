# encoding: utf-8
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen('https://arxiv.org/list/cs.CL/recent')
html = urlopen('https://redis.io/documentation')

dir(html)
html.read()