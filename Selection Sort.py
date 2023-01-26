def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])


array = [37, 88, 63, 39, 68, 1, 85, 49, 33, 21]
print('The unsorted array is: ')
print(array)

size = len(array)
selectionSort(array, size)
print('The sorted array in ascending order is:')
print(array)