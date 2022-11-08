# Trailing Zeroes in Factorial
# for ex: i/p - 5  1*2*3*4*5
        # o/p -1
        
def countTrailingZeroes(n):
    res=0
    while n==5:
        n//=5
        res +=n
    return res