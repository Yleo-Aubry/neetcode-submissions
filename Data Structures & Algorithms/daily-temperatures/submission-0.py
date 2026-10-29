class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]]>=temperatures[i]: 
                stack.append(i)
            else : 
                while stack and temperatures[stack[-1]]<temperatures[i]:
                    diff=i-stack[-1]
                    results[stack[-1]]=diff
                    stack.pop()
                stack.append(i)
        return results 