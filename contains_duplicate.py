# Problem: Given an integer array nums,
# return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List


def containsduplicate(nums: List[int]) -> bool:
    s = set()

    for n in nums:
        if n in s:
            return True
        s.add(n)
    return False


nums = [1, 2, 3, 1]
print(containsduplicate(nums))


# Ex. nums = [1,2,3,1]
# hashset = ()
# for n = 1  -->  1 not in hashset then add
# hashset.add(1) -> hashset = (1)

# for n = 2  --> 2 not in hashset then add
# hashset.add(2) -> hashset = (1,2)

# for n = 3  --> 3 not in hashset then add
# hashset.add(3) -> hashset = (1,2,3)

# for n = 1  --> 1 is already present in hashset -> contains duplicate
# return True


# Time: O(n), n is size of array
# Space: O(n), extra space used by hashset
