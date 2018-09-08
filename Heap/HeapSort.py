"""
堆排序
堆排序是利用堆这种数据结构而设计的一种排序算法，堆排序是一种选择排序，它的最坏，最好，平均时间复杂度均为O(nlogn)，它也是不稳定排序。
堆排序的基本思想是：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了
"""

# 引入下数据结构
class MaxHeap:

    def __init__(self, capacity,array=None):
        if array is None:
            self._array = [""] * (capacity+1)
            self._size = 0
            self.capacity = capacity 

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, value):
        # 我们的索引是从1开始的,所以我们要在索引+1的位置添加元素
        self._array[self._size+1] = value
        self._size += 1
        self._shiftUp(self._size)

    def _shiftUp(self, index):
        # 通过不断和父元素比较大小，将元素上浮到相应位置
        while index > 1 and self._array[index//2] < self._array[index]:
            self._array[index //
                        2], self._array[index] = self._array[index], self._array[index//2]
            index //= 2

    def extractMax(self):
        if not self._size > 0:
            raise IndexError("Can not extract from an empty Heap")
        rel = self._array[1]
        self._array[1], self._array[self._size] = self._array[self._size], self._array[1]
        self._size -= 1
        self._shiftDown(1)
        return rel

    def _shiftDown(self, index):
        # 在一个完全二叉树里，如果节点有左孩子节点，就一定有孩子节点
        while 2*index <= self._size:
            # 维护一个左孩子的索引
            j = 2*index
            # 如果该节点有有孩子，且右孩子比左孩子还大
            if (j+1) <= self._size and self._array[j+1] > self._array[j]:
                j += 1
            # 如果该节点比这俩孩子都大的话，什么都不用交换
            if self._array[index] >= self._array[j]:
                break
            # 否则，就和两个孩子中较大的那个交换
            self._array[index], self._array[j] = self._array[j], self._array[index]
            index = j 


def heapSort(arr,n):
    """
    @params arr: 待排序数组
    @params n: 数组的元素个数
    """
    maxHeap = MaxHeap(n)
    for i in arr:
        maxHeap.add(i)
    #从小到大排列
    for a in range(n-1,-1,-1):
        arr[a] = maxHeap.extractMax()


if __name__ == "__main__":
    # 测试堆排序
    import random
    test1 = [i for i in range(100)]
    random.shuffle(test1)
    print(test1)
    heapSort(test1,100)
    print(test1)
    


