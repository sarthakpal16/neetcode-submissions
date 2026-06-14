class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]

        for i,h in enumerate(height):
            if i == 0:
                continue
            
            curr_max = max(height[i-1],max_left[-1])
            max_left.append(curr_max)
        
        print(max_left)

        for i,h in enumerate(height[::-1]):
            if i == 0:
                continue
            
            curr_max = max(height[-i],max_right[-1])
            max_right.append(curr_max)
        
        print(max_right)

        trapped_water = 0
        for i,h in enumerate(height):
            trapped_water += max(0,min(max_left[i],max_right[-i])-h)
        
        return trapped_water
            









        