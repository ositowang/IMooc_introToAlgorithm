"""
基本思想是：先比较距离远的元素，而不是像简单交换排序算法那样先比较相邻的元素，这样可以快速减少大量的无序情况，
从而减轻后续的工作。被比较的元素之间的距离逐步减少，直到减少为1，这时的排序变成了相邻元素的互换。
有毒的讲解视频：
https://v.youku.com/v_show/id_XNTA3NDUxMjcy.html
"""

def shell_sort(arr):
    n = len(arr)
    gap = n//2
    #直到gap为1的时候，停止循环，这时候排序变成了相邻元素互换
    while gap > 0:
        #根据gap对原数组进行分组
        for i in range(gap,n):
            j = i
            #如有需要，交换间隔为gap的两个元素 
            while j >= gap and arr[j-gap] > arr[j]:
                arr[j-gap],arr[j] = arr[j],arr[j-gap]
                j -= gap
        gap = gap//2
    return arr



if __name__ == "__main__":
    arr1 = [i for i in range(100)]
    import random
    random.shuffle(arr1)
    print(shell_sort(arr1))