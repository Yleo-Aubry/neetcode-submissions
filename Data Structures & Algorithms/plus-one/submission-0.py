class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        L=[0]*(n+1)
        ret=1
        for i in range (n-1,-1,-1):
            if digits[i]+ret>10:
                L[i+1]+=(digits[i]+ret//10)
            elif digits[i]+ret==10:
                 L[i+1]+=0
            else : 
                L[i+1]+=(digits[i]+ret)
                ret=0
        if ret==1:
            L[0]=1
            return L
        else:
            return L[1:]
        

        