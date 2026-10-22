class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            A,B=nums2,nums1
        else:
            A,B=nums1,nums2
        elements = (len(A)+len(B)+1)//2
        a,b=0,len(A)
        while a<=b :
            mid =(a+b)//2
            mid_B=elements-mid
            A_left = A[mid - 1] if mid > 0 else float('-inf')
            A_right = A[mid] if mid < len(A) else float('inf')
            
            B_left = B[mid_B - 1] if mid_B > 0 else float('-inf')
            B_right = B[mid_B] if mid_B < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right :

                if (len(A)+len(B)) % 2 == 1:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                b = mid - 1
            else:
                a = mid + 1
