class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            x,y=stones[-1],stones[-2]
            if x==y:
                del stones[-1]
                del stones[-1]
            elif y>x:
                stones[-2]=y-x
                del stones[-1]
            else : 
                stones[-1]=x-y
                del stones[-2]
            
        return stones[0] if stones else 0