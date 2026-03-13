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
        if language.lower().strip() == "italian":
            self.italiano.printAll()
        elif language.lower().strip() == "english":
            self.inglese.printAll()
        elif language.lower().strip() == "spanish":
            self.spagnolo.printAll()

    def searchWord(self, words, language):
        self.parole_frase = []
        parole = words.split(" ")
        if language.lower().strip() == "italian":
            for word in parole:
                word_item = rw.RichWord(word.strip())
                if word_item is None:
                    print(f"Attenzione l'item di word è None: {word}")
                if self.italiano.dict.__contains__(word):
                    word_item.corretta = True
                else:
                    word_item.corretta = False
                self.parole_frase.append(word_item)
        elif language.lower().strip() == "english":
            for word in parole:
                word_item = rw.RichWord(word)
                if self.inglese.dict.__contains__(word):
                    word_item.corretta = True
                else:
                    word_item.corretta = False
                self.parole_frase.append(word_item)
        elif language.lower().strip() == "spanish":
            for word in parole:
                word_item = rw.RichWord(word)
                if self.spagnolo.dict.__contains__(word):
                    word_item.corretta = True
                else:
                    word_item.corretta = False
                self.parole_frase.append(word_item)
        return self.parole_frase