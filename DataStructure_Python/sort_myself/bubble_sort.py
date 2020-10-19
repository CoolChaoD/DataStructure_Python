# coding=gbk
# author=ChaoD
# date:2020/10/19 20:43


def bubbleSort(arr):
    flag = 0  # 标志位用来检测某一轮是否发生了交换
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                flag = 1
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        if flag == 0:
            break
        else:
            flag = 0

        print("第%d轮" % (i + 1), arr)


if __name__ == '__main__':
    arr = [5, 4, 3, 1, 2]
    bubbleSort(arr)
