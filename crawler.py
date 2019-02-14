# encoding: utf-8
from urllib.request import urlopen
# This is for https
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('https://arxiv.org/list/cs.CL/recent')





