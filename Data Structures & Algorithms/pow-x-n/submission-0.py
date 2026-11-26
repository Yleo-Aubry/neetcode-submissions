class Solution:
    def __init__(self):
        self.seen={0:1}
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        if n==1 :
            return x
        if n in self.seen:
            return self.seen[n]
        else :
            if n%2==0:
                self.seen[n]=self.myPow(x,n//2)**2
            else :
                self.seen[n]=x*self.myPow(x,n//2)**2
        return self.seen[n]
        