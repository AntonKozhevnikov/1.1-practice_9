from random import randint
list = [randint(0, 100) for i in range(100)]
list.sort()
print(list)
def binary_search_recursion(lst, val):
    import time
    start_time = time.time()
    left = 0
    right = len(lst) - 1
    mid = (left + right) // 2
    if (val == lst[mid]):
        return mid + 1
    elif (val > lst[mid]):
        return binary_search_recursion(lst[mid + 1:], val) + (mid + 1)
    elif (val < lst[mid]):
        return binary_search_recursion(lst[:mid], val)
print(binary_search_recursion(list, 59))
