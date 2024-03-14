# r lettura (per leggere i file)
# w scrittura (cancella il contenuto precedente) 
# a append (modifica il file aggiundendo nuovo contenuto a quello gia presente)    
fin = open("alice.txt","r") 
linee = fin.readlines()
fin.close()
l1 = []

for l in linee:
    l1.append(l.strip())

linee = l1

parole = []

for l in linee:
    parole.extend(l.split(" "))



for f in range(0,(len(parole)-1)):
    print(parole[f])
