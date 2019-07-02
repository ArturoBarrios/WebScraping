from BeautifulSoup import BeautifulSoup
import urllib2
import re
import ssl
import requests
from lxml import html

POST_LOGIN_URL ="https://drop.com/?loggedout#login"
REQUEST_URL = "https://drop.com/my-communities/drops"

payload = {
    'username': "arturobarrios357@gmail.com",
    'password': "Ruforufo4$"
}
with requests.Session() as session:
    post = session.post(POST_LOGIN_URL,data=payload)
    print(post)
    r = session.get(REQUEST_URL)
    #print(r.text)
    soup = BeautifulSoup(str(r))
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        print link.get('href')
    links = re.findall('.//alcontains(@class,"item__link")]/@href,str(r))
    # print(links)
# context = ssl._create_unverified_context()
# html_page = urllib2.urlopen("https://drop.com/buy/",context = context)
