from pojistenec import Pojistenec

class SpravaPojistencu:
    def __init__(self):
        self.pojistenci = []

    def pridat_pojistence(self, pojistenec: Pojistenec):
        self.pojistenci.append(pojistenec)

    def zobraz_vsechny(self):
        if not self.pojistenci:
            print("Žádní pojištěnci nebyli nalezeni.")
        else:
            for p in self.pojistenci:
                print(p)

    def vyhledat_pojistence(self, jmeno: str, prijmeni: str):
        nalezeni = [p for p in self.pojistenci if p.jmeno.lower() == jmeno.lower() and p.prijmeni.lower() == prijmeni.lower()]
        if not nalezeni:
            print("Pojištěnec nebyl nalezen.")
        else:
            for p in nalezeni:
                print(p)
