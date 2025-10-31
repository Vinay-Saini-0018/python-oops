#simple class and object code
class car:
    def __init__(self):
        self.__owner = "vinay"
        self.car_model = "bmw"
        self.car_name = "m5"
        self.car_mf_year = 2023

    def about_car(self):
        print(f"we have {self.car_model} {self.car_name} car of manufacturing year {self.car_mf_year}")

    def get_owner(self):
        return self.__owner
    
    def set_owner(self,new_owner):
        self.__owner = new_owner

c1 = car()
c1.about_car()
print(f"personal data --> owner of this car is {c1.get_owner()}")
print("\n")
c1.set_owner("vinay saini")
print(f"this car is sold out and the name of the new owner is {c1.get_owner()} ")