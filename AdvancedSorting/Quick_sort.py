"""
选择基准值 pivot 将数组分成两个子数组：小于基准值的元素和大于基准值的元素。
这个过程称之为 partition。对这两个子数组进行快速排序。合并结果
"""

#我的原生python写法

def quick_sort(array):
    """
    @array: list to be sorted
    """
    if len(array) < 2:
        return array
    else:
        #把第一个元素当成基准值，对原数组就行分组
        pivot_index = 0 
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index+1:] if i <= pivot]
        larger_part = [i for i in array[pivot_index+1:] if i > pivot]
        return quick_sort(less_part)+[pivot]+quick_sort(larger_part)



# In-place修改的快速排序,左闭右开
def quick_sort_inplace(array,beg,end):
    """
    @param array: list to be parted 
    @param beg: beginning index
    @param end: end index
    """
    if beg < end:
        pivot = partition(array,beg,end)
        quick_sort_inplace(array,beg,pivot)
        quick_sort_inplace(array,pivot+1,end)

#更好的一个切分原数组的函数
def partition(array,beg,end):
    """
    @param array: list to be parted 
    @param beg: beginning index
    @param end: end index
    @return: new pivot index
    """
    #第一个元素作为pivot
    pivot_index = beg 
    pivot = array[pivot_index]
    left = pivot_index+1
    right = end-1
    while True:
        # 找到左指针指向的第一个比pivot大的值，找到了 进入下面的找右边比pivot小的值
        while left <= right and array[left] < pivot:
            left += 1
        #找到右指针指向的第一个比pivot小的值，找到了 进入下面的交换环节
        while right >= left and array[right] >= pivot:
            right -= 1
        # 如果左指针大于了右指针，表示左边的值比Pivot的都要小，右边的值都比pivot要大
        if left > right:
            break
        else:
            #交换元素
            array[left],array[right] = array[right],array[left]
    #最后 交换一下右指针和pivot的位置,不明白的画下图就好了，找到最后一步的时候也就是left>right的时候
    #这时候的right位置就是pivot应该待的位置
    array[pivot_index],array[right] = array[right],array[pivot_index]
    # 返回Pivot位置
    return right

#根据老师c++代码，用python复现的方式，左闭右闭

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
    #把待排序数组的第一个值作为基准值
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
    #首先测试我自己的Python写法
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    print("partition ok!")
    #测试第一个非原地排序的快排
    test_list = [i for i in range(100)]
    import random 
    random.shuffle(test_list)
    assert quick_sort(test_list) == sorted(test_list)
    print("quick_sort ok")

    #测试第二个原地排序的快排
    quick_sort_inplace(test_list,0,len(test_list))
    print(test_list)

    #测试复现老师的原地快排
    test_list2 = [i for i in range(50)]
    random.shuffle(test_list2)
    quick_sort1(test_list2,len(test_list2))
    print(test_list2)

