nums1 = [2, 1, 5, 1, 3, 2, 1, 1, 8, 5, 2]
nums2 = []
nums3 = [2, -1, 5, 1, -3, 2, 1, 1, 8, -5, 2]
nums4 = [1]
nums5 = [2, 1]


def bucket_sort(array):
    min_num, max_num = min(array), max(array)
    bucket_num = (max_num - min_num) // 3 + 1
    buckets = [[] for _ in range(int(bucket_num))]
    for num in array:
        buckets[int((num - min_num) // 3)].append(num)
    new_array = list()
    for i in buckets:
        for j in sorted(i):
            new_array.append(j)
    return new_array


ans = bucket_sort(nums1)
print(ans)