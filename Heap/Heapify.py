"""
Heapify:

将list类型转化为heap
"""


class MaxHeap:
    def __init__(self, array):
        self._array = [""] * (len(array)+1)
        for i in range(0, len(array)):
            self._array[i+1] = array[i]
        self._size = len(array)
        for i in range(len(array)//2, 0, -1):
            self._shiftDown(i)

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
            # 如果该节点有右孩子，且右孩子比左孩子还大
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
    test1 = [i for i in range(10)]
    random.shuffle(test1)
    print(test1)
    myheap = MaxHeap(test1)
    print(myheap._array)
    for i in range(6):
        print(myheap.extractMax())
