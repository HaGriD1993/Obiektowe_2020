import Bohater
import Przeciwnik
import Alchemik
import Kowal
import Wyprawa


if __name__ == "__main__":
    print("Witaj w grze. Na początku podaj imie dla twojego bohatera: ")

    imie = input("\nImie bohatera: ")
    print("\n'bryłka złota'- możesz ja zdobyc na wyprawach oraz podaczas kopania złóż metali.")
    postac = Bohater.Bohater(imie)
    kowal = Kowal.Kowal()
    alchemik = Alchemik.Alchemik()
    mob = Przeciwnik.Przeciwnik()


    #Menu:
    while True:
        print("\n1. Bohater:      Informacje||Naprawa ekwipunku||Polowanie||Ognisko||Wyprawa||Inwentarz||Odpoczynek")
        print("2. Kowal:        Informacje||Kuźnia||Handel")
        print("3. Alchemik:     Informacje||Rośliny||Mikstury")
        print("4. Walka z Lilith: ")
        print("5. Koniec gry.")
        wybor_1 = int(input("Wybierz: "))

        #Bohater:
        if wybor_1 == 1:
            postac.info()
            print("\n1.Naprawa ekwipunku: ")
            print("2.Polowanie: ")
            print("3.Gotowanie: ")
            print("4.Wyprawa: ")
            print("5.Sprawdź plecak: ")
            print("6.Górnictwo: ")
            print("7.Odpoczynek: ")

            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                postac.naprawaeq()
            elif wybor_2 == 2:
                postac.polowanie()
            elif wybor_2 == 3:
                postac.ognisko()
            elif wybor_2 == 4:
                Wyprawa.wyprawa(postac)
            elif wybor_2 == 5:
                postac.pokazplecak()
            elif wybor_2 == 6:
                postac.gornictwo()
            elif wybor_2 == 7:
                postac.odpoczynek()
                continue

        #Kowal
        if wybor_1 == 2:
            kowal.info()
            print("\n1.Materiały: ")
            print("2.Odzysk materiałów: ")
            print("3.Rzemiosło: ")
            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                kowal.skladniki(postac)
            elif wybor_2 == 2:
                kowal.przetapianie(postac)
            elif wybor_2 == 3:
                kowal.handel(postac)
                continue

        #Alchemik
        if wybor_1 == 3:
            alchemik.info()
            print("\n1.Rośliny: ")
            print("2.Mikstury ")
            print("3.Transmutacja (ołów -> złoto)")

            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                alchemik.zbieranie(postac)
            elif wybor_2 == 2:
                alchemik.mikstury(postac)
            elif wybor_2 == 3:
                alchemik.transmutacja(postac)
                continue

        if wybor_1 == 4:
            mob.info()
            mob.walka(postac)

        #Kuniec:
        if wybor_1 == 5:
            print("Koniec gry, było miło. (-(-_-)-) ")
            break






