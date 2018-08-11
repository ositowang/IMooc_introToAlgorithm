"""
N平法复杂度的算法
选择排序
我们从第一个开始，从头到尾找一个个头最小的小盆友，然后把它和第一个小盆友交换。 然后从第二个小盆友开始采取同样的策略，这样一圈下来小盆友就有序了。
"""


def selection_sort(array):
    for i in range(0,len(array)):
        # 假设当前下标的值是最小的
        min_index = i 
        # 从当前下标的下一个开始遍历
        for j in range(i+1,len(array)):
            #如果值小于当前的最小值，就更新当前最小值的下标
            if array[j] < array[min_index]:
                min_index = j 
        #最后交换当前下标和当前最小值
        array[i],array[min_index] = array[min_index],array[i]
    return array