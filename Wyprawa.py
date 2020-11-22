import Bohater
import random
import time


def wyprawa(mojbohater: Bohater.Bohater):                   #zmienna mojbohater z pliku:Bohater, klasa:Bohater
        print("Opuszczasz miasto, wybierz gdzie sie udasz: \n1.Las \n2.Bagna \n3.Pustynia")

        wybor = int(input(":"))

        if wybor == 1:
            print("Atakuje dzika: ")
            dzik_zycie = random.randint(30, 50)

            while dzik_zycie > 0 and mojbohater.pkt_zycia > 0:
                dzik_atak = random.randrange(1, 10, 2)
                mojbohater.pkt_ataku = random.randint(1, 10)
                mojbohater.pkt_obrony = random.randint(1, 3)
                dzik_zycie -= mojbohater.pkt_ataku
                print("###"*10)
                print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", mojbohater.pkt_ataku)
                time.sleep(2)
                print("Dzik: ", dzik_zycie, "punkty życia.", "\nDzik atakuje: ", dzik_atak)
                time.sleep(2)
                print("Bohater blokuje tarcza: ", mojbohater.pkt_obrony)
                mojbohater.pkt_zycia -= dzik_atak - mojbohater.pkt_obrony
                time.sleep(2)


            if dzik_zycie <= 0:
                print("Zabiłeś dzika")
                mojbohater.plecak.extend(["skóra dzika", "kieł dzika"])
                print("Otrzymujesz: ", mojbohater.plecak)

            else:
                print("Dzik cie zabił,")

        if wybor == 2:
            print("Atakuje bielika: ")
            bielik_zycie = random.randint(30, 50)

            while bielik_zycie > 0 and mojbohater.pkt_zycia > 0:
                bielik_atak = random.randrange(2, 12, 2)
                mojbohater.pkt_ataku = random.randint(1, 10)
                mojbohater.pkt_obrony = random.randint(1, 3)
                bielik_zycie -= mojbohater.pkt_ataku
                print("###" * 10)
                print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", mojbohater.pkt_ataku)
                time.sleep(2)
                print("Bielik: ", bielik_zycie, "zycia.", "\nBielik atakuje: ", bielik_atak)
                time.sleep(2)
                print("Bohater blokuje tarcza: ", mojbohater.pkt_obrony)
                mojbohater.pkt_zycia -= bielik_atak - mojbohater.pkt_obrony
                time.sleep(2)

            if bielik_zycie <= 0:
                print("Zabiłeś bielika")
                mojbohater.plecak.extend(["pióra bielika", "szpony bielika"])
                print("Otrzymujesz: ", mojbohater.plecak)

            else:
                print("Bielik cię zabił,")

        if wybor == 3:
            print("Atakuje skorpiona: ")
            skorpion_zycie = random.randint(30, 50)

            while skorpion_zycie > 0 and mojbohater.pkt_zycia > 0:
                skorpion_atak = random.randrange(2, 12, 2)
                mojbohater.pkt_ataku = random.randint(1, 10)
                mojbohater.pkt_obrony = random.randint(1, 3)
                skorpion_zycie -= mojbohater.pkt_ataku
                print("###"*10)
                print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", mojbohater.pkt_ataku)
                time.sleep(2)
                print("Bielik: ", skorpion_zycie, "zycia.", "\nBielik atakuje: ", skorpion_atak)
                time.sleep(2)
                print("Bohater blokuje tarcza: ", mojbohater.pkt_obrony)
                mojbohater.pkt_zycia -= skorpion_atak - mojbohater.pkt_obrony
                time.sleep(2)

            if skorpion_zycie <= 0:
                print("Zabiłeś skorpiona")
                mojbohater.plecak.extend(["ogon skorpiona", "szpony skorpiona", "oczy skorpiona"])
                print("Otrzymujesz: ", mojbohater.plecak)

