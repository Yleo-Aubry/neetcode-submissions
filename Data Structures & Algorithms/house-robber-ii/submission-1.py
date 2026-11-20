class Solution:
    def rob2(self, nums: List[int]) -> int:
        memo={}
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in memo :
                return memo[i]
            voler=nums[i]+dfs(i+2)
            passer=dfs(i+1)
            memo[i]=max(voler,passer)
            return memo[i]
        return dfs(0)
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob2(nums[1:]),self.rob2(nums[:-1]))
        
