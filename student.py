class Student:
    school="AkiraChix"
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.coutry=country
    def greet(self):
        return f"hello{self.name}, welcome  to{self.school},how is {self.country} "
    def __init__(self,full_name,last_name,birth):
        
