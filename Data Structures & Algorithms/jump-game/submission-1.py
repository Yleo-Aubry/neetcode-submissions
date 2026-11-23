class Solution:
    def canJump(self, nums: List[int]) -> bool:
        output=[None]*len(nums)
        output[-1]=True
        def dfs(i):
            if i >= len(nums)-1:
                return True
            if output[i] is not None :
                return output[i]
            output[i]=False
            for k in range (1,nums[i]+1):
                if dfs(i+k):
                    output[i]=True
                    return True
            return False
                


        return dfs(0)
