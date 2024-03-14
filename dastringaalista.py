#esempio di utilizzo
def SplitList(sd):
    lista = []
    for i in sd:
        lista.append(int(i))

    return lista

stringa1 = input("inserisci numero: ")
print(SplitList(stringa1))