class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, current = nums[0], 0
        for n in nums:
            current=max(current,0)
            current += n
            best=max(best, current)
        return best

        