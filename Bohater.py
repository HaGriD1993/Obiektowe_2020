import random
import time


class Bohater:
    def __init__(self, imie):
        self.imie = imie
        self.specjanosc = "Wojownik"
        self.plecak = []                          #DLA TESTOW MOZNA DODAC BRYŁKE NA START
        self.pkt_ataku = 10
        self.pkt_obrony = 3
        self.pkt_zycia = 90
        self.stan_pancerz = random.randint(0, 5)                        # DOWOLNY POZIOM PANCERZA I BRONI
        self.stan_bron = random.randint(0, 5)

    def info(self):
        print("#######"*5)
        print("Imie:", self.imie, "\tKlasa:", self.specjanosc)
        print("Punkty życia:", self.pkt_zycia, "/ 100",
              "\nStan pancerza:", self.stan_pancerz, "/ 5",
              "\nStan broni: ", self.stan_bron, "/ 5",
              "\nilość bryłek", self.plecak.count('bryłka złota'))
        print("#######" * 5)

    def pokazplecak(self):
        print("#######" * 5)
        self.plecak.sort()
        print("zawartość: ", self.plecak, ", ilość w plecaku:", len(self.plecak))
        print("#######" * 5)
        pass

    def naprawaeq(self):
        print("Przed walka musze sprawdzic stan swojego oręża:",
              "\npancerz:", self.stan_pancerz, "|| broń:", self.stan_bron)
        print("#######" * 5)

        if self.stan_bron and self.stan_pancerz == 5:               #SPRAWDZAM STAN BRONI I PANCERZA
            print("Ekwipunek w doskonałym stanie.")
        elif self.stan_bron < 5 or self.stan_pancerz < 5:
            print("Powinieneś naprawić ekwipunek. Narzedzia można znaleść u Kowala.")

        if 'młotek kowalski' in self.plecak:                    #SPRAWDZA CZY W PLECAKU JEST MŁOTEK
            print("Naprawiam pancerz.")
            time.sleep(1)
            while self.stan_pancerz < 5:
                time.sleep(3)
                self.stan_pancerz += 1
                print("stan:", self.stan_pancerz)

                if self.stan_pancerz == 5:
                    print("#######" * 5)
                    print("Naprawiłem.")
                    self.plecak.remove("młotek kowalski")
        else:
            print("Nie mam wymaganych narzedzi do naprawy pancerza.")

        if 'osełka' in self.plecak:                         #SPRAWDZA CZY W PLECAKU JEST OSEŁKA
            print("Naprawiam i szlifuje broń.")
            time.sleep(1)
            while self.stan_bron < 5:
                time.sleep(3)
                self.stan_bron += 1
                print("stan:", self.stan_bron)

                if self.stan_bron == 5:
                    print("#######" * 5)
                    print("Naprawiłem.")
                    self.plecak.remove("osełka")
        else:
            print("Nie mam wymaganych narzedzi do ostrzenia broni.")

    def polowanie(self):
        print("Czas ruszyć po jedzenie.")
        print("1: Las"
              "\n2: Bagna")

        zw_las = ["Sarna", "Królik", "Wilk"]
        zw_bagna = ["Kaczka", "Gęś", "Czapla"]
        zw_czesci = ["mięso", "skóra", "głowa", "wątroba"]
        m_miejsce = int(input("Wybierz gdzie chcesz sie udać: "))

        if m_miejsce == 1:
            print("Jestem w lesie: ...... szukam śladów zwierzyny.")
            time.sleep(3)
            zwierze = random.choice(zw_las)
            print("Znalazłem ślady: ", zwierze)
            szansa_zwierze = random.randint(0, 2)

            if szansa_zwierze == 2:                                     #SZANSA NA UPOLOWANIE.
                time.sleep(3)
                print("Udało mi sie upolować", zwierze)
                time.sleep(3)
                self.plecak.extend(random.sample(zw_czesci, k=2))        #DODAJE DO PLECAKA 2-ELEMENTY
                print("zebrałem:", self.plecak)
            else:
                time.sleep(2)
                print(zwierze, "spłoszone.", "\nNic nie upolowałem.")

        if m_miejsce == 2:
            print("Jestem na bagnach: ...... szukam śladów zwierzyny.")
            time.sleep(5)
            zwierze = random.choice(zw_bagna)
            szansa_zwierze = random.randint(0, 2)
            if szansa_zwierze == 2:                                     #SZANSA NA UPOLOWANIE.
                time.sleep(3)
                print("Udało mi sie upolować", zwierze)
                time.sleep(3)
                self.plecak.extend(random.sample(zw_czesci, k=2))       #DODAJE DO PLECAKA 2- ELEMENTY
                print("zebrałem:", self.plecak)
            else:
                time.sleep(2)
                print(zwierze, "spłoszone.", "\nNic nie upolowałem.")

    def ognisko(self):
        print("Do przygotowania 'potrawki', będziesz potrzebował 'mięsa' oraz 'wątroby'.")

        if 'mięso' and 'wątroba' in self.plecak:
            print("W plecaku sa składniki na 'potrawke'.")
            print("\nAby rozpalić ognisko będę potrzebował drewna.")

            if 'mięso' in self.plecak:
                self.plecak.remove('mięso')
            if 'wątroba' in self.plecak:
                self.plecak.remove('wątroba')

            self.plecak.append('potrawka')

            drewno = 0
            time.sleep(2)
            print("Szukam drewna.")

            while drewno < 3:
                time.sleep(2)
                print("znalazłem 'kawałek drewna'.")
                time.sleep(1)
                drewno += 1
                self.plecak.append("kawałek drewna")

            print("Zebrałem :", self.plecak.count("kawałek drewna"),
                  "kawałki drewna \nTyle drewna powinno wystarczyć.")

            ognisko = 0
            print("Próbuje rozpalić ognisko.")

            while ognisko <= 3:
                time.sleep(3)
                print("cyk, cyk, cyk")
                ognisko += 1
            print("Ognisko płonie.")
            print("Otrzymujesz 'potrawkę'.")

            if 'kawałek drewna' in self.plecak:                 #SPRAWDZA KAWAŁEK DREWNA W PLECAKU, JAK JEST TO USUWA.
                while 'kawałek drewna' in self.plecak:
                    self.plecak.remove("kawałek drewna")
            else:
                print("Nie mam już drewna.")
        else:
            print("W plecaku nie ma skladników na 'potrawke'. Udaj sie na Polowanie.")


    def odpoczynek(self):
        print("Możesz troche odpocząc, przywróci ci to punkty życia.")

        if self.pkt_zycia == 100:
            print("Jesteś pełni sił.")
        else:
            pass

        odpoczynek = input("Chcesz odpocząc: (T/N): ")           #ODNOWIENIE ZYCIA (ODPOCZYNEK)

        if odpoczynek == str("T"):
            time.sleep(5)
            self.pkt_zycia = 100
            print("Jesteś w pełni zregenerowany: ", self.pkt_zycia, "/", self.pkt_zycia)
        else:
            print("Może innym razem.")

        if 'potrawka' in self.plecak:
            zjesc = input("Zjeść potrawkę, |życie = 100|. [T/N]?: ")        #ODNOWIENIE ZYCIA (POTRAWKA)
            if zjesc == str("T"):
                self.plecak.remove("potrawka")
                self.pkt_zycia = 100
                print("Zycie Bohatera: ", self.pkt_zycia, "/", self.pkt_zycia)
            if zjesc == str("N"):
                print("Zostawiam na pozniej.")

    def gornictwo(self):
        rudy_metali = ["ruda Stali", " ruda Żelaza", "ruda Miedźi", "ruda Brązu", "ruda Niklu", "ruda Złota"]

        if 'kilof' in self.plecak:
            print("Szukam złóż: ")
            time.sleep(5)
            ruda = random.choice(rudy_metali)
            szansa = random.randint(0, 3)
            print(szansa, "moja szansa")
            time.sleep(1)
            print("Zanalazłem:", ruda)

            if szansa == 2:
                print("Wydobyłem: ", ruda)
                time.sleep(2)
                self.plecak.append(ruda)

            elif szansa == 1:
                print("Wydobyłem: ", ruda)
                time.sleep(2)
                self.plecak.append(ruda)
                self.plecak.append('bryłka złota')
            else:
                time.sleep(2)
                print("Nic nie wydobyłem.")
        else:
            print("Nie mam narzedzia do wydobycia. \nNarzedzia możesz znaleść u Kowala.")
