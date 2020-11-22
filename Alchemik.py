import random
import time
#import Bohater

class Alchemik:
    def __init__(self):
        self.imie = "Bogdan"
        self.wiek = 72
        self.specjanosc = "Zielarz"
        self.sakwa = []

    def info(self):
        print("Witaj nazywam się:", self.imie, ",jestem", self.specjanosc+"em")

    def zbieranie(self):
        #mojbohater: Bohater.Bohater
        las_ziola = ["Czerwone źiele", "Niebieski bez", "Korzeń piementu", "Kwiat drugrotu"]
        bagna_ziola = ["Bagienne źiele", "Kulczyba wronie oko", "Trójkolorowe źiele", "Jaskółcze źiele",
                       "Ziarna sporyszu"]

        print("Mogę zebrać składniki roslinne, wybierz gdzie mam się udać: "
              "\n1: Las "
              "\n2: Bagna ")

        zbieraj = int(input("Wybierz miejsce ___ : "))

        if zbieraj == 1:
            print("Ide do lasu. ")
            time.sleep(6)
            ziolo_1 = random.randint(0, 1)
            if ziolo_1 == 1:
                for ziolo in range(5):
                    wybrane = random.choice(las_ziola)
                    self.sakwa.append(wybrane)
                    #mojbohater.plecak.extend(wybrane)
                print("Udało mi sie zebrać: ", self.sakwa)
            elif ziolo_1 == 0:
                print("Nie udało mi sie nic znaleść.")

        if zbieraj == 2:
            print("Ide na bagna. ")
            ziolo_2 = random.randint(0, 1)
            time.sleep(10)
            if ziolo_2 == 1:
                for ziolo in range(5):
                    wybrane = random.choice(bagna_ziola)
                    self.sakwa.append(wybrane)
                print("Udało mi sie zebrać: ", self.sakwa)
            elif ziolo_2 == 0:
                print("Nie udało mi sie nic znaleść.")

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
            self.sakwa.append(miksturki[1]), self.sakwa.append(miksturki[2])
            print("Otrzymujesz: ", miksturki[1], ",", miksturki[2])
        elif pokaz_miks == 2:
            self.sakwa.append(miksturki[3]), self.sakwa.append(miksturki[4])
            print("Otrzymujesz: ", miksturki[3], ",", miksturki[4])
        elif pokaz_miks == 3:
            self.sakwa.append(miksturki[5]), self.sakwa.append(miksturki[6])
            print("Otrzymujesz: ", miksturki[5], ",", miksturki[6])

    def transmutacja(self):
        print("Otrzymujesz: ołów.")
        self.sakwa.append("ołów")
        szansa = [1, 2, 3, 4, 5]
        moja_szansa = random.choice(szansa)
        print("Moge zamienić ołów w złoto: ", "szansa: ", moja_szansa, "%")
        wybor = int(input("Zamienic ołów w złoto ?\n1.Tak \n2.Nie\n: "))
        if wybor == 1:
            print("Szansa na przemianę:", moja_szansa, "%")
            ulepszenie = random.randint(0, 1)
            if ulepszenie == 1:
                print("Pomyślne ulepszenie, otrzymujesz 'Bryłka złota' ")
                self.sakwa.append("bryłka złota")
            elif ulepszenie == 0:
                print("Zawiodłem, tracisz 'ołów' ")
                self.sakwa.remove("ołów")
        else:
            print("Nie chciałeś zaryzykować.")












