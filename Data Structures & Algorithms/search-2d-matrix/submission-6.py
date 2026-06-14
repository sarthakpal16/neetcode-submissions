import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix)
        y = len(matrix[0])
        l = 1
        h = x*y
        while l<=h:
            m = (l+h)//2
            mx = int(math.ceil(m/y))
            my = m%y
            print(l,h,m,mx,my)
            if target < matrix[mx-1][my-1]:
                h = m-1
            
            elif target > matrix[mx-1][my-1]:
                l = m+1
            
            else:
                return True
            
        return False


        