# coding=gbk
# author=ChaoD
# date:2020/10/19 20:43

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            print("第%d轮%d次" % (i + 1, j+1), arr)


if __name__ == '__main__':
    arr = [5, 4, 3, 1, 2]
    bubbleSort(arr)
