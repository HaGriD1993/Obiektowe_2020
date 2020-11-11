import random

class Przeciwnik:

    def __init__(self):
        self.imie = "Lilith - Matka Sanktuarium"
        self.wiek = 50
        self.rasa = "Demon"
        self.pkt_ataku = 80
        self.pkt_obrony = 70
        self.pkt_zycia = 3000

    def info(self):
        print("Witaj nazywam się: " + self.imie)

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




