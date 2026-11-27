class Solution:
    def vers_binaire(self,n):
        if n == 0:
            return "0"
        bits = ""
        while n > 0:
            bits = str(n % 2) + bits
            n //= 2
        return bits
    def hammingWeight(self, n: int) -> int:
        return sum(int(c) for c in self.vers_binaire(n))
        