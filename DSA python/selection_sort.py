def selection_sort(array):
    for i in range(len(array)-1):
        least_num_index = i
        for j in range(i+1, len(array)):
            if array[j]<array[least_num_index]:
                least_num_index = j
        if least_num_index != i:
            array[i] , array[least_num_index] = array[least_num_index], array[i]
    return array