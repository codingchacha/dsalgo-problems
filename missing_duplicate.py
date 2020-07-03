""" 1. We are given an array containing ‘n’ 
distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ 
numbers, find the missing number
like .. 1 5 3 2 -- missing number is 4
2.  We are given an array containing ‘n’ 
distinct numbers taken from the range 0 to ‘n’.
 one number is repeated, find the duplicate number
3. We are given an array containing ‘n’ distinct numbers 
taken from the range 0 to ‘n’. there is one duplicate 
 and one missing number.. find those duplicate and missing number
 
 
 
 
Duplicate  -3 missing - 5"""

#1
def get_missing_elem(array):
    for idx in range(len(array)):
        index = abs(int(array[idx]))
        if index >= len(array):
            continue 
        if array[index] == 0:
            array[index] = "0"
        else:
            array[index] *= -1
    for idx in range(len(array)):
        if array[idx] == "0":
            continue
        elif array[idx] > -1:
            return idx
    return idx + 1
#print(get_missing_elem([6 , 3 , 0 , 1, 4 , 2]))

#2
def get_duplicate(array):
    for elem in array:
        index = abs(int(elem))
        if array[index] == "0" or array[index] <= -1:
            return index
        else:
            if array[index] == 0:
                array[index] = "0"
            else:
                array[index] *= -1
print(get_duplicate([0,3,1,0 , 2]))

"" 1 We are given an array containing n distinct numbers taken from range 0 to n 
since the array has only n numbers out of total n+1 find the missing no e.g
 
I/P - [1 , 5 , 3 , 2]
O/P - > 4 """
 
 
# method keeping track of visited index
 
def get_missing_elem(array):
    for idx in range(len(array)):
        index = abs(int(array[idx]))
        if index >= len(array):
            continue 
        if array[index] == 0:
            array[index] = "0"
        else:
            array[index] *= -1
    for idx in range(len(array)):
        if array[idx] == "0":
            continue
        elif array[idx] > -1:
            return idx
    return idx + 1
#print(get_missing_elem([6 , 3 , 0 , 1, 4 , 2]))
 
def get_duplicate(array):
    for elem in array:
        index = abs(int(elem))
        if array[index] == "0" or array[index] <= -1:
            return index
        else:
            if array[index] == 0:
                array[index] = "0"
            else:
                array[index] *= -1
#print(get_duplicate([1 , 0 , 0 , 4 , 3]))
 
 
def get_duplicate_missing(array):
    for elem in array:
        index = abs(int(elem))
        if array[index] == "0" or array[index] <= -1:
            duplicate = index
        else:
            if array[index] == 0:
                array[index] = "0"
            else:
                array[index]*= -1
    for idx , elem in enumerate(array):
        if elem == "0":
            continue
        else:
            if elem > -1:
                return idx , duplicate
 
 
print(get_duplicate_missing([1 , 0 , 0 , 4 , 3]))






