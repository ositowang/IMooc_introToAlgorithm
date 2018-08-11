"""
原理：
将递归分解列表，直至最小（即每个列表仅有一个元素）
将列表分解最小之后，递归合并两个列表，即挨个比较两个列表中最前面的元素，谁较小就将谁加入新的列表，
而后该列表的下标后移一位，继续比较，
直至其中一个列表为空，而后将另一个列表中剩余的元素加入新列表
不断合并，直至完全排序完成
"""



def merge_sort(arr):
    #最小情况
    if len(arr) <= 1:
        return arr
    #拆分原数组
    mid = len(arr)//2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    #递归合并最小情况，逐层返回
    return merge(left,right)


def merge(left,right):
    #构造新空间 存放合并后的数组
    result = []
    #维护两个下标指针
    i,j=0,0
    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            #此时左数组 下标+1，方便下一次比较
            i += 1
        else:
            result.append(right[j])
            j += 1
    #由于左右数组可能长度不一致，最后将两个数组中有剩余的数字添加到结果集中
    #由于左右数组都是排序数组，剩余的元素一定比已经添加到数组中元素大，所以可以放心的添加到数组的末尾
    #此处使用了比较暴力的方法，直接都加一遍，如果你愿意，也可以进行比较一下，最后决定加哪个
    result += left[i:]
    result += right[j:]
    return result


if __name__ == "__main__":
    arr_test = [i for i in range(1000)]
    import random
    random.shuffle(arr_test)
    print(arr_test)
    assert merge_sort(arr_test) == sorted(arr_test)
    print(merge_sort(arr_test))
    print("ok!")
