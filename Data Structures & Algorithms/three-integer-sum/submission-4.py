def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        paires=[]
        while l<r :
            if numbers[l]+numbers[r]==target :
                paires.append([l,r])
                l+=1
                r-=1
            elif  numbers[l]+numbers[r]>target : 
                r-=1
            else :
                l+=1
        return paires

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        for i in range (len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            sub_array=nums[i+1:]
            all_res = twoSum(self,sub_array,-nums[i])
            for res in all_res :
                triplet=[nums[i],sub_array[res[0]],sub_array[res[1]]]
                triplet.sort()
                if triplet not in output:
                    output.append(triplet)

        return output
            
            
            

        