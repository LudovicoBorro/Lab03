class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path,'r', encoding="utf-8") as f:
            for line in f.readlines():
                self.dict.append(line.strip())

    def printAll(self):
        for word in self.dict:
            print(word)

    @property
    def dict(self):
        return self._dict

    def searchLinear(self, parola_cercata: str):
        for word in self.dict:
            if parola_cercata.strip() == word:
                return True
        return False

    def searchDichotomic(self, parola_cercata: str):
        parole = self.dict
        while len(parole) > 0:
            if len(parole) == 1:
                if parola_cercata.strip() == parole[0]:
                    return True
                else:
                    return False
            pos_centrale = int(len(parole)/2) - 1
            if parola_cercata.strip() == parole[pos_centrale]:
                return True
            else:
                if parola_cercata.strip().__lt__(parole[pos_centrale]):
                    parole = parole[:pos_centrale]
                else:
                    parole = parole[pos_centrale+1:]
        return False
