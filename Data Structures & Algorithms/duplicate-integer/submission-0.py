class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L=[]
        for i in range(len(nums)):
            if nums[i] in L :
                return True
            else :
                L.append(nums[i])
        return False
