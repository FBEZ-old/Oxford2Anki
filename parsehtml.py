#! /usr/bin/python

import urllib2
from bs4 import BeautifulSoup
print "Oxford2Anki"
parola = raw_input("Parola:  ")

try:
    response = urllib2.urlopen(r'http://www.oxforddictionaries.com/it/definizione/inglese/'+parola)
    html = response.read()
except urllib2.HTTPError:
    print "Non esiste!"
    exit()


soup = BeautifulSoup(html,'html.parser')
pronuncia = [row.text for row in soup.find_all('div', class_='headpron')]
significato = soup.find_all('span', class_ = 'definition')

print
print
sign_array = []
for s in significato:
    sign = ""
    for link in s:
        try:
            sign = sign+link.text
        except AttributeError:
            sign = sign+link
    sign_array.append(sign)

print "Significato:\n************\n "
for s in sign_array:
    print s
    print
print "\n"+pronuncia[0]
