class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        con_seq = []
        n = 0
        for i in range(len(nums)):
            t = nums[i]
            if len(con_seq)>0:
                if t == (con_seq[-1]+1):
                    con_seq.append(t)
                elif t == con_seq[-1]:
                    continue
                else:
                    if len(con_seq)>n:
                        n = len(con_seq)
                    con_seq.clear()
                    con_seq.append(t)
            else:
                con_seq.append(t)
            print(con_seq,n)
        if len(con_seq)>n:
            n = len(con_seq)
        return n