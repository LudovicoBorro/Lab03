import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_dict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        self.multi_dict.load_dicts()
        txtIn = replaceChars(txtIn)
        # Ricerca usando __contains__
        start_time = time.time()
        parole = self.multi_dict.searchWord(txtIn.lower().strip(), language)
        end_time = time.time()
        cont = 0
        print("-----------------------------------------------------------------")
        print("Using contains")
        for word in parole:
            if word.corretta is False:
                print(word)
                cont += 1
        print(f"Nella frase sono stati rilevati {cont} errori!")
        print(f"L'algoritmo ha impiegato {end_time - start_time:.6f} secondi")

        # Ricerca Lineare
        start_time_linear = time.time()
        parole = self.multi_dict.searchWordLinear(txtIn.lower().strip(), language)
        end_time_linear = time.time()
        cont = 0
        print("-----------------------------------------------------------------")
        print("Using Linear search")
        for word in parole:
            if word.corretta is False:
                print(word)
                cont += 1
        print(f"Nella frase sono stati rilevati {cont} errori!")
        print(f"L'algoritmo ha impiegato {end_time_linear - start_time_linear:.6f} secondi")

        # Ricerca dicotomica
        start_time_dic = time.time()
        parole = self.multi_dict.searchWordDichotomic(txtIn.lower().strip(), language)
        end_time_dic = time.time()
        cont = 0
        print("-----------------------------------------------------------------")
        print("Using Dichotomic search")
        for word in parole:
            if word.corretta is False:
                print(word)
                cont += 1
        print(f"Nella frase sono stati rilevati {cont} errori!")
        print(f"L'algoritmo ha impiegato {end_time_dic - start_time_dic:.6f} secondi")

    @classmethod
    def printMenu(cls):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*_{}[]()><#-.!$%^;,/&£€\"?=§°:"
    for c in chars:
        text = text.replace(c, "")
    return text