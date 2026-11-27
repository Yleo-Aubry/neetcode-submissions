class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    def countBits(self, n: int) -> List[int]:
        L=[]
        for i in range (0,n+1):
            L.append(self.hammingWeight(i))
        return L
        