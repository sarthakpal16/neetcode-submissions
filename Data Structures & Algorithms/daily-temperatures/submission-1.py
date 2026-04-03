class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        result = [0]*len(temperatures)
        
        count = 0
        for i in range(1,len(temperatures)):
            t = temperatures[i]
            # print(t,i)
            # print(stack)
            # print(result)
            if stack and t<stack[-1][0]:
                stack.append((t,i))
                
            else:
              
                while stack and t > stack[-1][0]:
                    x = stack.pop()
                    result[x[1]] = i - x[1]

                stack.append((t,i))
        return result





        
        