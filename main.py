from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen


url = 'https://www.masterofmalt.com/whiskies/hibiki/hibiki-japanese-harmony-whisky/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
uClient = uReq(url)
uClient.close()
page_soup = soup(webpage, 'html.parser')
info = page_soup.find("div", {"id": "whiskyDetailsWrapper", "class" : "expanderBox boxBgr"})

name = info.h2
country = info.a
brand = info.find(itemprop="brand").text
bottler = info.find(itemprop="manufacturer").text
style = info.find(id="ContentPlaceHolder1_ctl00_ctl00_wdStyle").a.text
alcohol = info.find("div", {"id":"ContentPlaceHolder1_ctl00_ctl00_wdAlcohol"}).find("span", {"class": "kv-val"}).text
alcohol = info.find("div", {"id":"ContentPlaceHolder1_ctl00_ctl00_wdVolume"}).find("span", {"class": "kv-val"}).text

