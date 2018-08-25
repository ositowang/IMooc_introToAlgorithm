"""
快速排序在排序近乎有序的数组的时候，根据我们之前的Pivot选定方法
会退化为O(n**2)级别的算法，此处我们可以用随机选定pivot的方法来改进
我们的快排算法
"""
import random
#随机选定Pivot值的改进版本快排

def quick_sort1(arr,n):
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
    # 把待排序数组的第一个值作为基准值
    v = arr[l]
    j = l 
    for i in range(l+1,r+1):
        #如果右边的值比v小，就把它换到左边来
        if arr[i] < v:
            arr[j+1],arr[i] = arr[i],arr[j+1]
            j += 1
    #所有交换结束后，j位置左边的都比基准值小，j右边的都比基准值大，交换l和j
    arr[l],arr[j] = arr[j],arr[l]
    #返回新的基准值的位置
    return j

if __name__ == "__main__":
    #测试复现老师的原地快排
    test_list2 = [i for i in range(100)]
    # import time 
    # time1 = time.time()
    random.shuffle(test_list2)
    print(test_list2)
    quick_sort1(test_list2,len(test_list2))
    # time2 = time.time()
    # print(time2-time1)
    print(test_list2)