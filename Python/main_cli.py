#! /usr/bin/python

import urllib2,urllib,time,os
from EnglishWord import *
import vlc
import EnglishEnglishAnkiNote

print "Oxford2Anki: MAIN"
parola = raw_input("Parola:  ")

perc = r'/home/francesco/Documenti/Anki/Utente 1/collection.media'
dizionario = OxfordDictionary(perc)
dizionario.downloadPronunciation(parola)
ox = dizionario.getWord(parola)
if ox == None:
    print "Non esiste"
    exit()

m = ox.getMeanings()
esci = False
num_significati =4

an = EnglishEnglishAnkiNote.EnglishEnglishAnkiNote()
scelta_significato = 0

while not esci:
    
    for i in range(min(num_significati,len(m))):
        print str(i+1)+") "+m[i].getMeaning()
        print
    scelta_significato = raw_input("Quale significato? ['a' per altre opzioni]")
    if scelta_significato == 'a':
        if num_significati+2 >= len(m):
            print "Sono mostrati tutti i significati!"
        else:
            num_significati = num_significati +2
    elif scelta_significato == 'q':
        esci = True
    else:
        try:
            an.meaning = m[int(scelta_significato)-1].getMeaning()
            esci = True
        except ValueError:
            print "Ripeti"
        

esci = False
scelta_esempio = 0

esempi = m[int(scelta_significato)-1].getExamples()
while not esci:
    for i in range(len(esempi)):
        print str(i+1)+"] "+esempi[i]
    scelta_esempio = raw_input("Quale esempio? [q per uscire]: ")
    try:
            an.example = esempi[int(scelta_esempio)-1]
            esci = True
    except ValueError:
            print "Ripeti"


an.pronunce_written= ox.getPronunciation()
print an.pronunce_written
print m[int(scelta_significato)-1].partOfSpeech
print an.example
print an.meaning
aaa=  an

