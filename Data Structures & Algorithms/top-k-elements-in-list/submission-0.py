class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count={}
        for x in nums :
            count[x]=1+count.get(x,0)
        count = dict (sorted(count.items(),key=lambda item : item[1], reverse = True))
        return (list(count.keys())[:k])
        