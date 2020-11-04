import random
import time


class Alchemik:
    def __init__(self, imie, wiek, specjanosc, sakwa):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc
        self.sakwa = sakwa

    def info(self):
        print("Witaj nazywam się: " + self.imie, self.specjanosc)

    def zbieranie(self):
        print("Potrzebuje kilku roślin, wybierz gdzie mam się udać: "
              "\n1: Las "
              "\n2: Bagna ")

        zbieraj = input("Wybierz miejsce ___ : ")

        if zbieraj == 1:
            print("Ide do lasu. ")
            time.sleep(6)

        elif zbieraj == 2:
            print("Ide na bagna. ")
            time.sleep(10)

        lista_ziol = []
        ziolo_1 = random.randint(0, 1)
        ziolo_2 = random.randint(0, 1)

        if ziolo_1 == 1:
            lista_ziol.append("Czerwone źiele")
            lista_ziol.append("Niebieski bez")
            lista_ziol.append("Korzeń piementu")
            lista_ziol.append("Kwiat drugrotu")
            self.sakwa = lista_ziol
            print("Udało mi sie zebrać następujące rośliny: ", self.sakwa)

        elif ziolo_2 == 1:
            lista_ziol.append("Bagienne źiele")
            lista_ziol.append("Kulczyba wronie oko")
            lista_ziol.append("Trójkolorowe źiele")
            lista_ziol.append("Jaskółcze źiele")
            lista_ziol.append("Ziarna sporyszu")
            self.sakwa = lista_ziol
            print("Udało mi sie zebrać następujące rośliny: ", self.sakwa)

    def mikstury(self):
        miksturki = {1: "Mała mikstura leczenia",
                     2: "Duża mikstura leczenia",
                     3: "Mikstura 'Powrót do korzeni'",
                     4: "Napar z utopca",
                     5: "Strychnina",
                     6: "Botulina"
                     }

        print("Moge ofiarowac ci kilka pomocnych mikstur: "
              "\n 1. Lęczące "
              "\n 2. Regeneracyjne "
              "\n 3. Trucizny ")

        pokaz_miks = int(input("Wybierz ___ : "))

        if pokaz_miks == 1:
            print(miksturki[1], "||||", miksturki[2])
        elif pokaz_miks == 2:
            print(miksturki[3], "||||", miksturki[4])
        elif pokaz_miks == 3:
            print(miksturki[5], "||||", miksturki[6])



Bogdan = Alchemik ("Bogdan", 73, "Źielarz",[])

print(Bogdan.info())
print(Bogdan.zbieranie())
print(Bogdan.mikstury())







