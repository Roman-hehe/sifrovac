abeceda="abcdefghijklmnopqrstuvwxyz"
zprava = input("Zadej zpravu: ")
posun = input("(Zadej kladne cislo, sifra se posouva v abecede doprava)\no kolik pozic abecedy chcete zpravu posunout:")
zasifrovane =""
def zasifruj(zprava, posun):
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    for i in range(len(zprava)):
        index = 0
        znak = zprava[i].lower()
        if znak == " ":
            zasifrovane = zasifrovane + " "
        for j in range(len(abeceda)):
            if znak == abeceda[j]:
                index = j + posun
                while index >= 26:
                    index = index - 26
                zasifrovane = zasifrovane + abeceda[index]
                break
            
            
    return(zasifrovane)


def desifruj(text, posun):
    #TODO (B): posuň každé písmeno o 'posun' míst dozadu
    return text


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))