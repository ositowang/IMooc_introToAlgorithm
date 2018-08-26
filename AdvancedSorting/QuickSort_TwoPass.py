"""
快排优化1：双路快速排序
之前的快排算法，对于出现大量重复值的数组进行排序，尽管我们有随机化选定基准值的优化，但是由于有大量重复，也就是相等的值
我们在分割子数组的时候，可能会出现左右数组长度严重失衡的情况，这种情况下，快排就会退化到接近n**2复杂的算法，双路快排
从两端开始扫描数组，可以更有效的将数组进行分割。双路快排指针还是一个，但是是从两边夹攻，他的结果就是即使你是和指针相等的，我也交换，这样就避免了，不平衡的出现，我们的快排又回到O(nlog2N)的时间复杂度
"""
import random

def quicksort_twoPass(arr,n):
    """
    @param arr: 待排序数组
    @param n: 待排序数组长度
    """
    __quick_sort(arr,0,n-1)

def __quick_sort(arr,l,r):
    """
    @param arr:待排序数组
    @param l:左边界
    @param r:右边界
    """
    #递归边界
    if l >= r:
        return 
    p = __partrition(arr,l,r)
    __quick_sort(arr,l,p-1)
    __quick_sort(arr,p+1,r)

def __partrition(arr,l,r):
    """
    @param arr:待排序数组
    @param l:左边界
    @param r:右边界
    @return j: 新的基准值的位置
    """
    # 构造一个随机下标
    index = random.randint(l,r)
    #交换一下随机下标和最左侧的值，这样可以不动后面的逻辑
    arr[l],arr[index] = arr[index],arr[l]
    #把待排序数组的第一个值作为基准值
    v = arr[l]
    # arr[l+1...i) <= v,arr(j...r]
    i, j = l+1, r
    while True:
        # 找到左指针指向的第一个比pivot大的值，找到了 进入下面的找右边比pivot小的值
        while i <= r and arr[i] < v:
            i += 1
        #找到右指针指向的第一个比pivot小的值，找到了 进入下面的交换环节
        while j >= l+1 and arr[j] > v:
            j -= 1
        # 如果左指针大于了右指针，表示左边的值比Pivot的都要小，右边的值都比pivot要大
        if i > j :
            break
        else:
            arr[i],arr[j] = arr[j],arr[i]
    #最后 交换一下右指针和pivot的位置,不明白的画下图就好了，找到最后一步的时候也就是left>right的时候
    #这时候的right位置就是pivot应该待的位置
    arr[l],arr[j] = arr[j],arr[l]
    return j 


if __name__ == "__main__":
    #测试复现老师的原地快排
    test_list2 = [i for i in range(100000)]
    random.shuffle(test_list2)
    import time 
    time1 = time.time()
    quicksort_twoPass(test_list2,len(test_list2))
    time2 = time.time()
    print(time2-time1)
    print("ok")
