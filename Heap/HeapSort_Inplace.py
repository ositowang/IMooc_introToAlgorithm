"""
原地堆排序
"""


def heapSort(arr, n):
    """
    @param arr: 待排序数组
    @param n: 数组长度
    """
    # 先把进来的数组转化成堆，由于这里是索引为0的堆，
    # 所以最后一个非叶子节点是(n-2)//2,终止位置是0
    for i in range((n-2)//2, -1, -1):
        __shiftDown(arr, n, i)
    # 根据堆的定义，数组第一个元素是最大的元素，我们为了从小到大排序
    # 需要把最后一个位置的元素和第一个位置的元素交换
    # 然后对新的第一个位置的元素shiftDown
    for a in range(n-1, 0, -1):
        arr[0], arr[a] = arr[a], arr[0]
        # 由于每循环一次，数组的长度就应该-1，因为后面的已经排好序了。
        __shiftDown(arr, a, 0)


def __shiftDown(arr, n, k):
    """
    @param arr: 待排序数组
    @param n: 数组长度
    @param k: 待下沉的元素下标
    """
    # 基本的工作原理和之前的shiftdown是差不多的，只是索引有所变化
    while 2*k+1 < n:
        j = 2*k + 1
        if j+1 < n and arr[j+1] > arr[j]:
            j += 1
        if arr[k] >= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


if __name__ == "__main__":
    import random
    test1 = [i for i in range(10)]
    random.shuffle(test1)
    print(test1)
    heapSort(test1, len(test1))
    print(test1)
