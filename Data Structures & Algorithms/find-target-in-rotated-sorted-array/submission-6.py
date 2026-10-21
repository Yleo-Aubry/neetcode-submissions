class Solution:
    def search(self, nums: List[int], target: int) -> int:
        output=-1
        a,b=0,len(nums)-1
        while a<=b:
            mid=(a+b)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>nums[b]:
                if nums[a]<=target<nums[mid]:
                    b=mid-1
                else :
                    a=mid+1
            else :
                if nums[mid]<target<=nums[b]:
                    a=mid+1
                else:
                    b=mid-1
        return output
