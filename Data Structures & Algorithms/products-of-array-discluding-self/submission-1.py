class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        product = 1 
        for x in nums :
            product*=x
        for i in range (len(nums)):
            if nums[i]==0:
                j=1
                for k in range (len(nums)):
                    if k!=i:
                        j*=nums[k]

                output.append(int(j))
            else :
                output.append(int(product/nums[i]))
        return output            