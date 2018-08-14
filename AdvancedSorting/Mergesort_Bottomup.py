<<<<<<< HEAD
"""
自底向上的归并排序法，首先将原数组划分成小块，然后逐个把小块合并成大块
直至完成整个数组的排序
"""


def Merge_bottomup(lst):
    """
    @param lst: list to be sorted
    """
    # 判断一下边界情况
    if not lst:
        return []
    # 拆分成嵌套列表，每个列表是单个元素，以便后面合并
    lists = [[x] for x in lst]
    # 如果还有列表没有合并
    while len(lists) > 1:
        lists = merge_lists(lists)
    # 合并到最后只剩一个元素，取出来就好
    return lists[0]


def merge_lists(lists):
    """
    @param lists: nested list containing the individual elements of the original list
    """
    result = []
    # 合并数组
    for i in range(0, len(lists) // 2):
        result.append(merge2(lists[i*2], lists[i*2 + 1]))
    # 如果合并完还有剩下的数组，加入结果中
    if len(lists) % 2:
        result.append(lists[-1])
    return result


def merge2(leftpart, rightpart):
    """
    @param leftpart: one of the sublist to be merged 
    @param rightpart: one of the sublist to be merged 
    """
    i = 0
    j = 0
    result = []
    # 双指针指向两个待合并的数组
    while i < len(leftpart) and j < len(rightpart):
        x = leftpart[i]
        y = rightpart[j]
        # 思路和正常的归并排序一样
        if x > y:
            result.append(y)
            j += 1
        else:
            result.append(x)
            i += 1
    # 如果两个待合并数组长度不一致，分别加上剩下的元素。因为已经都是排序数组了，多出来的元素可以直接加进去
    result.extend(leftpart[i:])
    result.extend(rightpart[j:])
    return result


if __name__ == "__main__":
    arr_test = [i for i in range(10000)]
    import random
    random.shuffle(arr_test)
    import time
    time1 = time.time()
    Merge_bottomup(arr_test)
    time2 = time.time()
    print(time2-time1)
    # 测试了一下 在10000数据下 大概比正常的归并排序 快0.5s左右
    assert Merge_bottomup(arr_test) == sorted(arr_test)
    print("ok")
=======
"""
自底向上的归并排序法，首先将原数组划分成小块，然后逐个把小块合并成大块
直至完成整个数组的排序
"""


def Merge_bottomup(lst):
    """
    @param lst: list to be sorted
    """
    # 判断一下边界情况
    if not lst:
        return []
    # 拆分成嵌套列表，每个列表是单个元素，以便后面合并
    lists = [[x] for x in lst]
    # 如果还有列表没有合并
    while len(lists) > 1:
        lists = merge_lists(lists)
    # 合并到最后只剩一个元素，取出来就好
    return lists[0]


def merge_lists(lists):
    """
    @param lists: nested list containing the individual elements of the original list
    """
    result = []
    # 合并数组
    for i in range(0, len(lists) // 2):
        result.append(merge2(lists[i*2], lists[i*2 + 1]))
    # 如果合并完还有剩下的数组，加入结果中
    if len(lists) % 2:
        result.append(lists[-1])
    return result


def merge2(leftpart, rightpart):
    """
    @param leftpart: one of the sublist to be merged 
    @param rightpart: one of the sublist to be merged 
    """
    i = 0
    j = 0
    result = []
    # 双指针指向两个待合并的数组
    while i < len(leftpart) and j < len(rightpart):
        x = leftpart[i]
        y = rightpart[j]
        # 思路和正常的归并排序一样
        if x > y:
            result.append(y)
            j += 1
        else:
            result.append(x)
            i += 1
    # 如果两个待合并数组长度不一致，分别加上剩下的元素。因为已经都是排序数组了，多出来的元素可以直接加进去
    result.extend(leftpart[i:])
    result.extend(rightpart[j:])
    return result


if __name__ == "__main__":
    arr_test = [i for i in range(10000)]
    import random
    random.shuffle(arr_test)
    import time
    time1 = time.time()
    Merge_bottomup(arr_test)
    time2 = time.time()
    print(time2-time1)
    # 测试了一下 在10000数据下 大概比正常的归并排序 快0.5s左右
    assert Merge_bottomup(arr_test) == sorted(arr_test)
    print("ok")
>>>>>>> 3eb368cc06f74535916421a0f4ac8ba4e3d7801c
