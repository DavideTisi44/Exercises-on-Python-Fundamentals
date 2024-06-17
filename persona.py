class Persona():

    def __init__(self, first_name, last_name):
        
        if isinstance(first_name, str) and isinstance(last_name,str): 

            self.last_name = last_name
            self.first_name = first_name

            self.age = 0

        else:

            self.age = None

            if isinstance(self.first_name, str):

                self.last_name = None

                print("il cognome inserito non è una stringa!")

            else:

                self.first_name = None

                print("il nome inserito non è una stringa!")

    
    def setName(self, first_name):

        if isinstance(first_name, str):

            self.first_name = first_name

        else:

            print("il nome inserito non è una stringa!")

    
    def setLastName(self, last_name):

        if isinstance(last_name, str):

            self.last_name = last_name

        else:

            print("il cognome inserito non è una stringa!")

    def setAge(self, age):

        if isinstance(age, int):

            self.age = age

        else:

            print("l'età inserita non è un intero!")

    def getName(self):

        return self.first_name
    
    def getLastName(self):

        return self.last_name
    
    def getAge(self):

        return self.age
    
    def greet(self):

        print("ciao, sono", self.getName(), self.getLastName(),"ho", self.getAge(), "anni!")

    







        
