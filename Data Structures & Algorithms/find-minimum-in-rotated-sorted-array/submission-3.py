class Solution:
    def findMin(self, nums: List[int]) -> int:
        a,b=0,len(nums)-1
        while a<=b:
            if nums[a]<nums[b]:
                return nums[a]
            mid = (a+b)//2
            if mid!=0 and nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>nums[b]:
                a=mid+1
            else:
                b=mid-1 
        return nums[mid]
