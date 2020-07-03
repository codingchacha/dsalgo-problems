def is_rotated(array):
    if array[0] < array[-1]:
        return False
    return True
 
 
def get_index(array):
    if not is_rotated(array):
        return -1
    start = 0
    end = len(array) - 1
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] > array[mid + 1]:
            return mid
        elif array[mid] < array[start]:
            end = mid - 1
        else:
            start = mid + 1
 
def binary_search(array , target):
    start = 0
    end = len(array) - 1
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
 
 
 
 
#print(get_index([6,7,1,2,3,4,5]))
def sorted_rotated_search(array , key):
    sudden_dip = get_index(array)
    if sudden_dip == -1:
        return binary_search(array , key)
    if key == array[sudden_dip]:
        return sudden_dip
    elif array[0] <= key:
        start = 0
        end = sudden_dip - 1
        while(start <= end):
            mid = (start + end) // 2
            print(mid)
            if array[mid] == key:
                return  mid
            elif array[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
    else:
        start = sudden_dip + 1
        end = len(array) - 1
        while(start <= end):
            mid = (start + end) // 2
            if array[mid] == key:
                return mid
            elif array[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
 
 
    return -1
 
def get_rotation_count(array):
    if not is_rotated(array):
        return 0
    dip_point = get_index(array)
    return len(array[dip_point + 1:])
 
 
#print(get_rotation_count([8 , 1, 2 , 3 , 4 , 5 , 6])) note if answer changes if rotated in 
# different direction e.g if rotated towards right then and will be no of elements before 
# depression point and if left then after the depression point I assumed rotated left as 
# not mentioned in the problem
 
 
 
 
#print(sorted_rotated_search([3,4,5,6,7,8,1,2] , 8))
 
 
def get_key(array , target):
    is_sorted_desending = False
    if array[0] > array[-1]:
        is_sorted_desending = True
    start = 0
    end = len(array) - 1
    while(start <= end):
 
        mid = (start + end) // 2
        if is_sorted_desending:
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    return -1
 
 
 
 
#print(get_key([1,2,3,4,5] ,5))
 
def smallest_greatest(array , key):
    start = 0
    end = len(array) - 1
    possible_answer = None
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            possible_answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return possible_answer
 
 
print(smallest_greatest([2 ,4,6,8,10] , 9))