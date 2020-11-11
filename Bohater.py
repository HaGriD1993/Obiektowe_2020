import random
import time

class Bohater:

    def __init__(self, imie):
        self.imie = imie
        self.wiek = 27
        self.specjanosc = "Wojownik"
        self.rasa = "człowiek"
        self.plecak = []
        self.pkt_ataku = 10
        self.pkt_obrony = 3
        self.pkt_zycia = 100


    def info(self):
        print("Nazywam się: " + self.imie+".", "Jestem", self.specjanosc+"iem,", "mam lat: ", self.wiek)
        print("Punkty ataku:", self.pkt_ataku,
              "\nPunkty obrony:", self.pkt_obrony,
              "\nPunkty życia:", self.pkt_zycia)

    def plecak(self):
        print(self.plecak)

    def naprawaeq(self):
        pancerz = random.randint(0, 3)
        bron = random.randint(0, 4)

        print("Przed walka musze sprawdzic stan swojego oręża:", "\npancerz:", pancerz, "broń:", bron)
        print("Stan pancerza:", pancerz)

        while pancerz < 5:
            time.sleep(4)
            pancerz += 1
            print("Naprawiam pancerz. Puk Puk")
            print("stan:", pancerz)

            if pancerz == 5:
                print("Naprawiłem. \nPancerz w doskonałym stanie.")


        print("Stan broni:", bron)
        while bron < 5:
            time.sleep(4)
            bron += 1
            print("Naprawiam i szlifuje broń. Puk Puk")
            print("stan:", bron)

            if bron == 5:
                time.sleep(2)
                print("Naprawiłem. \nBroń ostra i w doskonałym stanie.")


    def polowanie(self):
        print("Moj plecak jest pusty, czas ruszyć po jedzenie.", self.plecak)
        print("1: Las"
              "\n2: Bagna")

        zw_las = ["Sarna", "Królik", "Wilk"]
        zw_bagna = ["Kaczka", "Gęś", "Czapla"]
        zw_czesci = ["mięso", "skóra", "głowa", "wątroba"]
        m_miejsce = int(input("Wybierz gdzie chcesz sie udać: "))

        if m_miejsce == 1:
            print("Jestem w lesie: ...... szukam śladów zwierzyny.")
            time.sleep(5)
            zwierze = random.choice(zw_las)
            print("Znalazłem ślady: ", zwierze)
            time.sleep(5)
            print("Udało mi sie upolować", zwierze)
            time.sleep(5)
            self.plecak.append(random.sample(zw_czesci, k=2))
            print("zebrałem:", self.plecak)

        if m_miejsce == 2:
            print("Jestem na bagnach: ...... szukam śladów zwierzyny.")
            time.sleep(5)
            zwierze = random.choice(zw_bagna)
            print("Znalazłem ślady: ", zwierze)
            time.sleep(3)
            print("Udało mi sie upolować", zwierze)
            time.sleep(5)
            self.plecak.append(random.sample(zw_czesci, k=2))
            print("zebrałem:", self.plecak)


    def gotowanie(self):
        time.sleep(3)
        print("Z upolowanego zwierzecia moge przygotowac potrawe: ", "\nAby rozpalić ognisko bede potrzebował drewna. ")
        drewno = 0
        time.sleep(2)
        print("Szukam drewna.")

        while drewno < 3:
            print("znalazłem 'kawałek drewna'.")
            time.sleep(3)
            drewno += 1
            self.plecak.append("kawałek drewna")

        print("Zebrałem :", self.plecak.count("kawałek drewna"), "kawałki drewna \nTyle drewna powinno wystarczyć.")
        ognisko = 0
        print("Próbuje rozpalić ognisko.")

        while ognisko <= 3:
            time.sleep(3)
            print("cyk, cyk, cyk")
            ognisko += 1
        print("Ognisko płonie.")

        if 'kawałek drewna' in self.plecak:
            while 'kawałek drewna' in self.plecak:
                self.plecak.remove("kawałek drewna")

        else:
            print("Nie mam już drewna.")
        print("Moge teraz przygotować jedzenie.")


    def przygoda(self):
        print("Opuszczasz miasto, wybierz gdzie sie udasz: \n1.Las \n2.Bagna")
        wybor = int(input(":"))

        if wybor == 1:
            print("Atakuje dzika: ")
            dzik_zycie = random.randint(30, 50)

            while dzik_zycie > 0 and self.pkt_zycia > 0:
                dzik_atak = random.randrange(1, 10, 2)
                self.pkt_ataku = random.randint(1, 10)
                self.pkt_obrony = random.randint(1, 3)
                dzik_zycie -= self.pkt_ataku
                print("Bohater: ", self.pkt_zycia, "życia.", "\nBohater atakuje: ", self.pkt_ataku)
                time.sleep(2)
                print("Dzik: ", dzik_zycie, "punkty życia.", "\nDzik atakuje: ", dzik_atak)
                print("\nBohater blokuje tarcza: ", self.pkt_obrony)
                self.pkt_zycia -= dzik_atak - self.pkt_obrony
                time.sleep(2)

            if dzik_zycie <= 0:
                print("Zabiłeś dzika")
                self.plecak.extend(["skóra dzika", "kieł dzika"])
                print("Otrzymujesz: ", self.plecak)

            else:
                print("Dzik cie zabił,")

        if wybor == 2:
            print("Atakuje bielika: ")
            bielik_zycie = random.randint(30, 50)

            while bielik_zycie > 0 and self.pkt_zycia > 0:
                bielik_atak = random.randrange(2, 12, 2)
                self.pkt_ataku = random.randint(1, 10)
                self.pkt_obrony = random.randint(1, 3)
                bielik_zycie -= self.pkt_ataku
                print("Bohater: ", self.pkt_zycia, "życia.", "\nBohater atakuje: ", self.pkt_ataku)
                time.sleep(2)
                print("Bielik: ", bielik_zycie, "zycia.", "\nBielik atakuje: ", bielik_atak)
                print("Bohater blokuje tarcza: ", self.pkt_obrony)
                self.pkt_zycia -= bielik_atak - self.pkt_obrony
                time.sleep(2)

            if bielik_zycie <= 0:
                print("Zabiłeś bielika")
                self.plecak.extend(["pióra bielika", "szpony bielika"])
                print("Otrzymujesz: ", self.plecak)

            else:
                print("Bielik cię zabił,")








