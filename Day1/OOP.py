
class school(): 
    
    def __init__(self, name, age, level): 
        self.name = name 
        self.age = age 
        self.level = level 
        
    def show(self): 
        print(f"leanring{self.name}, {self.age}, {self.level} ")

s1 = school("Samuel", 20, "year2")
s1.show()