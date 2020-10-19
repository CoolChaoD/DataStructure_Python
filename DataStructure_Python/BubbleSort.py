def bubbleSort(arr):
    n = len(arr)  # 求数组的长度
    temp = 0
    flag = 0
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

        print("第%d轮：" % (i + 1), arr)


if __name__ == '__main__':
    arr = [3, 2, 1, 4, 5]
    bubbleSort(arr)
