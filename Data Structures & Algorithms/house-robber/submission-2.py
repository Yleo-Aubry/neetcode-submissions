class Solution:
    def rob(self, nums: List[int]) -> int:
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
