class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[1]*len(nums)
        left=[1]*len(nums)
        for i in range (1,len(nums)):
            right[i]=right[i-1]*nums[i-1]
        for j in range (len(nums)-2,-1,-1):
            left[j]=left[j+1]*nums[j+1]
        output=[i*j for (i,j) in zip(right,left)]
        return output 