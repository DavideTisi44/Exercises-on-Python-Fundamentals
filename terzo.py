#In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
#antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
#le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
#john, alice, mary
#altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
#stampare l'elenco delle persone presenti

gente=["antonio", "marco", "andrea", "luigi", "tony", "bruno", "laura" , "anita", "annarita", "lucia"]
print("nella stanza entrano:")
print(gente)

print("dalla stanza escono" , gente[0] , "e" , gente[1])
gente.pop(0)
gente.pop(0)

print("quindi rimangono:")
print(gente)

gente.append("john")
gente.append("alice")
gente.append("mary")

print("si aggiungono" , gente[8:11])

print("ora nella stanza ci sono:")
print(gente)

gente.pop(0)
gente.pop(0)

print("le persone rimanenti sono:")
print(gente)


