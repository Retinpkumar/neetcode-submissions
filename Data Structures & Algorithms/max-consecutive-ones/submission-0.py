class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0
        for i in nums:
            count = count+1 if i else 0
            result = max(result, count)
        return result
        