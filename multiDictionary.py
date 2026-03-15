import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self.italiano = d.Dictionary()
        self.inglese = d.Dictionary()
        self.spagnolo = d.Dictionary()
        self.parole_frase: list[rw.RichWord] = []

    def _get_dict(self, language):
        lang = language.lower().strip()
        if lang == "italian": return self.italiano
        if lang == "english": return self.inglese
        if lang == "spanish": return self.spagnolo
        return None

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
        dizionario = self._get_dict(language)
        for word in words.split():
            word_item = rw.RichWord(word.strip())
            word_item.corretta = dizionario.dict.__contains__(word.strip())
            self.parole_frase.append(word_item)
        return self.parole_frase

    def searchWordLinear(self, words, language):
        self.parole_frase = []
        dizionario = self._get_dict(language)
        for word in words.split():
            word_item = rw.RichWord(word.strip())
            word_item.corretta = dizionario.searchLinear(word.strip())
            self.parole_frase.append(word_item)
        return self.parole_frase

    def searchWordDichotomic(self, words, language):
        self.parole_frase = []
        dizionario = self._get_dict(language)
        for word in words.split():
            word_item = rw.RichWord(word.strip())
            word_item.corretta = dizionario.searchDichotomic(word.strip())
            self.parole_frase.append(word_item)
        return self.parole_frase