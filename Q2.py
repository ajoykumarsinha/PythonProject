# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:


def fact(i):
    
    #print("i value"+str(i))
    
    factval = 1
    
    if (i == 0) :
       factval = 1
    else :
       factval = i * fact(i-1)

    return factval   

x=int(input())
print (fact(x))
    #print( i + ":" +fact(3))