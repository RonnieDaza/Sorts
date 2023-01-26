def partition(array, low, high):

  pivot = array[high]

  i = low - 1


  for j in range(low, high):
    if array[j] <= pivot:

      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)


data = [37, 88, 63, 39, 68, 1, 85, 49, 33, 21]
print("The unsorted array is: ")
print(data)