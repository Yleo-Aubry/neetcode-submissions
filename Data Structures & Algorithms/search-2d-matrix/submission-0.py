class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[-1][-1]<target:
            return False
        if matrix[0][0]>target :
            return False
        a,b=0,len(matrix)-1
        m=0
        if matrix[b][0]<=target :
            m=b
        else:
            while a<b:
                mid=(a+b)//2
                if matrix[mid][0]<=target:
                    if matrix[mid+1][0]>target :
                        m=mid
                        break
                    else: 
                        a=mid+1
                else :
                    if matrix[mid-1][0]<=target :
                        m=mid-1
                        break
                    else:
                        b=mid-1
        find=False
        c,d=0,len(matrix[m])-1
        while c<=d:
            milieu=(c+d)//2
            if matrix[m][milieu]==target:
                find = True
                return find
            elif matrix[m][milieu]>target :
                d=milieu-1
            else:
                c=milieu+1
        return find




