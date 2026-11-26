class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        s=0
        while n!=1 :
            while n>0 :
                s+=(n%10)**2
                n=n//10
            if s in seen:
                return False
            else : 
                seen.add(s)
            n=s
            s=0
        return True