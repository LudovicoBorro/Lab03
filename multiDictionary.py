from operator import truediv

import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self.italiano = d.Dictionary()
        self.inglese = d.Dictionary()
        self.spagnolo = d.Dictionary()
        self.parole_frase: list[rw.RichWord] = []

    def load_dicts(self):
        self.italiano.loadDictionary("resources/Italian.txt")
        self.inglese.loadDictionary("resources/English.txt")
        self.spagnolo.loadDictionary("resources/Spanish.txt")

    def printDic(self, language: str):
        if language.lower().strip() == "italiano":
            self.italiano.printAll()
        elif language.lower().strip() == "inglese":
            self.inglese.printAll()
        elif language.lower().strip() == "spagnolo":
            self.spagnolo.printAll()

    def searchWord(self, words, language):
        parole = words.split(" ")
        if language.lower().strip() == "italiano":
            for word in parole:
                word_item = rw.RichWord(word)
                if self.italiano.dict.contains(word):
                    word_item.corretta(True)
                else:
                    word_item.corretta(False)
                self.parole_frase.append(word_item)
        elif language.lower().strip() == "inglese":
            for word in parole:
                word_item = rw.RichWord(word)
                if self.inglese.dict.contains(word):
                    word_item.corretta(True)
                else:
                    word_item.corretta(False)
                self.parole_frase.append(word_item)
        elif language.lower().strip() == "spagnolo":
            for word in parole:
                word_item = rw.RichWord(word)
                if self.spagnolo.dict.contains(word):
                    word_item.corretta(True)
                else:
                    word_item.corretta(False)
                self.parole_frase.append(word_item)
        return self.parole_frase