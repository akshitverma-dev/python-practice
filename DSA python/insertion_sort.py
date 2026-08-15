def insertion_sort(array):
    for i in range(1, len(array)):
        temp_var = array[i]
        pos = i-1
        while pos >= 0:
            if array[pos] > temp_var:
                array[pos+1] = array[pos]
                pos -= 1
            else:
                break
        array[pos+1] = temp_var 
    return array