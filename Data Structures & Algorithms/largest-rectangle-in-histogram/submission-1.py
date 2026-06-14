class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0,heights[0]]]
        max_area = 0
        
        for i in range(1,len(heights)):
            # print(stack,max_area)
            if heights[i] >= stack[-1][1]:
                stack.append([i,heights[i]])
                # print(stack, max_area)

            else:
                j = i
                # print(stack,max_area)
                while stack and heights[i] < stack[-1][1]:
                    j,h = stack.pop()
                    max_area = max(max_area,(i-j)*h)
                    # print(stack, max_area)
                stack.append([j,heights[i]])
                # print(stack, max_area)
        
        for s in stack:
            i,h = s
            a = (len(heights)-i)*h
            max_area = max(max_area,a)
            # print(a,max_area,i,h)


        return max_area
            


        