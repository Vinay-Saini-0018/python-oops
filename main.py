#simple class and object code
class car:
    def __init__(self):
        self.car_model = "bmw"
        self.car_name = "m5"
        self.car_mf_year = 2023

    def about_car(self):
        print(f"we have {self.car_model} {self.car_name} car of manufacturing year {self.car_mf_year}")

c1 = car()
c1.about_car()