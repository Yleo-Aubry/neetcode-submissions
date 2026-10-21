class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        n=1
        output=m
        while n<=m :
            mid=(m+n)//2
            time=sum(math.ceil(x / mid) for x in piles)
            if time <=h:
                output=mid
                m=mid-1
            else:
                n=mid+1
            
        return output 
        