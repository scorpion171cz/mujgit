class Pojistenec:
    # Údaje k pojištěné osobě
    def __init__(self, jmeno: str, prijmeni: str, vek: int, telefon: str):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    # Vrací výpis o pojištěnci
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, telefon: {self.telefon}"
