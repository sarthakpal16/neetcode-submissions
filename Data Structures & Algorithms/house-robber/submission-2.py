class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        n = len(nums)

        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(n):
            dp[i] = nums[i]
            mx = 0
            for j in range(i-1):
                mx = max(mx,dp[j])
            dp[i] += mx
        return max(dp)
        