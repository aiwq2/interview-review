nums1 = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]

import math


def xuanze(nums):
    length = len(nums)
    for i in range(length):
        min = nums[i]
        min_loc = i
        for j in range(i + 1, length):
            if nums[j] < min:
                min = nums[j]
                min_loc = j
        nums[i], nums[min_loc] = nums[min_loc], nums[i]


xuanze(nums5)
print(nums5)