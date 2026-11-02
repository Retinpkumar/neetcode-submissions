from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total

def get_min(nums: List[int]) -> int:
    minval = nums[0]
    for n in nums:
        if n < minval:
            minval = n
    return minval

def get_max(nums: List[int]) -> int:
    maxval = nums[0]
    for n in nums:
        if n > maxval:
            maxval = n
    return maxval

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
