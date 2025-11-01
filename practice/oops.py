class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def start(self):
        self.price = "80000"
        print("Car Started")

    def full_name(self):
        print(f"{self.brand}-{self.model}")

c1 = Car("tata","superTata")
print(c1.brand)
print(c1.model)
c1.start()
print(c1.__dict__)
c1.full_name()
