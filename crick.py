from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.cricbuzz.com")
bsObj = BeautifulSoup(html,"lxml")
namelist = bsObj.findAll("a")
for name in namelist:
	print(name.get_text())
