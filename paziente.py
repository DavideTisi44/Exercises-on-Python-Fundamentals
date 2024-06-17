from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name, last_name, idCode):
        super().__init__(first_name, last_name)

        if isinstance (idCode, str):

            self.idCode = idCode

        else:

            print("il codice inserito non è una stringa!")

    def setIdCode(self, idCode):

        if isinstance (idCode, str):

            self.idCode = idCode

        else:

            print("il codice inserito non è una stringa!")

    def getIdCode(self):

        return self.idCode
    
    def patientInfo(self):

        print("Paziente:", self.getName, self.getLastName)
        print("ID:", self.getIdCode)



    