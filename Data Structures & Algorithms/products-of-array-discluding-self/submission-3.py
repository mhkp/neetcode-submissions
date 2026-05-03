class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                s *= nums[i]
        Output = []

        for i in range(len(nums)):
            if (0 in nums[:i] or 0 in nums[i+1:]):
                Output.append(0)
            elif nums[i]==0:
                Output.append(s)
            else:
                Output.append(int(s/nums[i]))
        return Output

        