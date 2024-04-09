import time
import random

def bubbleSort(arr):
    n = len(arr)
    start_time = time.time()  # Start time
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break
    
    end_time = time.time()  # End time
    run_time = end_time - start_time  # Calculate runtime
    return run_time
 
# Driver code to test above
if __name__ == "__main__":
    unsorted_array = [random.randint(1, 100000) for _ in range(10000)]
 
    run_time = bubbleSort(unsorted_array)
 
    print("Sorted array:")
    for i in range(len(unsorted_array)):
        print("%d" % unsorted_array[i], end=" ")
    
    print("\nBubble Sort runtime:", run_time, "seconds")
