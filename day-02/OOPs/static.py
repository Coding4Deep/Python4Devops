class MathHelper:
    def __init__(self):
        return print("this is math class")
    
    @staticmethod
    def add(x, y):
        return x + y
    
m1=MathHelper()
print(m1.add(2,3))
print(MathHelper.add(5,6))