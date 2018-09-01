"""
最大堆:
最大（小）堆是指在树中，存在一个结点而且该结点有儿子结点，该结点的data域值都不小于（大于）其儿子结点的data域值，并且它是一个完全二叉树（不是满二叉树）。
"""


class MaxHeap:

    def __init__(self, capacity):
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


if __name__ == "__main__":
    import random
    myheap = MaxHeap(10)
    for i in range(10):
        myheap.add(random.randint(0, 100))
    while not myheap.isEmpty():
        print(myheap.extractMax())
