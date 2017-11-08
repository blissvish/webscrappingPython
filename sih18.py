from urllib.request import urlopen
from bs4 import BeautifulSoup
pagelist = []
#pagelist = ['aicte','council-of-scientific-and-industrial-research-csir','dept-of-commerce-ministry-of-commerce-industry', ]
html = urlopen("https://innovate.mygov.in/sih2018/")
bsObj = BeautifulSoup(html,"lxml")
for div in bsObj.find_all('div', class_ = "thumbnail"):
	pagelist.append(div.find("a")['href'])
#for name in namelist:
#	print(name.get_text())
for pageentry in pagelist:
	html = urlopen(pageentry)
	bsObject = BeautifulSoup(html,"lxml")
	for divis in bsObject.find_all('article', class_="category-listing"):
		print("Problem Statement: ",divis.find("a").get_text())
		print("Description:\n",divis.find('div',class_="description").p.get_text())
		print("\n")
