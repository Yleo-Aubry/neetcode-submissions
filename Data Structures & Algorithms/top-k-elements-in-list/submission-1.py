class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        paquet=[[] for x in range  (len(nums)+1)]
        count={}
        for i in range (len(nums)):
            count[nums[i]]=1+count.get(nums[i],0)

        for num,frequence in count.items():
            paquet[frequence].append(num)
        res=[]
        for i in range (len(nums),-1,-1):
            for num in paquet[i]:
                res.append(num)
                if len(res)==k:
                    return res
      