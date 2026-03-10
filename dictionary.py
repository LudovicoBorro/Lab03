class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path,'r') as f:
            for line in f.readlines():
                self.dict.append(line.strip())

    def printAll(self):
        for word in self.dict:
            print(word)

    @property
    def dict(self):
        return self._dict