# Brute Force Method
import time 
def brute_force(text,sample):
    n = len(text)
    m = len(sample)
    start_time = time.time()
    for i in range(n-m +1): # From 0 to n-m
        j = 0 
        while j < m:
                if text[i+j] != sample[j]:
                    break
                j += 1
        if j == m:
            end_time = time.time()
            run_time = end_time - start_time
            print("Sample found at index:", i)
            print("Brute Sort Runtime:", run_time, "seconds")  # Print the runtime
            return i 
    end_time = time.time()
    run_time = end_time - start_time
    print("Sample not found")
    print("Brute Sort Runtime:", run_time, "seconds")  # Print the runtime
    return -1

# testing
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
sample = "blaahsdhdhfgdhdhdajjjddjjshahagagagbsbddnd"
brute_force(text, sample)

