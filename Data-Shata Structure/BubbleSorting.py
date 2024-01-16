def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[i] = customList[i], customList[j]
    print(customList)


cList = [10, 5, 6, 8, 7, 2, 1, 13]
bubbleSort(cList)
