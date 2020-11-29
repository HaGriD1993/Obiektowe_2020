import random
import time
import Bohater


class Kowal():
    def __init__(self):
        self.imie = "Darek"
        self.wiek = 52
        self.specjanosc = "Kowal"

    def info(self):
        print("Witaj nazywam się: " + self.imie, "jestem", self.specjanosc+"em")        #PRZEDSTAWIA SIE

    def skladniki(self, mojbohater: Bohater.Bohater):
        metale = ["Stal", "Żelazo", "Miedź", "Brąz", "Nikiel", "Złoto"]
        dodatki = ["Drewno", "Węgiel", "Świńska skóra", "Ołów", "Diament"]

        wyb_metale = random.sample(metale, k=3)                                         #RANDOMOWE ELEMENTY Z LISTY
        wyb_dodatki = random.sample(dodatki, k=2)                                       #RANDOMOWE ELEMENTY Z LISTY

        if 'bryłka złota' in mojbohater.plecak:                                         #SPRAWDZA CZY MA BRYŁKE W PLECAKU
            wybor = input("Za 'bryłke złota' mogę ofiarować ci kilka metali. (T/N): ")
            if wybor == str("T"):
                print("Za bryłke otrzymujesz: ")
                mojbohater.plecak.remove("bryłka złota")                                #USUWA BRYŁKE Z PLECAKA
                print(wyb_metale)
                mojbohater.plecak.extend(wyb_metale)                                    #DODAJE DO PLECAKA Z LISTY METALI
                time.sleep(2)
                print("Dostajesz również: ", wyb_dodatki)
                mojbohater.plecak.extend(wyb_dodatki)                                   #DODAJE DO PLECAKA Z LISTY DODATKÓW

            if wybor == str("N"):
                print("Wróć jak zmienisz zdanie.")
        else:
            print("Nie masz 'bryłki złota'. Wróć jak znajdziesz.")                      #JAK NIE MA BRYŁKI TO KONIEC

    def przetapianie(self, mojbohater: Bohater.Bohater):
        wybor = input("Za 'bryłke złota' mogę przetopię metal w sztabke.(T/N): ")
        metale_lista = ["Stal", "Żelazo", "Miedź", "Brąz", "Nikiel", "Złoto"]
        if wybor == str("T"):

            for metal in metale_lista:                                      #SPRAWDZA CZY Z ELEMENTY Z LISTY METALI SA W PLECAKU
                if metal in mojbohater.plecak:
                    print("Ten metal moge przetopić: ", metal)
                    wybor_metal = input("Czy przetopic: (T/N): ")
                    if wybor_metal == str("T"):
                        mojbohater.plecak.remove(metal)                             #USUWA METAL Z PLECAKA, DODAJE SZTABKE
                        mojbohater.plecak.append(str("sztabka ") + metal)
                    else:
                        print("Może poźniej.")
            else:
                print("Nie masz nic do przetopienia.")


    def handel(self, mojbohater: Bohater.Bohater):
        print("Moge sprzedać ci kilka rzeczy: \nCena to 'bryłka złota.'")

        przedmioty = {
            1: "Miecz",
            2: "Pancerz",
            3: "Naramienniki",
            4: "Hełm",
            5: "Tarcza",
            6: "Inne"
        }

        miecze = {
            1: "Zwykły miecz",
            2: "Doskonały miecz",
            3: "Zardzewiały miecz"
        }

        pancerz = {
            1: "Pancerz sierzanta",
            2: "Pancerz strażnika",
            3: "Pancerz oficera"
        }

        naramienniki = {
            1: "Zwykłe naramienniki",
            2: "Stalowe naramienniki",
            3: "Żelazne naramienniki"
        }

        helm = {
            1: "Skórzany hełm",
            2: "Stalowy hełm",
            3: "Miedziany hełm"
        }

        tarcze = {
            1: "Stalowa tarcza",
            2: "Złota tarcza",
            3: "Miedziana tarcza"
        }
        inne = {
            1: "osełka",
            2: "młotek kowalski",
            3: "kilof",
            4: ""
        }

        if 'bryłka złota' in mojbohater.plecak:                 #SPRAWDZA CZY MA BRYŁKE
            print("Tyle masz bryłek: ", mojbohater.plecak.count("bryłka złota"))
            time.sleep(2)
            print("\n", przedmioty)
            wybor = int(input("Wybierz: "))                          #WYBIERA KATEGORIE

            if wybor == 1:
                print(miecze)
                x = int(input("Który chcesz kupic: "))
                if x in miecze:
                    mojbohater.plecak.append(miecze.get(x))         # (X) JAKO KLUCZ ZE SLOWNIKA, DO PLECAKA DODAJE WARTOSC
                    mojbohater.plecak.remove('bryłka złota')

            if wybor == 2:
                print(pancerz)
                x = int(input("Który chcesz kupic: "))
                if x in pancerz:
                    mojbohater.plecak.append(pancerz.get(x))
                    mojbohater.plecak.remove('bryłka złota')

            if wybor == 3:
                print(naramienniki)
                x = int(input("Który chcesz kupic: "))
                if x in naramienniki:
                    mojbohater.plecak.append(naramienniki.get(x))
                    mojbohater.plecak.remove('bryłka złota')

            if wybor == 4:
                print(helm)
                x = int(input("Który chcesz kupic: "))
                if x in helm:
                    mojbohater.plecak.append(helm.get(x))
                    mojbohater.plecak.remove('bryłka złota')

            if wybor == 5:
                print(tarcze)
                x = int(input("Który chcesz kupic: "))
                if x in tarcze:
                    mojbohater.plecak.append(tarcze.get(x))
                    mojbohater.plecak.remove('bryłka złota')

            if wybor == 6:
                print(inne)
                x = int(input("Który chcesz kupic: "))
                if x in inne:
                    mojbohater.plecak.append(inne.get(x))
                    mojbohater.plecak.remove('bryłka złota')
        else:
            print("Nie masz: 'bryłek złota'")









