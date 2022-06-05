from typing import List


def longestconsecutive_seq(nums : List[int]) -> int:
    S = set(nums)
    maxlen = 0  # initialise max length with 0

    for n in nums:  # iterate for each number
        if (n - 1) not in S:  # check for current element
            length = 1
            while (n + length) in S:  # check for consecutive elements
                length = length + 1
            # update maxlen
            maxlen = max(maxlen, length)

    # return result
    return maxlen


nums = [100, 1, 4, 50, 3, 11, 2, 12]
print(longestconsecutive_seq(nums))

# Time: O(n), under assumption hash insert take+ search take O(1)= n*O(1)+ 2*n*O(1)
# Space: O(n),  extra space used by hash set

