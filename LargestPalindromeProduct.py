
def isPalindrome(n):
    return str(n) == str(n)[::-1]

def largestPalindromeProductUsing2NDigits(n):
    x = pow(10,n-1)
    y = x
    z = pow(10,n)
    res = x
    for i in range(x,z):
        for j in range(y,z):
            if isPalindrome(i*j):
                res = max(res,i*j)

    return res
def __main__():
    print(largestPalindromeProductUsing2NDigits(2))
    print(largestPalindromeProductUsing2NDigits(3))

__main__()
