import random
import time

class Kowal:
    def __init__(self, imie, wiek, specjanosc, torba):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc
        self.torba = torba

    def info(self):
        print("Witaj nazywam się: " + self.imie, self.specjanosc)

    def przetapianie(self):
        print("Z kilku dostepnych składników wykonam dla ciebie:")
        metale = ["Stal", "Żelazo", "Miedź", "Brąz", "Nikel", "Złoto"]
        dodatki = ["Drewno", "Węgiel", "Świńska skóra", "Ołów", "Diament"]
        wyb_metale = random.sample(metale, k=3)
        wyb_dodatki = random.sample(dodatki, k=2)

        self.torba = wyb_dodatki+wyb_metale
        print(self.torba)

    def kucie(self):

        print("Jako kowal moge wykonać dla ciebie kilka rzeczy.")
        przedmioty = {1: "Miecz",
                      2: "Pancerz",
                      3: "Naramienniki",
                      4: "Hełm",
                      5: "Tarcza"}

        miecze = {1: "Zwykły miecz",
                  2: "Doskonały miecz",
                  3: "Zardzewiały miecz"}

        pancerz = {1: "Pancerz sierzanta",
                   2: "Pancerz strażnika",
                   3: "Pancerz oficera"}


        naramienniki = {1: "Zwykłe naramienniki",
                        2: "Stalowe naramienniki",
                        3: "Żelazne naramienniki"}

        helm = {1: "Skórzany hełm",
                2: "Stalowy hełm",
                3: "Miedziany hełm"}

        tarcze = {1: "Stalowa tarcza",
                  2: "Złota tarcza",
                  3: "Miedziana tarcza"}

        print(przedmioty)
        print("Wybierz przediot który mam wykonac ")
        zrob = int(input(": "))

        print(self.torba,"Zabieram Ci wszystkie składniki.")
        self.torba = []
        opoznienie = (3, 5)

        if zrob == 1:
            print("Wykonałem dla ciebie: ")
            print("Puk puk , Puk puk")
            czas = random.choice(opoznienie)
            time.sleep(czas)
            mieczyk = random.choice(list(miecze.values()))
            self.torba.append(mieczyk)
            print("Otrzymujesz:", self.torba)

        elif zrob == 2:
            print("Wykonałem dla ciebie: ")
            print("Puk puk , Puk puk")
            czas = random.choice(opoznienie)
            time.sleep(czas)
            klata = random.choice(list(pancerz.values()))
            self.torba.append(klata)
            print("Otrzymujesz:", self.torba)

        elif zrob == 3:
            print("Wykonałem dla ciebie: ")
            print("Puk puk , Puk puk")
            czas = random.choice(opoznienie)
            time.sleep(czas)
            ramiona = random.choice(list(naramienniki.values()))
            self.torba.append(ramiona)
            print("Otrzymujesz:", self.torba)

        elif zrob == 4:
            print("Wykonałem dla ciebie: ")
            print("Puk puk , Puk puk")
            czas = random.choice(opoznienie)
            time.sleep(czas)
            glowa = random.choice(list(helm.values()))
            self.torba.append(glowa)
            print("Otrzymujesz:", self.torba)

        elif zrob == 5:
            print("Wykonałem dla ciebie: ")
            print("Puk puk , Puk puk")
            czas = random.choice(opoznienie)
            time.sleep(czas)
            dykta = random.choice(list(tarcze.values()))
            self.torba.append(dykta)
            print("Otrzymujesz:", self.torba)
        else:
            print("Nic dla ciebie nie zrobie, najwidoczniej nie umiem :D ")



obiekt_4 = Kowal("Ryszard", 47, "Kowal",[])
obiekt_4.przetapianie()
obiekt_4.kucie()
