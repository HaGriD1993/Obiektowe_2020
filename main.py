import Bohater
import Przeciwnik
import Alchemik
import Kowal
import Wyprawa

if __name__ == "__main__":
    print("Witaj w grze. Na początku podaj imie dla twojego bohatera: ")
    imie = input("\nImie bohatera: ")
    postac = Bohater.Bohater(imie)
    kowal = Kowal.Kowal()
    alchemik = Alchemik.Alchemik()
    mob = Przeciwnik.Przeciwnik()

    #Menu:
    while True:
        print("\n1. Bohater:      Informacje|| Naprawa ekwipunku|| Polowanie|| Ognisko")
        print("2. Kowal:          Informacje|| Odzysk materiałów|| Rzemiosło")
        print("3. Alchemik:       Informacje|| Rośliny|| Mikstury")
        print("4. Koniec gry.")
        wybor_1 = int(input("Wybierz: "))

        #Bohater:
        if wybor_1 == 1:
            postac.info()
            print("\n1.Naprawa ekwipunku: ")
            print("2.Polowanie: (las||bagna)")
            print("3.Gotowanie: ")
            print("4.Przygoda: ")

            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                postac.naprawaeq()
            elif wybor_2 == 2:
                postac.polowanie()
            elif wybor_2 == 3:
                postac.gotowanie()
            elif wybor_2 == 4:
                Wyprawa.wyprawa(postac)
                continue

        #Kowal
        if wybor_1 == 2:
            kowal.info()
            print("\n1.Materiały: (metale||dodatki)")
            print("2.Odzysk materiałów (przetopy)")
            print("3.Rzemiosło: (broń||pancerz)")
            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                kowal.skladniki()
            elif wybor_2 == 2:
                kowal.przetapianie()
            elif wybor_2 == 3:
                kowal.kucie()
                continue

        #Alchemik
        if wybor_1 == 3:
            alchemik.info()
            print("\n1.Rośliny: (zbieranie)")
            print("2.Mikstury (lęczące||regeneracyjne||trucizny)")
            print("3.Transmutacja (ołów -> złoto)")

            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                alchemik.zbieranie()
            elif wybor_2 == 2:
                alchemik.mikstury()
            elif wybor_2 == 3:
                alchemik.transmutacja()
                continue

        #Kuniec:
        if wybor_1 == 4:
            print("Koniec gry, było miło. (-(-_-)-) ")
            break






