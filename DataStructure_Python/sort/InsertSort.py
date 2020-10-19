arr = [4, 3, 2, 1]

for i in range(1, 4):
    insertValue = arr[i]
    insertIndex = i - 1
    while insertIndex >= 0 and insertValue < arr[insertIndex]:
        arr[insertIndex + 1] = arr[insertIndex]
        insertIndex -= 1
    arr[insertIndex + 1] = insertValue
    print("第%d轮的进结果为：" % i, arr)
