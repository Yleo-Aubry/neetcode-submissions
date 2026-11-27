class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen=set()
        n=len(nums)
        for k in range (0,n+1):
            seen.add(k)
        for num in nums:
            seen.discard(num)
        return seen.pop()