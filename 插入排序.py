nums1 = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]


def charu(nums):
    length = len(nums)
    for i in range(1, length):
        if nums[i] < nums[i - 1]:
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break


charu(nums5)
print(nums5)