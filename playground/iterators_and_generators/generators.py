def custom_range(num):
    pass

def infinite_number_genrator():
    num = 0
    while True:
        yield num
        num +=1

gen = infinite_number_genrator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)