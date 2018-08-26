"""
快排优化2:三路快排
三路快排是在双路快排的基础上进一步的优化，由于双路快排的时候没有对元素==基准值的情况进行处理，只是简单的继续平衡分割。但是实际上，我们并不需要处理等于基准值的这一部分，只需要对大于基准值和小于基准值的部分再次进行分割就可以了，等于基准值的部分，小于基准值，大于基准值部分已经天然有序了。
"""

import random


def quicksort_3Pass(arr, n):
    """
    @param arr: 待排序数组
    @param n: 待排序数组长度
    """
    __quick_sort(arr, 0, n-1)


def __quick_sort(arr, l, r):
    """
    @param arr:待排序数组
    @param l:左边界
    @param r:右边界
    """
    # 递归边界
    if l >= r:
        return
    # 构造一个随机下标
    index = random.randint(l, r)
    # 交换一下随机下标和最左侧的值，这样可以不动后面的逻辑
    arr[l], arr[index] = arr[index], arr[l]
    # 把待排序数组的第一个值作为基准值
    v = arr[l]
    # 这个指针负责arr[l+1...lt] < v，初始区间为空
    lt = l
    # 这个指针负责arr[gt...r] > v，初始区间为空
    gt = r+1
    # 这个指针负责arr[lt+1...i) == v，初始区间也为空
    i = l+1
    while i < gt:
        # 如果i位置的值小于基准值的话，交换它和lt+1位置的值，并把lt++
        if arr[i] < v:
            arr[i], arr[lt+1] = arr[lt+1], arr[i]
            # 此时由于i已经扫描过当前元素了，可以扫描下一个元素了
            i += 1
            lt += 1
        elif arr[i] > v:
            arr[i], arr[gt-1] = arr[gt-1], arr[i]
            # 此时由于i换过来的是还没有扫描过的元素，所以i不需要++操作，继续处理当前元素就好
            gt -= 1
        # 如果相等 就不用管了，继续++就好
        else:
            i += 1
    # 循环结束以后，我们只需要把基准值和lt位置的值交换一下位置，整个数组就已经分割好了
    arr[l], arr[lt] = arr[lt], arr[l]
    # lt，gt是闭区间
    __quick_sort(arr, l, lt-1)
    __quick_sort(arr, gt, r)


if __name__ == "__main__":
    #测试复现老师的原地快排
    test_list2 = [i for i in range(100)]
    random.shuffle(test_list2)
    # import time 
    # time1 = time.time()
    print(test_list2)
    quicksort_3Pass(test_list2,len(test_list2))
    print(test_list2)
    # time2 = time.time()
    # print(time2-time1)
    print("ok")