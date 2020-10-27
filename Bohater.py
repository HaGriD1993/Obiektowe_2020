import random
import time

class Bohater:
    def __init__(self, imie, wiek, specjanosc, rasa, pkt_ataku = 0, pkt_obrony = 0, pkt_zycia = 0):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc
        self.rasa = rasa
        self.pkt_ataku = pkt_ataku
        self.pkt_obrony = pkt_obrony
        self.pkt_zycia = pkt_zycia

    def info(self):
        return "Witaj nazywam się: " + self.imie, self.specjanosc

    def atak(self):
        return random.randint(0, self.pkt_ataku) * (random.randint(2, 3))

    def obrona(self):
        return random.randint(0, self.pkt_obrony)

    def naprawaEQ(self):
        pancerz = random.randint(0,3)
        print("Poziom pancerza:", pancerz)
        while pancerz < 3:
            time.sleep(3)
            pancerz += 1
            print("Potrzebuje naprawic pancerz. Puk Puk ==> Puk Puk")
            if pancerz == 3:
                print("Naprawiłem. \nPancerz w doskonałym stanie.")


obiekt = Bohater("Numilles", 47, "Mag Bitewny", "Człowiek", 150, 95, 1500)

print(obiekt.info())
print(obiekt.naprawaEQ())



# Czy narazie idzie to w dobrym kierunku ?
#
# Mysle jeszcze jak rozwiazac problem z ta cala symulacja tej walki.





