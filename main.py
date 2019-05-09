from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen


urls = ("https://www.masterofmalt.com/whiskies/hibiki/hibiki-japanese-harmony-whisky/",
    "https://www.masterofmalt.com/whiskies/yamazaki/yamazaki-12-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-whisky-from-the-barrel-whisky/",
    "https://www.masterofmalt.com/whiskies/hakushu/the-hakushu-single-malt-whisky-distillers-reserve-whisky/",
    "https://www.masterofmalt.com/whiskies/suntory/suntory-toki-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-coffey-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-coffey-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/karuizawa/karuizawa-19-year-old-that-boutiquey-whisky-company-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-taketsuru-pure-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/the-nikka-12-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/yoichi/yoichi-single-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/chita/the-chita-suntory-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-coffey-grain-whisky-70cl/",
    "https://www.masterofmalt.com/whiskies/miyagikyo/miyagikyo-single-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/mars/mars-komagatake-shinanotanpopo-nature-of-shinshu-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka-all-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-days-whisky/",
    "https://www.masterofmalt.com/whiskies/kurayoshi/the-kurayoshi-18-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/kamiki/kamiki-whisky/",
    "https://www.masterofmalt.com/whiskies/miyashita/okayama-single-malt-whisky/",
    "https://www.masterofmalt.com/whiskies/shinshu/mars-maltage-cosmo-whisky/",
    "https://www.masterofmalt.com/whiskies/kurayoshi/the-kurayoshi-8-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/togouchi/togouchi-18-year-old-43-8-whisky/",
    "https://www.masterofmalt.com/whiskies/kurayoshi/the-kurayoshi-12-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/golden-horse/golden-horse-musashi-whisky/"
    )

file_name = "webscrape.csv"
f = open(file_name, "w")

headers = "name, country, brand, bottler, style, alcohol, volume\n"

f.write(headers)

for url in urls:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    uClient = uReq(url)
    uClient.close()
    page_soup = soup(webpage, 'html.parser')
    info = page_soup.find("div", {"id": "whiskyDetailsWrapper", "class" : "expanderBox boxBgr"})
    info = page_soup.find("div", {"id": "whiskyDetailsWrapper", "class" : "expanderBox boxBgr"})
    name = page_soup.h1.text
    country = info.find("div", {"id":"ContentPlaceHolder1_ctl00_ctl00_wdCountry"}).find("span", {"class": "kv-val"}).text
    brand = info.find(itemprop="brand").text
    bottler = info.find(itemprop="manufacturer").text
    style = info.find(id="ContentPlaceHolder1_ctl00_ctl00_wdStyle").find("span", {"class": "kv-val"}).text
    alcohol = info.find("div", {"id":"ContentPlaceHolder1_ctl00_ctl00_wdAlcohol"}).find("span", {"class": "kv-val"}).text
    volume = info.find("div", {"id":"ContentPlaceHolder1_ctl00_ctl00_wdVolume"}).find("span", {"class": "kv-val"}).text
    f.write(name + "," + country + "," + brand + "," + bottler + "," + style + "," + alcohol + "," + volume + "\n")

f.close()