# trying to do it on O(N)
def array_intersection(array1, array2):
    hash_table = {}
    result = []
    for values in array1:
        hash_table[values] = True
    for values in array2:
        if values in hash_table:
            result.append(values)
    return result
        
