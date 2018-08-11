
# 基本的冒泡算法
def bubble_sort(seq):  # O(n^2), n(n-1)/2 = 1/2(n^2 + n)
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):  # 这里之所以 n-1 还需要 减去 i 是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


#改进的冒泡排序
"""
鸡尾酒排序等于是冒泡排序的轻微变形。不同的地方在于从低到高然后从高到低，而冒泡排序则仅从低到高去比较序列里的每个元素。
他可以得到比冒泡排序稍微好一点的效能，原因是冒泡排序只从一个方向进行比对(由低到高)，每次循环只移动一个项目。 
数组中的数字本是无规律的排放，先找到最小的数字，把他放到第一位，然后找到最大的数字放到最后一位。
然后再找到第二小的数字放到第二位，再找到第二大的数字放到倒数第二位。以此类推，直到完成排序。
"""

def bubble_sortbetter(seq):
    n = len(seq)
    low,high = 0,n-1
    while low < high:
        swapPos = low
        #顺序扫描把最大的扔到后面去
        for j in range(low,high):
            if seq[j] > seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]               
                swapPos=j
        #更新上界
        high = swapPos
        #逆序扫描把最小的扔到最前面去
        for j in range(high,low,-1):
            if seq[j] < seq[j-1]:
                seq[j],seq[j-1] = seq[j-1],seq[j]
                swapPos=j
            #更新下界
            low = swapPos
    return seq


if __name__ == "__main__":
    a = [ i for i in range(1000)]
    import random
    random.shuffle(a)
    assert bubble_sortbetter(a) == sorted(a)
    print("ok")






