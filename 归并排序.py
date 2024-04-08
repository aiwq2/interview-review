nums1 = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]
nums6 = [3, 4, 2, 1]


def merge(nums, left, middle, right):
    nums_temp = []
    left_point = left
    right_point = middle + 1
    while left_point <= middle and right_point <= right:
        if nums[left_point] < nums[right_point]:
            nums_temp.append(nums[left_point])
            left_point += 1
        else:
            nums_temp.append(nums[right_point])
            right_point += 1
    if left_point > middle:
        nums_temp.extend(nums[right_point:right + 1])
    else:
        nums_temp.extend(nums[left_point:middle + 1])
    # print(nums_temp)
    for i in range(left, right + 1):
        nums[i] = nums_temp[i - left]


def guibing(nums, left, right):
    if left < right:
        middle = (left + right) // 2
        guibing(nums, left, middle)
        guibing(nums, middle + 1, right)
        merge(nums, left, middle, right)


length = len(nums5)
guibing(nums5, 0, length - 1)
print(nums5)
