class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)

        def eatingTime(rate):
            time = 0
            for p in piles:
                time+=(p+rate-1)//rate
            return time    
        
        l = 1
        hi = piles[0]
        m = -1
        while l<=hi:
            m = (l+hi)//2
            if m == 1:
                return m
            curr = eatingTime(m)
            prev = eatingTime(m-1)
            print(l,m,hi,curr,prev)
             
            if curr<=h and prev>h:
                return m
            
            elif curr<=h:
                hi = m-1
            
            else:
                l = m+1
        
        return m