class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else: 
                dic[n]+=1
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                s = nums[i]+nums[j]
                dic[nums[i]]-=1
                dic[nums[j]]-=1
                if -s in dic and dic[-s] > 0:
                    results.add(tuple(sorted([nums[i],nums[j],-s])))
                dic[nums[i]]+=1
                dic[nums[j]]+=1

        results = list(results)
        for i in range(len(results)):
            results[i] = list(results[i])
        return results



        