from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # initialize two pointers
    l, r = 0, len(nums)-1  # set left at start & right at end of array

    while l < r:
        cursum = nums[l] + nums[r]  # define current sum

        if cursum > target:
            r -= 1      # decrement right pointer
        elif cursum < target:
            l += 1      # increment right pointer
        else:
            return [l + 1, r + 1]  # here index start by adding one


nums = [2, 7, 11, 15]
target = 9
print("Result:", twoSum(nums, target))

# time complexity: O(n), linear time
# space: O(1), no extra space
