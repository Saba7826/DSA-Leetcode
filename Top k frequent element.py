from typing import List


def top_k_element(nums: List[int], k: int) -> List[int]:  # nums = [1, 2, 3, 3, 4, 4, 4]
    hmap = {}   # {num : count} --> {1:1, 2:1, 3:1+1=2, 4:1+1+1=3} -->{1:1, 2:1, 3:2, 4:3}
    freq = [[] for i in range(len(nums) + 1)]   # freq = [[],[],[],[],[],[],[],[]]

    for num in nums:  # for num = 1, num=2, num=3, num=3, num=4, num=4,num=4
        hmap[num] = 1 + hmap.get(num, 0)  # {1 : 1}
    for num, count in hmap.items():
        freq[count].append(num)  # -> freq = [[],[1,2],[3],[4],[],[],[],[]]

    result = []
    for i in range(len(freq)-1, 0, -1): # for i=7, i=6, i=5, i=4, i=3, i=2
        for num in freq[i]:    # for num in freq[3]
            result.append(num) # result = [4, 3]
            if len(result) == k:
                return result


nums = [1, 2, 3, 3, 4, 4, 4]
k = 2
print(top_k_element(nums, k))


# time: O(n), linear search
# space: O(n), space required for hashmap


































