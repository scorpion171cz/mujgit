from sprava_pojistencu import SpravaPojistencu
from pojistenec import Pojistenec
import validace

def zobraz_menu():
    print("\n----------------------------")
    print("Evidence pojištěných osob")
    print("----------------------------")
    print("1. Přidat nového pojištěnce")
    print("2. Zobrazit všechny pojištěnce")
    print("3. Vyhledat pojištěnce")
    print("4. Konec")

def main():
    sprava = SpravaPojistencu()

    while True:
        zobraz_menu()
        volba = input("Zadejte volbu (1-4): ")

        if volba == "1":
            jmeno = validace.nacti_neprazdny_text("Zadejte jméno: ")
            prijmeni = validace.nacti_neprazdny_text("Zadejte příjmení: ")
            vek = validace.nacti_cislo("Zadejte věk: ")
            telefon = validace.nacti_neprazdny_text("Zadejte telefonní číslo: ")
            pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
            sprava.pridat_pojistence(pojistenec)
            print("Pojištěnec byl úspěšně přidán.")
        elif volba == "2":
            print("\nSeznam všech pojištěnců:")
            sprava.zobraz_vsechny()
        elif volba == "3":
            jmeno = validace.nacti_neprazdny_text("Zadejte jméno: ")
            prijmeni = validace.nacti_neprazdny_text("Zadejte příjmení: ")
            print("\nVýsledek vyhledávání:")
            sprava.vyhledat_pojistence(jmeno, prijmeni)
        elif volba == "4":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba. Zadejte číslo 1 až 4.")

if __name__ == "__main__":
    main()
