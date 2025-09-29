from bs4 import BeautifulSoup
import requests

FEGA = "shop.fega.de"
ENPAL = "enpal.pro"
WUERTH = "eshop.wuerth.de"
AMAZON = "www.amazon.de"


def checkWebsiteName(url):
    if FEGA in url:
        return FEGA
    elif ENPAL in url:
        return ENPAL
    elif WUERTH in url:
        return WUERTH
    elif AMAZON in url:
        return AMAZON
    return None


def parseArticleName(website: str, content: BeautifulSoup):
    if website == FEGA:
        return "None"
    if website == ENPAL:
        return content.find("h1", class_="product-title h5").text
    if website == WUERTH:
        return "None"
    if website == AMAZON:
        return "None"
    return None

def parsePrice(website: str, content: BeautifulSoup):
    if website == FEGA:
        return "None"
    if website == ENPAL:
        return content.find('meta', attrs={'property':'og:price:amount'})['content']
    if website == WUERTH:
        return "None"
    if website == AMAZON:
        return "None"
    return None

def parseDescription(website: str, content: BeautifulSoup):
    if website == FEGA:
        return "None"
    if website == ENPAL:
        return content.find('div', attrs={'class':'product-detail-description-text'}).text,
    if website == WUERTH:
        return "None"
    if website == AMAZON:
        return "None"
    return None

def parseDelivery(website: str, content: BeautifulSoup):
    if website == FEGA:
        return "None"
    if website == ENPAL:
       #p-tag
        for p in content.find_all('p'):


    if website == WUERTH:
        return "None"
    if website == AMAZON:
        return "None"
    return None

class WebCrawler:
    # urls = open('websites.txt', 'r').read().split('\n')
    # urls = open('websites.txt', 'r').read().split('\n')
    url = "https://enpal.pro/collections/unterkonstruktionen/products/k2-singlehook-3s-art-nr-2003215-kopie"
    checkWebsiteName(url)
    # for url in urls:
    websiteName = checkWebsiteName(url)
    content = BeautifulSoup(requests.get(url).content, 'html.parser')
    articleName = parseArticleName(websiteName, content)
    price = parsePrice(websiteName, content)
    description = parseDescription(websiteName, content)
    delivery = parseDelivery(websiteName, content)
    print("website",websiteName,"articlename" ,articleName, "price",price,"description", description,"delivery" ,delivery)
