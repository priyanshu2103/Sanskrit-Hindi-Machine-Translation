from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

url = "https://hindi.webdunia.com/religion/religion/hindu/ramcharitmanas/"

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('ul', {"class": "listStyleNone mp0"})

shloks = ''
bhawarths = ''

for link in content.findAll('a'):
    url2 = url + "/" + link.get('href')
    page2 = requests.get(url2).text
    soup2 = BeautifulSoup(page2, 'html.parser')
    content2 = soup2.find('ul', {"class": "bullet_bow listStyleNone mp0"})
    
    for link2 in content2.findAll('a'):
        url3 = url2.replace("/index.htm", "") + "/" + link2.get('href')
        page3 = requests.get(url3).text
        soup3 = BeautifulSoup(page3, 'html.parser')
        content_shlok = soup3.find_all('div', {"class": "slok"})
        content_bhawarth = soup3.find_all('div', {"class": "bhawarth"})

        for tag in soup3.find_all('strong'):
            tag.replaceWith('')

        for row in content_shlok:
            line = row.text
            line = line.replace('* ', '')
            # print(line)
            shloks += line
            shloks += "\n"

        for row in content_bhawarth:
            line = row.text
            line = line.replace('\t', '')
            # print(line)
            bhawarths += line
            bhawarths += "\n"

with open('ramcharitramanas_shloks.txt', 'w') as file:
    file.write(shloks)

with open('ramcharitramanas_bhawarths.txt', 'w') as file:
    file.write(bhawarths)


