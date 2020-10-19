def selectSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = arr[i]
        minIndex = i
        for j in range(i + 1, n):
            if min > arr[j]:
                minIndex = j  # 最小数的索引
                min = arr[j]  # 最小数的下标

        if minIndex!=i:
            arr[minIndex] = arr[i]
            arr[i] = min
        print("选择排序第%d轮" % (i + 1), arr)


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    selectSort(arr)
