# Sorting Alg to sort biggest to smallest
# 1. Define the sorting function

def sorting_ar(arr):
    biggest_index = 0
    for i in range (1, len(arr)):
        if arr[i] > arr[biggest_index]:
            biggest_index = i
    return biggest_index        
# Creating a testing array 
def test(arr):
    newArr = []
    while len(arr) > 0:
        biggest_index = sorting_ar(arr)
        newArr.append(arr.pop(biggest_index))
    return newArr
 
print(test([9, 10, 5, 7, 600, -1]))

