def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


array = [37, 88, 63, 39, 68, 1, 85, 49, 33, 21]
print('The unsorted array is: ')
print(array)

bubbleSort(array)

print('The sorted array in ascending order is: ')
print(array)