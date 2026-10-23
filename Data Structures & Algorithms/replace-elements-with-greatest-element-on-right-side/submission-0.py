class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # Initialize new max with -1 for comparison
        right_max = -1
        # Reverse loop through arr
        for i in range(n-1, -1 ,-1):
            new_max = max(arr[i], right_max)
            arr[i] = right_max
            right_max = new_max
        return arr
        