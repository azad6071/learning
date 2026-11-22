
def largestPrimeFactor(n):
    if n < 2: return null
    ## n = p1^a1*p2^a2..
    x = 2
    while x*x <= n:
        while n % x == 0:
            n //= x
        x+=1

    return n

def __main__():
    print(largestPrimeFactor(10))

    print(largestPrimeFactor(600851475143))

__main__()
