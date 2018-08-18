"""
原理：
将递归分解列表，直至最小（即每个列表仅有一个元素）
将列表分解最小之后，递归合并两个列表，即挨个比较两个列表中最前面的元素，谁较小就将谁加入新的列表，
而后该列表的下标后移一位，继续比较，
直至其中一个列表为空，而后将另一个列表中剩余的元素加入新列表
不断合并，直至完全排序完成
"""
# 我的原生python写法


def merge_sort(arr):
    """
    @param arr: list to be sorted
    @return: list sorted 
    """
    # 最小情况
    if len(arr) <= 1:
        return arr
    # 拆分原数组
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 递归合并最小情况，逐层返回
    return merge(left, right)


def merge(left, right):
    """
    @param left: left part subarray of the initial array
    @param right: right part subarray of the initial array
    @return:
    """
    # 构造新空间 存放合并后的数组
    result = []
    # 维护两个下标指针
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            # 此时左数组 下标+1，方便下一次比较
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 由于左右数组可能长度不一致，最后将两个数组中有剩余的数字添加到结果集中
    # 由于左右数组都是排序数组，剩余的元素一定比已经添加到数组中元素大，所以可以放心的添加到数组的末尾
    # 此处使用了比较暴力的方法，直接都加一遍，如果你愿意，也可以进行比较一下，最后决定加哪个
    result += left[i:]
    result += right[j:]
    return result


# 根据老师的C++代码，用python复现的写法

def merge_sort1(arr, n):
    """
    @param arr: list to be sorted
    @param n: length of the arr

    """
    __mergesort(arr, 0, n-1)


def __mergesort(arr, start, end):
    """
    @param arr: list to be sorted 
    @param start: starting point we want to merge
    @param end: ending point we want to merge
    """
    if start >= end:
        return
    mid = (start+end)//2
    __mergesort(arr, start, mid)
    __mergesort(arr, mid+1, end)
    if arr[mid] > arr[mid+1]:
        __merge(arr, start, mid, end)

# 合并[l..mid],[mid+1,r]两个部分的数组


def __merge(arr, l, mid, r):
    """
    @param arr: list to be merged 
    @param l: starting point of the array
    @param mid: middle point
    @param r: ending point
    """
    # 由于考察的是闭区间，所以要把1+回来
    result_list = [0]*(r-l+1)
    # 同理闭区间,arr是从l开始的，result_list是从0开始的
    for i in range(l, r+1):
        result_list[i-l] = arr[i]
    i, j = l, mid+1
    for k in range(l, r+1):
        # 处理i越界，j还没越界的情况
        if(i > mid):
            arr[k] = result_list[j-l]
            j += 1
        # 处理j越界的情况
        elif (j > r):
            arr[k] = result_list[i-l]
            i += 1
        # 如果左边的小，左边的排序到数组的左边
        elif result_list[i-l] < result_list[j-l]:
            arr[k] = result_list[i-l]
            i += 1
        else:
            arr[k] = result_list[j-l]
            j += 1


if __name__ == "__main__":
    arr_test = [i for i in range(10000)]
    import random
    random.shuffle(arr_test)
    print(arr_test)
    print("good boy")
    import time
    time1 = time.time()
    merge_sort1(arr_test,len(arr_test))
    time2 = time.time()
    print(time2-time1)
    print("ok!")
