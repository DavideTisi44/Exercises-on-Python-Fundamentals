from persona import Persona

class Dottore(Persona):
    
    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name, last_name)

        if isinstance (specialization, str):

            self.specialization = specialization

        else:

            self.specialization = None

            print("la specializzazione inserita non è una stringa!")

        if isinstance(parcel, float):

            self.parcel = parcel

        else:

            self.parcel = None

            print("la parcella inserita non è di tipo float!")

    def setSpecialization (self, specialization):

        if isinstance(specialization, str):

            self.specialization =  specialization

        else:

            print("la specializzazione inserita non è una stringa!")

    def setSpecialization (self, parcel):

        if isinstance(parcel, float):

            self.parcel =  parcel

        else:

            print("la parcella inserita non è di tipo float!")

    def getSpecialization(self):

        return self.specialization
    
    def getParcel(self):

        return self.parcel
    
    def isAValidDoctor(self):

        if self.age > 30:

            print("Doctor", self.getName(), self.getLastName(), "is valid!")

            return True

        else:

            print("Doctor", self.getName(), self.getLastName(), "is NOT valid!")

            return False

    def doctorGreet(self):

        self.greet()
        print("Sono un medico", self.getSpecialization())






d1 = Dottore("Gianni" , "MattoFracico", "Spacciatore" , 6.9)
d2 = Dottore("Paolo" , "ScartaCazzi", "Muratore" , 6.9)

d1.setAge(23)
d2.setAge(45)
d1.doctorGreet()
d2.doctorGreet()
d1.isAValidDoctor()
d2.isAValidDoctor()



        
    


