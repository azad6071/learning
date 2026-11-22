
def sumOfEvenFibonacciNumbersTillNum(num):
    x = 0
    y = 1
    sum = 0
    while x+y <= num:
        t = x+y
        x = y
        y = t
        if t % 2 == 0:
            sum = sum + t
    return sum

def __main__():
    print(sumOfEvenFibonacciNumbersTillNum(8))
    print(sumOfEvenFibonacciNumbersTillNum(4_000_000))


__main__()
