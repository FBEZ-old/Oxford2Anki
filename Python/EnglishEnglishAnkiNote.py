class EnglishEnglishAnkiNote:
    def __init__(self,word="",pronunce_written="",meaning="",remark="",example="",pronunce_sound=""):
        if type(word) is list:
            self.word = "/".join(word)
        else:
            self.word = word
        self.pronunce_written = pronunce_written
        self.meaning = meaning
        self.remark = remark
        self.example = example
        self.pronunce_sound = pronunce_sound
    def __str__(self):
        return self.word+";"+str(self.pronunce_written)+";"+self.meaning+";"+self.remark+";"+self.example+";"+"[sound:"+self.pronunce_sound+"]"
