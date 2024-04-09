import time
import random

def insertionSort(arr):
    n = len(arr)
    start_time = time.time()
    
    if n <= 1:
        return
    
    for i in range(1, n):
        key = arr[i] # current element = ky
        j = i - 1
        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    end_time = time.time()
    run_time = end_time - start_time
    return run_time

unsorted_array = [random.randint(1,10000) for _ in range (1000)]
run_time = insertionSort(unsorted_array)
print("Sorted array:")
for i in range(len(unsorted_array)):
    print("%d" % unsorted_array[i], end= " ")
print("\nInsetion Sort Runtime:", run_time, "seconds")


