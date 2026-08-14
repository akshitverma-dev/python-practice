def Bubble_sort(lst:list) ->list:
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst