nums1 = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]


# 大根堆，从小到大排序
class HeapSort():

    def __init__(self, nums: list) -> None:
        self.nums = nums
        length = len(nums)
        end = length - 1
        self.build_heap(nums, end)
        while (end >= 0):
            temp = nums[0]
            nums[0] = nums[end]
            nums[end] = temp
            end -= 1
            for i in range((end - 1) // 2, -1, -1):
                self.Heap_once(nums, i, end)
            # print(nums)

    def build_heap(self, nums, end):
        for i in range((end - 1) // 2, -1, -1):
            self.Heap_once(nums, i, end)
            # print(nums)

    def Heap_once(self, nums, start, end):
        left_child_index = start * 2 + 1
        right_child_index = start * 2 + 2
        max_index = start
        if left_child_index <= end:
            if nums[left_child_index] > nums[max_index]:
                max_index = left_child_index
        if right_child_index <= end:
            if nums[right_child_index] > nums[max_index]:
                max_index = right_child_index
        if max_index != start:
            temp = nums[start]
            nums[start] = nums[max_index]
            nums[max_index] = temp
            self.Heap_once(nums, max_index, end)


# nums = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
heap_sort = HeapSort(nums3)
print(nums3)
