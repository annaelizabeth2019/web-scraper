from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen


urls = ( "https://www.masterofmalt.com/whiskies/hakushu-10-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-pure-malt-spice-rack-set-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka-whisky-from-the-barrel-gift-pack/",
    "https://www.masterofmalt.com/whiskies/yamazakura/963-malt-and-grain-whisky/",
    "https://www.masterofmalt.com/whiskies/mars/mars-komagatake-2014-bottled-2017-cask-1782-whisky/",
    "https://www.masterofmalt.com/whiskies/karuizawa/karuizawa-1984-bottled-2013-cask-3663-whisky/",
    "https://www.masterofmalt.com/whiskies/hibiki/hibiki-35-year-old-by-tokuda-yasokichi-iii-whisky/",
    "https://www.masterofmalt.com/whiskies/hibiki/suntory-hibiki-blended-whisky/",
    "https://www.masterofmalt.com/whiskies/suntory/suntory-whisky-white-192cl-1990s-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/yoichi-and-miyagikyo-rum-cask-finish-set-whisky/",
    "https://www.masterofmalt.com/whiskies/hibiki/hibiki-japanese-harmony-masters-select-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/nikka-taketsuru-on-the-road-set-whisky/",
    "https://www.masterofmalt.com/whiskies/mars/mars-komagatake-30-year-old-1986-whisky/",
    "https://www.masterofmalt.com/whiskies/mars/mars-shinshu-2013-bottled-2016-cask-1664-number-one-drinks-company-10th-anniversary/",
    "https://www.masterofmalt.com/whiskies/suntory/suntory-kakushiro-white-label-whisky/",
    "https://www.masterofmalt.com/whiskies/chichibu/chichibu-the-peated-2012-bottled-2016-whisky/",
    "https://www.masterofmalt.com/whiskies/karuizawa/karuizawa-33-year-old-1981-cask-136-whisky/",
    "https://www.masterofmalt.com/whiskies/suntory/suntory-kakubin-black-label-whisky/",
    "https://www.masterofmalt.com/whiskies/hibiki/hibiki-12-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/hakushu/suntory-1981-kioke-shikomi-whisky/",
    "https://www.masterofmalt.com/whiskies/hanyu/ichiros-malt-hanyu-15-year-old-whisky/",
    "https://www.masterofmalt.com/whiskies/mars/mars-komagatake-tsunuki-aging-whisky/",
    "https://www.masterofmalt.com/whiskies/nikka/super-nikka-revival-limited-edition-whisky/",
    "https://www.masterofmalt.com/whiskies/karuizawa/karuizawa-1981-bottled-2011-cask-6256-whisky/",
    "https://www.masterofmalt.com/whiskies/hanyu/hanyu-1990-bottled-2007-cask-9511-whisky/"
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