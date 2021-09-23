import codecs
from threading import Thread

from bs4 import BeautifulSoup
import requests
import _thread as thread
import html2text


def downloadPage(url,title):
    print(title)
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    content = soup.find_all("div", {"class" : "entry-content"})[0]
    text = content.find_all("p")
    text_parts = content.findAll(text=True)
    for part in text_parts:
        if "(function () {" in part or part == " nativni reklama " or "AI CONTENT END " in part:
            text_parts.remove(part)
    text = ''.join(text_parts)
    file = codecs.open("Files/"+title+".txt", "w", "utf-8")
    file.write(text)
    file.close()

def processPage(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    articles = soup.find_all("article")

    for article in articles:
        h2 = article.contents[1]
        a = h2.contents[1]
        story = a["href"]
        title = story.replace("https://vase-eroticke-povidky.cz/","").replace("/","")
        Thread(target=downloadPage,args=(story,title,)).start()
def getUrls():
    url = "https://vase-eroticke-povidky.cz/"
    pageCount = 234
    maxThreadCount = 4
    currentCount = 0
    for pageNum in range(1,pageCount+1,1):
        thread = None
        if currentCount == maxThreadCount:
            thread.join()
            thread = Thread(target=processPage,args=(url + "/page/" + str(pageNum) + "/",))
            thread.start()
        else:
            Thread(target=processPage,args=(url + "/page/" + str(pageNum) + "/",)).start()



if __name__ == '__main__':
    getUrls()

