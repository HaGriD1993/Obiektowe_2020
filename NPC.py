import random
#import time


class NPC:
    def __init__(self, imie, wiek, specjanosc):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc

    def info(self):
        return "Witaj nazywam się: " + self.imie, "pracuje jako: "+self.specjanosc

    def zbieranie(self):
        lista_ziol = []
        ziolo_1 = random.randint(0, 1)
        ziolo_2 = random.randint(0, 1)

        if ziolo_1 == 1 :
            lista_ziol.append("Bagienne źiele")
            lista_ziol.append("Niebieski bez")
            print("Udało mi sie zebrać następujące rośliny: ", lista_ziol)
        elif ziolo_2 == 1 :
            lista_ziol.append("Kulczyba wronie oko")
            lista_ziol.append("Trójkolorowe źiele")
            print("Udało mi sie zebrać następujące rośliny: ", lista_ziol)
        else:
            print("Nie udało mi sie nic zebrać. Mój plecak jest pusty.")




obiekt_2 = NPC ("Bogdan", 73, "Źielarz")

print(obiekt_2.info())
print(obiekt_2.zbieranie())


