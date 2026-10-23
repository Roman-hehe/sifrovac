def zasifruj(text, posun):
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    return text


def desifruj(text, posun):
    abeceda = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
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