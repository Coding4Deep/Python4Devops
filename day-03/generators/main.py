def CustomGen(limit):
    n=1
    for i in limit:
        yield n
        n=n*2
obj=CustomGen(range(5))

print(type(obj))
print(type(CustomGen))

for i in obj:
    print(i)