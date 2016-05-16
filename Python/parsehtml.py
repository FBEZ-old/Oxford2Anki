#! /usr/bin/python

import urllib2,urllib,time,os
import vlc
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
significato = soup.find_all('div', class_ = 'senseInnerWrapper')

for s in significato:
    try:
        print "* "+s.find_all('span',class_= 'definition')[0].text
        print
        i = 0
        for example in s.find_all('span',class_='exampleGroup exGrBreak'):
            i=i+1
            print str(i)+")"+ example.find_all('em',class_='example')[0].text
        print "------------------------------------"
        print
    except IndexError:
        print
print
print

print "\n"+pronuncia[0]


urllib.urlretrieve ("https://ssl.gstatic.com/dictionary/static/sounds/de/0/"+parola+".mp3", parola+".mp3")
instance = vlc.Instance()

player = instance.media_player_new()
media = instance.media_new(parola+'.mp3')
player.set_media(media)
player.play()
time.sleep(3)
os.remove(parola+".mp3")
