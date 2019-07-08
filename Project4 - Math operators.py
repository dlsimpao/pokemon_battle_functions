#random math operators

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#n choose r
def combination(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))


