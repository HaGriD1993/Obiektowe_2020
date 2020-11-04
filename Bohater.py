import random
import time


class Bohater:
    def __init__(self, imie, wiek, specjanosc, rasa, sakwa, pkt_ataku=0, pkt_obrony=0, pkt_zycia=0):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc
        self.rasa = rasa
        self.sakwa = sakwa
        self.pkt_ataku = pkt_ataku
        self.pkt_obrony = pkt_obrony
        self.pkt_zycia = pkt_zycia


    def info(self):
        print("Witaj nazywam się: " + self.imie, self.specjanosc)

    def atak(self):
        return random.randint(0, self.pkt_ataku) * (random.randint(2, 3))

    def obrona(self):
        return random.randint(0, self.pkt_obrony)

    def obrazenia(self, ilosc):
        self.pkt_zycia -= ilosc
        if self.pkt_zycia <= 0:
            print(self.imie, "śmierć na polu bitwy.")

    def zyje(self):
        if self.pkt_zycia <= 0:
            return False
        else:
            return True

    def naprawaeq(self):
        pancerz = random.randint(0, 3)
        bron = random.randint(0, 4)

        print("Stan pancerza:", pancerz)
        while pancerz < 3:
            time.sleep(4)
            pancerz += 1
            print("Potrzebuje naprawic pancerz. Puk Puk ==> Puk Puk")
            if pancerz == 3:
                print("Naprawiłem. \nPancerz w doskonałym stanie.")

        print("Stan broni:", pancerz)
        while pancerz < 3:
            time.sleep(4)
            bron += 1
            print("Potrzebuje naprawić broń. Puk Puk ==> Puk Puk")
            if bron == 4:
                print("Naprawiłem. \nBroń w doskonałym stanie.")


    def polowanie(self):

        print("Moj plecak jest pusty, czas ruszyć po jedzenie.", self.sakwa)
        print("1: Las"
              "\n2: Bagna")
        zw_las = ["Sarna", "Królik", "Wilk"]
        zw_bagna = ["Kaczka", "Gęś", "Czapla"]
        zw_czesci = ["mięso", "skóra", "głowa", "wątroba"]
        m_miejsce = int(input("Wybierz gdzie chcesz sie udać: "))

        if m_miejsce == 1:
            print("Jestes w lesie: ...... szukaj śladów zwierzyny.")
            time.sleep(5)
            zwierze = random.choice(zw_las)
            print("Znalazłem ślady: ", zwierze)
            time.sleep(3)
            print("Udało mi sie upolować", zwierze)
            self.sakwa.append(random.sample(zw_czesci, k=2))
            print("zebrano:", self.sakwa)

        if m_miejsce == 2:
            print("Jestes na bagnach: ...... szukaj śladów zwierzyny.")
            time.sleep(5)
            zwierze = random.choice(zw_bagna)
            print("Znalazłem ślady: ", zwierze)
            time.sleep(3)
            print("Udało mi sie upolować", zwierze)
            self.sakwa.append(random.sample(zw_czesci, k=2))
            print("zebrano:", self.sakwa)


Michau = Bohater("Michał", 47, "Mag Bitewny", "Człowiek",[], 150, 95, 1500)

Michau.info()
Michau.naprawaeq()
Michau.polowanie()

