#! /usr/bin/python

import urllib2
from bs4 import BeautifulSoup
print "Oxford2Anki"
parola = raw_input("Parola: ")

try:
    response = urllib2.urlopen(r'http://www.oxforddictionaries.com/it/definizione/inglese/'+parola)
    html = response.read()
except urllib2.HTTPError:
    print "Non esiste!"
    exit()


soup = BeautifulSoup(html,'html.parser')
pronuncia = [row.text for row in soup.find_all('div', class_='headpron')]
significato = soup.find_all('span', class_ = 'definition')
print significato[0]


print pronuncia[0]
# div_pronuncia = soup.find("div", { "class" : "headpron" })
# print div_pronuncia
# div_significato = soup.find("div", { "class" : "senses" })
# print div_significato

# for link in soup.find_all('a'):
#     print(link.get('href'))
