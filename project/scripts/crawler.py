import sys
import urlparse
import urllib2
from bs4 import BeautifulSoup
url ="http://www.ungineering.com/"

urls = [url]
#print urls
visited = [url]

while len(urls) >0:
   
         htmltext =urllib2.urlopen(urls[0]).read()
         soup = BeautifulSoup(htmltext)
        # print soup
         urls.pop(0)

         for tag in soup.findALL('a',href=True):
               tag['href'] = urlparse.urljoin(url,tag['href'])
               print tag['href']
               if url in tag['href'] and tag['href'] not in visited:
                    urls.append(tag['href'])
                    visited.append(tag['href'])


print visited
