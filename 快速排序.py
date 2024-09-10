import numpy as np
import random
import time

nums1 = [5, 2, 8, 1,5, 9, 3]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]
nums6 = [random.randint(0, 50) for _ in range(1000)]


def partition(nums, left, right):
    pivot_p = random.randint(left, right)
    nums[left], nums[pivot_p] = nums[pivot_p], nums[left]
    pivot = nums[left]
    left_point = left
    right_point = right
    while (left_point < right_point):
        while nums[right_point] >= pivot and left_point < right_point:
            right_point -= 1
        nums[left_point] = nums[right_point]
        while (nums[left_point] <= pivot and left_point < right_point):
            left_point += 1
        nums[right_point] = nums[left_point]
    nums[left_point] = pivot
    return left_point


def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid+1 , right)


time_start = time.time()
length = len(nums1)
quick_sort(nums1, 0, length - 1)
time_end = time.time()
print(nums1)
print('time:', time_end - time_start)

# import random

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = random.choice(arr)  # 随机选择基准元素
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # 示例用法
# time_start = time.time()
# length = len(nums6)
# ans = quick_sort(nums6)
# time_end = time.time()
# print(ans)
# print('time:', time_end - time_start)

