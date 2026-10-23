def zasifruj(zprava, posun):
    abeceda="abcdefghijklmnopqrstuvwxyz"
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    zasifrovane =""
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
    abeceda = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #TODO (B): posuň každé písmeno o 'posun' míst dozadu
    abeceda="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    interkpunkce = ".,!?-;:()[]' "
    desifrovany_text = ""
    
    for pismeno in text:
        if pismeno in abeceda:
            index = abeceda.index(pismeno)
            novy_index = (index - posun) % len(abeceda)
            desifrovany_text += abeceda[novy_index]
        elif pismeno in interkpunkce:
            desifrovany_text += pismeno
        else:
            desifrovany_text += pismeno
            
    return desifrovany_text


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))