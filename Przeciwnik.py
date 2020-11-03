import random



class Przeciwnik:
    def __init__(self, imie, wiek, specjanosc, rasa, pkt_ataku=0, pkt_obrony=0, pkt_zycia=0):
        self.imie = imie
        self.wiek = wiek
        self.specjanosc = specjanosc
        self.rasa = rasa
        self.pkt_ataku = pkt_ataku
        self.pkt_obrony = pkt_obrony
        self.pkt_zycia = pkt_zycia

    def info(self):
        print("Witaj nazywam się: " + self.imie, self.specjanosc)

    def atak(self):
        return random.randint(0, self.pkt_ataku) * (random.randint(0, 2))

    def obrona(self):
        return random.randint(0, self.pkt_obrony)

    def obrazenia(self, ilosc):
        self.pkt_zycia -= ilosc
        if self.pkt_zycia <= 0:
            print(self.imie, "umiera na polu bitwy.")

    def zyje(self):
        if self.pkt_zycia <= 0:
            return False
        else:
            return True

obiekt_2 = Przeciwnik("Lilith", 50, "Matka Sanktuarium", "Demon", 100, 70, 3000)


