# O(n) | 0(1) space - iterate over lst but no space extra needed
def remove_even(lst):
    ptr = 0
    while ptr < len(lst):
        num = lst[ptr]
        if num % 2 == 0:
            lst.remove(num)
            ptr = 0
        else:
            ptr += 1
    return lst


print(remove_even([1,2,4,5,10,6,3])) # [1,5,3]