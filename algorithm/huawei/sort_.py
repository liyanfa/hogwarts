# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 17:41
# @Author  : yanfa
# @user   : yanfa 
# @File    : sort_.py
# @remark: 常用排序方法

"""一、冒泡排序
比较相邻的两个元素，如果前面的元素比后面的元素大，则交换它们的位置。重复此操作，直到整个序列都有序为止
缺点：但在实际应用中效率较低，只适用于数据量较小的情况。"""

def maopao_sort(arr:list):
    n=len(arr)
    #外层循环，遍历数组的每一个元素，共进行n轮排序。
    for i in range(n):
        #内层循环，遍历未排序的部分，共进行n-i-1次比较和交换。
        for j in range(n-i-1):
            #比较相邻的两个元素是否需要交换。
            if arr[j]>arr[j+1]:
                #arr[j], arr[j+1] = arr[j+1], arr[j]：
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[992,67,188,1000]
print(maopao_sort(arr))

""""""