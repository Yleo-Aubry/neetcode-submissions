class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S=set()
        for x in nums :
            if x in S :
                return True
            else : 
                S.add(x)
        return False