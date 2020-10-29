import random
import time


class NPC:
    def __init__(self, imie, wiek, specjanosc):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc

    def info(self):
        return "Witaj nazywam się: " + self.imie, "pracuje jako: " + self.specjanosc

    def zbieranie(self):
        print("Potrzebuje kilku roślin, wybierz gdzie mam się udać: "
              "\n1: Las "
              "\n2: Bagna")
        zbieraj = input("Wybierz ___ : ")

        if zbieraj == 1:
            print("Ide do lasu. ")
            time.sleep(4)
        elif zbieraj == 2:
            print("Ide na bagna. ")
            time.sleep(6)
        lista_ziol = []
        ziolo_1 = random.randint(0, 1)
        ziolo_2 = random.randint(0, 1)

        if ziolo_1 == 1 :
            lista_ziol.append("Czerwone źiele")
            lista_ziol.append("Niebieski bez")
            lista_ziol.append("Korzeń piementu")
            lista_ziol.append("Kwiat drugrotu")
            print("Udało mi sie zebrać następujące rośliny: ", lista_ziol)
        elif ziolo_2 == 1 :
            lista_ziol.append("Bagienne źiele")
            lista_ziol.append("Kulczyba wronie oko")
            lista_ziol.append("Trójkolorowe źiele")
            lista_ziol.append("Jaskółcze źiele")
            lista_ziol.append("Ziarna sporyszu")
            print("Udało mi sie zebrać następujące rośliny: ", lista_ziol)



    def mikstury(self):
        miksturki = {1:"",2:"",
                     3:"",4:"",
                     5:"",6:""}

        print("Moge ofiarowac ci kilka pomocnych mikstur: "
              "\n 1. Lęczące: "
              "\n 2. Regeneracyjne: "
              "\n 3. Trucizny: ")
        pokaz_miks = input("Wybierz ___ : ")
        if pokaz_miks == 1:
            print()



obiekt_2 = NPC ("Bogdan", 73, "Źielarz")

print(obiekt_2.info())
print(obiekt_2.zbieranie())


