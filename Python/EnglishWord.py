from Word import *
from bs4 import BeautifulSoup
import urllib2,urllib,time,os

class OxfordDictionary:
    def __init__(self,folder = ""):
        self.url = r'http://www.oxforddictionaries.com/it/definition/english/'
        self.url_mp3 = r'https://ssl.gstatic.com/dictionary/static/sounds/de/0/'
        self.folder = folder
    def getWord(self,word):
        ind = self.url+word
        try:
            response = urllib2.urlopen(r'http://www.oxforddictionaries.com/it/definition/english/'+word)
            html = response.read()
            return EnglishOxfordWord(html)
        except urllib2.HTTPError:
            return None
    def downloadPronunciation(self,word):
        print self.url_mp3+word+".mp3"
        urllib.urlretrieve (self.url_mp3+word+".mp3", word+".mp3")
        if self.folder != "":
            os.rename(word+".mp3",self.folder+"/"+word+".mp3")
        
class EnglishOxfordMeaning:
    def __init__(self,data,POS):
        self.meaning = data.find_all('span',class_= 'definition')[0].text[:-1]
        try:
            wordform = "("+data.find_all('strong',class_='wordForm')[0].text+")"
        except IndexError:
            wordform = ""
        
        self.meaning = wordform+self.meaning 
        self.examples = []
        for example in data.find_all('span',class_='exampleGroup exGrBreak'):
            for e in example.find_all('em',class_='example'):
                self.examples.append(e.text)
        #Ulteriori esempi
        for example in data.find_all('li',class_='sentence'):
            self.examples.append(example.text)
        self.partOfSpeech = POS
        self.synonyms = []
        for syn in data.find_all('a',class_='syn'):
            self.synonyms.append(syn.text)
    def getMeaning(self):
        return self.meaning
    def getSynonyms(self):
        return self.synonyms
    def getExamples(self):
        return self.examples
    def getPartOfSpeech(self):
        return self.partOfSpeech
    
class EnglishOxfordWord:
    def __init__(self,data):
        soup = BeautifulSoup(data,'html.parser')
        pron = [row.text for row in soup.find_all('div', class_='headpron')]
        self.pronunciation = pron[0][11:]
        self.meanings = []
        for sign in soup.find_all('section',class_='se1 senseGroup'):
            POS = sign.find_all('span',class_='partOfSpeech')[0].text
            significato = sign.find_all('div', class_ = 'senseInnerWrapper')
        
            for s in significato:
                try:
                    self.meanings.append(EnglishOxfordMeaning(s,POS))
                except IndexError:
                    pass
    def getMeanings(self):
        return self.meanings
    def getPronunciation(self):
        return self.pronunciation
    def getNMeanings(self,N):
        return self.meanings[0:N]
