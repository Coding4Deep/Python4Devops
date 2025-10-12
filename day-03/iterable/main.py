class CountToIterator:
    def __init__(self,max_value):
        self.max=max_value
        self.current=1
    def __iter__(self):
        return  CountToIterator(self.max)
    def __next__(self):
        if self.current<=self.max:
            result=self.current
            self.current+=1
            return result
        else:
            raise StopIteration
counter = CountToIterator(5)
for number in counter:
    for number2 in counter:
        print(number, ":", number2)

# counter = CountToIterator(5)
# for number in  CountToIterator(5):
#     for number2 in  CountToIterator(5):
#         print(number,":",number2)