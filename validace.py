def nacti_neprazdny_text(prompt: str) -> str:
    while True:
        hodnota = input(prompt).strip()
        if hodnota:
            return hodnota
        else:
            print("Tato hodnota nesmí být prázdná!")

def nacti_cislo(prompt: str) -> int:
    while True:
        try:
            hodnota = int(input(prompt))
            return hodnota
        except ValueError:
            print("Zadejte platné číslo!")
