def bubble_sort(lst: list) -> list:
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
            
    return
