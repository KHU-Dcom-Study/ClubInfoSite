import requests
import json
import re
from json import dumps, loads, JSONEncoder, JSONDecoder
import time
from datetime import datetime
import datetime

now = datetime.datetime.now()
def strToInt(str):
    result = 0
    result = int(str)
    return result




from bs4 import BeautifulSoup
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

URL = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=21"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')




bbs = soup.select("#container > div.content-area > div.content-wrap > div.content")


titles = bbs[0].findAll("div", {"class": "tit"})
organs = bbs[0].findAll("div", {"class": "organ"})
remaindate = bbs[0].findAll("div", {"class": "day"})


challenge = []
for i in range(1, len(titles)):
    
    
    title = ''.join(titles[i].text.split())
    organ = ''.join(organs[i].text.split())
    remdate = ''.join(remaindate[i].text.split())
    
    S = remdate 
    numbers = re.findall("\d+",S)
    endDate = now + datetime.timedelta(days=int(numbers[0])) 

    j2 = {"title": title,"organism":organ,"Date":str(endDate)}
    challenge.append(j2)
print(challenge)
print(json.dumps({"challenge":challenge}, indent=2))
    
#json.dumps(j2)


