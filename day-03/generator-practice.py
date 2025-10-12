# class countTo:
#     def __init__(self,max_value):
#         self.max=max_value
#     def __iter__(self):
#         return countToIterator(self.max)

# class countToIterator():
#     def __init__(self,max_value):
#         self.max = max_value
#         self.current = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.max:
#             val = self.current 
#             self.current += 1
#             return val
#         else:
#             raise StopIteration

# counter = countTo(3)

# for i in counter:
#     for j in counter:
#         print(f"{i}:{j} ")







def gen(limit):
    n=1
    while n<limit:
        print(f"before {n} yield")
        yield n
        print(f"after {n} yield")

gen(5)























