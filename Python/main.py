#! /usr/bin/python

import urllib2,urllib,time,os
from EnglishWord import *
import vlc
import EnglishEnglishAnkiNote

print "Oxford2Anki: MAIN"
parola = raw_input("Parola:  ")

# try:
#     response = urllib2.urlopen(r'http://www.oxforddictionaries.com/it/definition/english/'+parola)
#     html = response.read()
# except urllib2.HTTPError:
#     print "Non esiste!"
#     exit()
perc = r'/home/francesco/Documenti/Anki/Utente 1/collection.media'
dizionario = OxfordDictionary(perc)
dizionario.downloadPronunciation(parola)
ox = dizionario.getWord(parola)
if ox == None:
    print "Non esiste"
    exit()

for m in ox.getNMeanings(3):
    print
    print "*" * (len(m.getMeaning())+4)
    print "* "+m.getMeaning()+" *"
    print "*" * (len(m.getMeaning())+4)
    print m.getPartOfSpeech()
    for i in m.getExamples():
        print "\t"+i
    print
    print m.getSynonyms()
print ox.getPronunciation()


an = EnglishEnglishAnkiNote.EnglishEnglishAnkiNote("trallalero","speek","speak tra","hllo","hippo","test.mp3")
print an

