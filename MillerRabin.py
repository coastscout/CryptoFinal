import random

# Get user input for testing
numtest = int(input("What number are you testing? "))
witness = int(input("What number is your witness? "))

def find_k_m(numtest):
    k = 0
    numtestmin = numtest - 1
    while numtestmin % 2 == 0:
        k += 1
        numtestmin = numtestmin // 2
    m = numtestmin
    print(f"k={k}")  # Print k here
    return k, m

def miller_rabin(numtest, witness):
    k, m = find_k_m(numtest)
    
    b_values = []  # Store b0, b1, b2, ..., b_k-1 values
    
    b0 = pow(witness, m, numtest)
    b_values.append(b0)
    
    if b0 == 1 or b0 == numtest - 1:
        return True, b_values  #Inconclusive, possibly prime
    
    for _ in range(k):
        b0 = pow(b0, 2, numtest)
        b_values.append(b0)
        if b0 == numtest - 1:
            return True, b_values  # Inconclusive, possibly prime
    
    return False, b_values  # Composite and return k

# Call Miller-Rabin function
result, b_values = miller_rabin(numtest, witness)

# Print the result
if result:
    print(f"{numtest} is inconclusive, possibly prime.")
else:
    print(f"{numtest} is composite.")

# Print b_values
for i, b in enumerate(b_values):
    print(f"b{i}:", b)

if result:
    result_str = "probably prime"
else:
    result_str = "composite"

# Print cga values
cga_values = ','.join(map(str, b_values))
print("***Be careful with the format, I'm not super confident it will be the same or that I will have the right amount of b's, spaces, etc.")
print(f"cga{{{cga_values},{result_str}}}")
