import random
a = 5
i=0
def ColoreCasuale():
    colori=["ROSSO","VERDE","GIALLO","ARANCIONE","ROSA","VIOLA"]
    print(colori[random.randint(0,(len(colori)-1))])

while i<=a:
    ColoreCasuale()
    i=i+1

