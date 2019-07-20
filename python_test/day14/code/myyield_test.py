
def myeven(start, stop):
    while start < stop:
        if start % 2 == 0:
            yield start
        start += 1

evens = list(myeven(10,20))
print(evens)

for x in myeven(21,30):
    print(x)