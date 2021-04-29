import timeit
lst = [97, 98, 99]

def f1(list):
    string = ""
    for i in list:
        string += chr(i)
    return string

print(timeit.timeit(f1(lst)))
