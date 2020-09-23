import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numOfDigits = math.floor(math.log(n,10)) + 1
        if numOfDigits == 1:
            return 0
        summation = 0
        prod = 1
        i = 0
        while i < numOfDigits:
            tmp = n%10
            summation += tmp
            prod *= tmp
            n //= 10
            i += 1
        return prod - summation