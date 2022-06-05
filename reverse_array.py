# from typing import List
#
# def reverseString(s: List[str]) -> None:
#     s[:] = s[::-1]
#     return s

# 2 approach: by swaping
from typing import List


def reverseString(s: List[str]) -> None:

    start = 0
    end = len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start+1
        end = end-1
    return s


s = ["h", "e", "l", "l", "o"]
print("Input:", s)
reverseString(s)
print("output:", s)

# Time complexity= O(N) where N is the number of elements.
# Space Complexity= O(1) because we don’t use any auxiliary space here









