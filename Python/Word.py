from abc import ABCMeta, abstractmethod

class Meaning:
    __metaclass__= ABCMeta
    @abstractmethod
    def __init__(self,data):
        """Parse the code containt the data corresponding to one single meaning"""
        pass
    @abstractmethod
    def getMeaning(self):
        pass
    @abstractmethod
    def getSynonym(self):
        pass
    @abstractmethod
    def getExamples(self):
        pass
    @abstractmethod
    def getPartOfSpeech(self):
        pass

class Word:
    """Parse data corresponding to a Word, works with array of Meanings """
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self,data):
        pass
    @abstractmethod
    def getMeanings(self):
        pass
    
