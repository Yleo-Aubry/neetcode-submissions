class Solution:
    def ceil_perso(self,x):
        n = int(x)
        return n if x <= n else n + 1
    def sum_time(self,piles,i):
        time=0
        for x in piles :
            time+=self.ceil_perso(x/i)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        n=1
        output=m
        while n<=m :
            mid=(m+n)//2
            time=self.sum_time(piles,mid)
            if time <=h:
                output=mid
                m=mid-1
            else:
                n=mid+1
            
        return output    

            
