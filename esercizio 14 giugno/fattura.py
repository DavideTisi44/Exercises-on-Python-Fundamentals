class Fattura():

    def __init__(self, patient, doctor):

        if doctor.isAValidDoctor == True:

            self.patient = patient
            self.doctor = doctor
            self.salary = 0
            self.fattura = len(patient)

        else:

            self.patient = None
            self.doctor = None
            self.salary = None
            self.fattura = None

            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):

        self.salary = self.doctor.parcel * self.fattura

    def getFatture(self):

        self.fattura = len(self.patient)

    def addPatient(self, newPatient):
        
        self.patient.append(newPatient)

        self.getFatture()
        self.getSalary()

        print("Alla lista del Dottor", self.doctor.getLastName(), "è stato aggiunto il paziente", self.patient.idCode)

    def removePatient(self, idCode):

        for i in self.patient:

            if i.idCode == idCode:

                self.patient.remove(i)

                self.getFatture()
                self.getSalary()

                print("Alla lista del Dottor", self.doctor.getLastName(), "è stato rimosso il paziente", self.patient.idCode)

        

            
