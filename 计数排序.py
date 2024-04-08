nums1 = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]

import math


def jishu(nums):
    if len(nums) <= 1:
        return nums
    min_n = math.inf
    max_n = -math.inf - 1
    for num in nums:
        if num < min_n:
            min_n = num
        if num > max_n:
            max_n = num
    count = [0] * (max_n - min_n + 1)
    for num in nums:
        count[num - min_n] += 1
    nums_temp = []
    for i in range(len(count)):
        nums_temp.extend([(min_n + i)] * count[i])
    return nums_temp


ans = jishu(nums5)
print(ans)