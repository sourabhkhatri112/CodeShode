def SelectionSort(custom_list):
    for i in range(len(custom_list) - 1):
        for j in range(i, len(custom_list)):
            if custom_list[i] > custom_list[j]:
                custom_list[i], custom_list[j] = custom_list[j], custom_list[i]

    print(custom_list, end=' ')


lists = [5, 4, 3, 2, 1]
SelectionSort(lists)
