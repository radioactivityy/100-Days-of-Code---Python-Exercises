def factoriel(x):
    if x == 1:
        return 1
    else:
        return x * factoriel(x-1) # Recursion
        
print(factoriel(3))