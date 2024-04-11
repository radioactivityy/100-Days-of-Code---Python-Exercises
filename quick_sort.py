import time
import random

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1
    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i +1

def quick_sort(arr, low, high):
    if low < high:  #This line checks if the current subarray has more than one element. 
        key = partition(arr,low,high)
        quick_sort(arr, low, key -1) #  left subarray (elements less than the pivot).
        quick_sort(arr, key + 1, high)
        
def run_time(arr):
    start_time = time.time()
    quick_sort(arr, 0, len(arr) -1)
    end_time = time.time()
    return end_time - start_time
        
if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for _ in range(1000)]
    
    runtime = run_time(unsorted_array)
    
    print("Sorted Array: ")
    for i in range(len(unsorted_array)):
        print("%d" % unsorted_array[i], end = " ")
        
    print("\n Quick Sort Runtime", runtime, "seconds")