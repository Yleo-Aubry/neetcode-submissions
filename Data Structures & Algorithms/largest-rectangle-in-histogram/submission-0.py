class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[]
        area =0
        for i in range (len(heights)):
            if not stack:
                stack.append(i)
                area=max(area,heights[i])
            else :
                if heights[stack[-1]]>heights[i]:
                    while stack and heights[stack[-1]]>heights[i]:
                        hauteur=heights[stack[-1]]
                        stack.pop()
                        if stack :
                            largeur=i-stack[-1]-1 
                            area=max(area,hauteur*largeur)
                        else :
                            area=max(area,hauteur*i)
                    stack.append(i)
                else : 
                    stack.append(i)
        return area
                    
