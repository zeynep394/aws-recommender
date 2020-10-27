import os
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#'https://250films.net/lists/imdb-top-250'  response = requests.get("http:"+image['src'])   'https://www.imdb.com/chart/top/'   'https://www.imdb.com/list/ls068082370/'
html = urlopen('https://www.imdb.com/list/ls041322734/' )
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    #print(image['src']+'\n')
    response = requests.get(image['src'])
    
    filename = image['src'].split('/')[-1]
    imdbresimleri = open(filename, "wb")
    imdbresimleri.write(response.content)
    imdbresimleri.close()

#bir tanesi işe yaradı ama hangisi bilmiyorum bütün resimler indi

#bu kod çalışıyor ve şuan imdbnin kendi sitesinden fotoğrafları indiriyorum