class Media:

    def __init__(self):

        self.title = ""
        self.reviews= []

    def set_title(self, title):
        
        self.title = title

    def get_title(self):
        
        return self.title

    def add_val (self, value):
        
        if value <= 5 and value >= 1:
            
            self.reviews.append(value)

    def get_media (self):

        return round(sum(self.reviews)/len(self.reviews),2)
         
    def get_rate (self):
        
        a = round(sum(self.reviews)/len(self.reviews))

        if a == 1:

            return("Terribile")

        if a == 2:

            return("Brutto")

        if a == 3:

            return("Normale")

        if a == 4:

            return("Bello")

        if a == 5:

            return("Grandioso")

    def rate_percentage (self, value):

        c=0
        
        for n in self.reviews:

            if n==value:
                    
                c+=1

        return round((100/len(self.reviews))*c,2)


    def recensione (self):
        
        print("Titolo: ", self.get_title())
        print("Voto: ", self.get_media())
        print("Giudizio: ", self.get_rate())
        print("Terribile: ", self.rate_percentage(1),"%")
        print("Brutto: ",self.rate_percentage(2),"%")
        print("Normale: ",self.rate_percentage(3),"%")
        print("Bello: ",self.rate_percentage(4),"%")
        print("Grandioso: ",self.rate_percentage(5),"%")


class Film(Media):
    def __init__(self, title):
        super().__init__()
        self.set_title(title)



film = Film("The Shawshank Redemption")

film.add_val(1)
film.add_val(2)
film.add_val(3)
film.add_val(4)
film.add_val(4)
film.add_val(4)
film.add_val(5)
film.add_val(5)
film.add_val(5)
film.add_val(5)

film.recensione()


    

