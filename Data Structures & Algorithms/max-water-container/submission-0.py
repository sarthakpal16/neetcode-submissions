class Solution:
    def maxArea(self, heights: List[int]) -> int:

        s = 0
        e = len(heights)-1

        ans = 0
        while s < e:
            ans = max(ans, (e-s)*min(heights[s],heights[e]))
            if heights[s] < heights[e]:
                s+=1
            
            else:
                e-=1
        
        return ans


