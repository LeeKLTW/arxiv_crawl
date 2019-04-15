# encoding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
datetime.now()

html = urlopen('https://arxiv.org/list/cs.CL/recent')

