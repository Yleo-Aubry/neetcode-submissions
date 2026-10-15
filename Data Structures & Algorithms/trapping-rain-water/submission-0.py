class Solution:
    def trap(self, height: List[int]) -> int:
        output=0
        n=len(height)
        top_left=[]
        top_right=[0]*n
        for l in range(n):
            if l ==0 :
                top_left.append(height[0])
            else: 
                top_left.append(max(height[l],top_left[l-1]))
        top_right[n-1] = height[n-1]
        for r in range(n-2, -1, -1):
            top_right[r] = max(height[r], top_right[r+1])
        for i in range(len(height)):
            output+=max(0,min(top_left[i],top_right[i])-height[i])
        return output

