def twoSum(nums, target):
    hashmap = {}  # {value : idx}

    for idx, value in enumerate(nums):
        # print(idx, value)
        diff = target - value
        if diff in hashmap:
            return [hashmap[diff], idx]  # return diff at index
        else:
            hashmap[value] = idx   # return value at index
            print(hashmap)


nums = [2, 7, 11, 13]
target = 9
print("twoSum:", twoSum(nums, target))


# Time complexity: O(n), we iterate over list of elements in array
# space complexity: O(n), extra space used by hashmap to store n elements
