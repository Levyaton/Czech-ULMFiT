
from bs4 import BeautifulSoup

import threading

from requests.packages.urllib3.packages.six.moves import urllib


def getUrls(urls, pageCount):
    opener = urllib.request.FancyURLopener({})
    for page in range(1, pageCount + 1,1):
        url = "https://www.sexypovidky.cz/vsechny_povidky/?page=" + str(page)
        f = opener.open(url)
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all("div", class_='perex cf')
        for link in links:
            cf = None
            counter = 0
            for child in link.children:
                if counter == 1:
                    cf = child
                else:
                    counter = counter + 1
            perex_title = None
            for child in cf.children:
                perex_title = child
                break
            h2 = None
            for child in perex_title.children:
                h2 = child
                break
            a = None
            for child in h2.children:
                a = child
                break
            urls.append(a["href"])


if __name__ == '__main__':
    urls = []
    getUrls(urls,82)
    print(urls)

