"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
求解数组中的第K大元素
思路1：
直接排序一下，数到位置就可以了，这里不写了。n*logn级别
思路2：
利用快排的思想，在我们进行快排的时候，我们利于基准点将数组分割成两个部分，而基准点的下标其实正好就是基准点这个值在排序后数组的位置。此外，基准点左边的元素都小于基准点，基准点右边的元素都大于基准点，我们只需要把比较一下k和基准值下标的大小就可以了，如果大于就去右边继续找，小于就去左边找，直到最后找到。n级别的复杂度。
"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def _findKthLargest(nums,k):
            #nums肯定有效这里就不判断了
            index = self.__partrition(nums,0,len(nums)-1)
            # 这里 Index 要加 1 才能代表 pivot 是 nums 中的第几大
            if k < index+1:
                return _findKthLargest(nums[:index],k)
            elif k > index+1:
                #这里需要去除掉index+1的偏移量，因为是从index+1开始找起的
                return _findKthLargest(nums[index+1:],k-index-1)
            else:
                return nums[index]
        import random
        #这里借鉴了一下别人的防止退化到on**2算法的，直接打乱一下数组
        random.shuffle(nums)
        return _findKthLargest(nums,k)
            
     
    #借用一下快排的分割函数
    def __partrition(self,nums,start,end):
        """
        这里有个坑
        这里需要反过来想一下，如果我们直接借用快排的思想的话，那么左边的都小，右边的都大.但这里其实是跟题目要求的正好反过来了。左边的要比基准值大，我们才能正确求出基准值是最后排序数组中的大，否则还需要去取反一下。
        @param arr:待排序数组
        @param l:左边界
        @param r:右边界
        @return j: 新的基准值的位置
        """
        pIndex = start
        pivot = nums[end]
        for i in range(start, end):
            if nums[i] > pivot:
                nums[i], nums[pIndex] = nums[pIndex], nums[i]
                pIndex += 1
        nums[pIndex], nums[end] = nums[end], nums[pIndex]
        return pIndex
        
