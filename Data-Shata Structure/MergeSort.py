def MergeSort(array):
    if len(array)>1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        MergeSort(left_array)
        MergeSort(right_array)

        # Lets merge both
        i = 0   # Tracking left Array left element
        j = 0   # Tracking right array right element
        k = 0   # Tracking merged array elements

        while i<len(left_array) and j<len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i<len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j<len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

        return array

array = [9, 8, 7, 6, 5, 4, 3, 2]
print(MergeSort(array))
