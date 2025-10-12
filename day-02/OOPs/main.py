class students:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.__marks=marks
    def info(self):
        return f"{self.name} is {self.age} years old"
    # access private variable
    def private(self):
        return self.__marks
    
s1=students("sagar",18,78)
print(s1.private())
print(s1._students__marks)
print(s1.marks)







# print(s1.name)
# print(s1.age)
# print(s1.info())
# print(s1.marks)  #show errro beacause marks is private
