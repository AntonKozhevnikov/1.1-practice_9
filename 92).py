def binary_search(length, x):
    import time
    start_time = time.time()
    print('length=', length)
    from random import randint
    list = [randint(0, 100) for i in range(length)]
    list.sort()
    print(list)
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == x:
            return mid + 1, time.time() - start_time
        if list[mid] < x:
            left = mid + 1
        elif list[mid] > x:
            right = mid - 1
    return False
    print('time of execution', time.time() - start_time)

print(binary_search(1, 4))
print(binary_search(100, 87))
print(binary_search(1000, 56))
print(binary_search(1000000, 723))
