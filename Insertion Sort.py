def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
               
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


array = [37, 88, 63, 39, 68, 1, 85, 49, 33, 21]
print('The unsorted array is: ')
print(array)