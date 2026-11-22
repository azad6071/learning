
def sumOfMultipleOf3and5BelowNum(num):
    sum = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            sum=sum+i
    return sum
def __main__():
    print(sumOfMultipleOf3and5BelowNum(10))
    print(sumOfMultipleOf3and5BelowNum(1000))

__main__()
