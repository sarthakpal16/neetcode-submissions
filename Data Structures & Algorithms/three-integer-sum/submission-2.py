class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i,val in enumerate(nums):
            if i>0 and val == nums[i-1]:
                continue
            s = i+1
            e = len(nums)-1
            while s < e:
                threesum = val + nums[s] + nums[e]

                if threesum == 0:
                    results.append([val,nums[s],nums[e]])
                    s+=1
                    e-=1
                    while nums[s] == nums[s-1] and s < e:
                        s+=1
                
                elif threesum > 0:
                    e-=1
                
                else:
                    s+=1

        return results



        