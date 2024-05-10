class Zoo:
    def __init__(self,fences=[],zoo_keeper=[]):
        self.fences = fences
        self.zoo_keeper = zoo_keeper


class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat, health):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = health
        health = round(100*(1/age),3)

class Fence:
    def __init__(self, area, temperature, habitat, animals = []):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = animals
        
class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
