class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen=set()
        for x in nums:
            if x in seen:
                seen.discard(x)
            else:
                seen.add(x)
        return seen.pop()
        
            
