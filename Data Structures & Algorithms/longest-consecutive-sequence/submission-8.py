class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0
    
        for x in num_set:
            if x-1 not in num_set:
                t = x
                c_t = 1

                while t+1 in num_set:
                    t+=1
                    c_t+=1
                streak = max(c_t,streak)
        return streak