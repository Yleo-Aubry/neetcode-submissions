class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output=nums[0]
        low,high=1,1

        for num in nums :
            temp=high*num
            high = max(temp,num*low,num)
            low=min(temp,num*low,num)
            output=max(output,high)
        return output
