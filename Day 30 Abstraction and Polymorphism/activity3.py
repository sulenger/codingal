class India():
    def capital(self):
        print("New Dehli is the capital of India.")
        
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")
class USA ():
    def capital(self):
        print("Washington,D.C is the capital of USA.")
        
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA ia a developed country")
obj_india = India()
obj_USA = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
        
        