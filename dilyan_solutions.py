class Passenger:

#init methodfor Passenger
    def __init__(self, first = None, last = None, email = None, rides_taken = None):
        self.first = first
        self.last = last
        self.email = email
        self.rides_taken = rides_taken

rebecca_black = Passenger("Rebecca", "Black", "rebecca.black@gmail.com", 0 )
print(rebecca_black.first) # "Rebecca"
print(rebecca_black.last) # "Black"
print(rebecca_black.email) # "rebecca.black@gmail.com"
print(rebecca_black.rides_taken) # 0

#init method for Driver

class Driver:

#init method
    def __init__(self, first, last, favorite_hobby = "driving"):
        self.first = first
        self.last = last
        self.favorite_hobby = favorite_hobby

dale_earnhardt = Driver("Dale", "Earnhardt")
print(dale_earnhardt.first) # "Dale"
print(dale_earnhardt.last) # "Earnhardt"
print(dale_earnhardt.favorite_hobby) # "driving"
