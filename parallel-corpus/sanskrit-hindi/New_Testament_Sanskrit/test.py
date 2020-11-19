from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
# from BeautifulSoup import BeautifulStoneSoup

# def HTMLEntitiesToUnicode(text):
#     """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
#     text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
#     return text
a=40
b=1

verses = ''
while(a<67):
    try:
        url = "http://www.sanskritbible.in/assets/txt/devanagari/" + str(a) + "0" + str(b).zfill(2) + ".html"
        print(url)
        page = requests.get(url).text

        # page = HTMLEntitiesToUnicode(page)
        soup = BeautifulSoup(page, 'html.parser')
        # print(soup.text)
        content = soup.find('tbody')

        # print(content)
        temp = ''
        i = 0
        count=0
        for verse in content.findAll('td'):
          if i==1:
            temp += verse.text
            temp += '\n'
            count+=1
          i=1-i

        print(count)
        verses += temp
        b+=1
        # verses=verses.encode("utf-8")
        # print(verses)

    except:
        print("sss")
        b=1
        a+=1
    # for row in content_shlok:

with open("test.txt", "w") as f:
  f.write(verses)
