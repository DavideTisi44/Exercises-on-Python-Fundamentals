# contare quanti caratteri ci sono in alice.txt
# contare quanti caratteri non spazi bianchi ci sono in alice.txt
# contare quanti caratteri alfanumerici [a-z A-Z 0-9] ci sono in alice.txt

fin = open("alice.txt","r") 
linee = fin.read()
fin.close()
car2 = 0
car3 = 0

car = len(linee)

for i in linee:
    if i!=" ":
        car2 += 1

for i in linee:
    if i.isalnum() or i.isalpha():
       car3 += 1


print(car)
print(car2)
print(car3)

