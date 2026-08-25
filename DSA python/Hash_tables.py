# trying to do it on O(N)
def array_intersection(array1:list, array2:list) ->list:
    hash_table = {}
    result = []
    for values in array1:
        hash_table[values] = True
    for values in array2:
        if values in hash_table:
            result.append(values)
    return result
        
''' making a function that tell you which char in array is a duplicate but the 
 question specifies that we need to consider that only 1 element is duplicate'''
 
def Check_duplicate(array:list) -> str:
    hash_table = {}
    for char in array:
        if hash_table.get(char):
            return char
        else:
            hash_table[char] = True
