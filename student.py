class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,birth,age):
        self.first_name=first_name
        self.last_name=last_name
        self.birth=birth
        self.age=age
    def fullname(self):
        name=self.first_name+self.last_name
        return name
    def short_name(self):
        short= self.first_name [0].split()+self.last_name[0].split()
        return short
    def year(self,current_year):
        birthdate=current_year-self.age
        return birthdate   