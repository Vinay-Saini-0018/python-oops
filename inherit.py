class college:
    def __init__(self):
        self.c_name = "amity university"
        self.c_location = "jaipur, rajasthan"

class student(college):
    def __init__(self,name,course):
        super().__init__()
        self.s_name = name
        self.s_course = course

    def data(self):
        print(f"""hello sir, my name is {self.s_name} and i am purshing 
              {self.s_course} from {self.c_name} {self.c_location}""")
        
s1 = student("vinay","btech")
s1.data()