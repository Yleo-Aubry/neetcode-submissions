class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            s = 0
            while n > 0:
                n, digit = divmod(n, 10)
                s += digit ** 2
            n = s
        return n == 1
