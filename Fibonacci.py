

# Fibonacci recursive approach
numTerms = int(input("How many terms of Fibonacci sequence to print?"))

# What are the first few terms of the fibonacci sequence?
# 0  1  1  2  3

# Main method
def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return(fibonacci(n-1) + fibonacci(n-2))

# check if the munber of the terms is valid
if numterms <= 0:
    print("Please enter a positive integer")
else:
    print("fibonacci sequence: ")
    for i in range(numTerms):
        print(fibonacci(i))
    
