"""
N2级别排序
插入排序
每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素
"""

def insertion_sorting(array):
    
    n = len(array)
    for i in range(1, n):
        value = array[i]    # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        pos = i
        while pos > 0 and value < array[pos-1]:
            array[pos] = array[pos-1]  # 如果前边的元素比它大，就让它一直前移
            pos -= 1
        array[pos] = value    # 找到了合适的位置赋值就好
    return array


if __name__ == "__main__":
    test_array = [i for i in range(1000)]
    import random
    random.shuffle(test_array)
    assert insertion_sorting(test_array) == sorted(test_array)
    print("ok")