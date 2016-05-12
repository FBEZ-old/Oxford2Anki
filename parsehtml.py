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
#print significato[0].find_all('a', class_='w translation')
print
print
sign = ""
for link in significato[1]:
    try:
        sign = sign+link.text
    except AttributeError:
        sign = sign+link
print "Significato:\n************\n "+sign
print "\n"+pronuncia[0]
