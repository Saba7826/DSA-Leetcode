from typing import List


def group_anagram(strs: List[str]) -> List[str]:
    if len(strs) == 0:
        return []

    hashmap = {}  # {tuple : List} # tuple as freq count : list of anagram

    for word in strs:
        freq_count = [0] * 26
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for ch in word:
            freq_count[ord(ch) - ord('a')] += 1

        freq_count = tuple(freq_count)

        if freq_count not in hashmap.keys():
            hashmap[freq_count] = [word]
        else:
            hashmap[freq_count].append(word)

    return hashmap.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(strs))

# Time:O(n.m) , where n is the number of strings and m is the length of characters in each string
# Space: O(n), extra space used by hashmap

# ascci value
# a = 97, b = 98,... z = 122

# freq_count[ord(ch) - ord('a')] += 1 --> freq_count[ord(ch) - ord('a')] = freq_count[ord(ch) - ord('a')] + 1
#        freq_count  word='eat'
# a = [0] = 0  + 1 = 1
# b = [1] = 0
# c = [2] = 0
# d = [3] = 0
# e = [4] = 0 + 1 = 1
# f = [5] = 0
# g = [6] = 0
# h = [7] = 0
# i = [8] = 0
# j = [9] = 0
# k = [10] = 0
# l = [11] = 0
# m = [12] = 0
# n = [13] = 0
# o = [14] = 0
# p = [15] = 0
# q = [16] = 0
# r = [17] = 0
# s = [18] = 0
# t = [19] = 0 + 1 = 1
# u = [20] = 0
# v = [21] = 0
# w = [22] = 0
# x = [23] = 0
# y = [24] = 0
# z = [25] = 0

